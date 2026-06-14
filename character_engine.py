"""
Shared engine for character conversations.

Every character page imports run_character_page() and passes in their
specific configuration (system prompt, voice settings, starter questions, etc).
This keeps all the common logic - API calls, audio generation, transcript
download, usage tracking - in one place.
"""

import streamlit as st
import anthropic
from elevenlabs import ElevenLabs
import base64
import tempfile
import os
import re
import time
from datetime import datetime

from auth import (
    check_login,
    usage_sidebar,
    has_messages_remaining,
    increment_usage,
)


def get_secret(key, default=""):
    try:
        return st.secrets[key]
    except Exception:
        return default


def generate_audio(text, eleven_key, voice_id, voice_settings):
    """Generate audio from text via ElevenLabs. Returns base64 string or None."""
    text = re.sub(r'[\*\_\#\`]', '', text)
    text = re.sub(r'\s*\u2014\s*', ', ', text)
    text = re.sub(r' - ', ', ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = text[:800]
    try:
        client = ElevenLabs(api_key=eleven_key)
        audio = client.text_to_speech.convert(
            voice_id=voice_id,
            text=text,
            model_id="eleven_multilingual_v2",
            voice_settings=voice_settings,
        )
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            for chunk in audio:
                f.write(chunk)
            tmp_path = f.name
        with open(tmp_path, "rb") as f:
            audio_bytes = f.read()
        os.unlink(tmp_path)
        return base64.b64encode(audio_bytes).decode()
    except Exception as e:
        st.warning(f"Voice unavailable: {e}")
        return None


def play_audio(b64, char_key):
    if not b64:
        return
    uid = str(int(time.time() * 1000))
    st.markdown(
        f'<audio id="{char_key}_{uid}" controls '
        f'style="width:100%;margin-top:8px;border-radius:4px;">'
        f'<source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
        f'<script>(function(){{var a=document.getElementById("{char_key}_{uid}");'
        f'if(a)a.play().catch(()=>{{}});}})();</script>',
        unsafe_allow_html=True
    )


def get_ai_response(messages, api_key, system_prompt):
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        system=system_prompt,
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in messages
            if m["role"] in ("user", "assistant")
        ],
        temperature=0.9
    )
    return response.content[0].text


def build_transcript(messages, character_name, scene_label):
    """Build a downloadable text transcript of the conversation."""
    lines = []
    lines.append(f"History Lives — Conversation Transcript")
    lines.append(f"Character: {character_name}")
    lines.append(f"Scene: {scene_label}")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("=" * 60)
    lines.append("")

    for msg in messages:
        speaker = "YOU" if msg["role"] == "user" else character_name.upper()
        lines.append(f"{speaker}:")
        lines.append(msg["content"])
        lines.append("")

    return "\n".join(lines)


def run_character_page(config):
    """
    Main entry point for a character page.

    config is a dict with keys:
        - char_key: short identifier, e.g. "eisenhower"
        - character_name: display name, e.g. "General Eisenhower"
        - page_title, page_icon
        - header_html, briefing_html: HTML strings for header/briefing
        - scene_label: short description for transcript header
        - system_prompt: the full character system prompt
        - opening_message: first message from character
        - starter_questions: list of suggested questions
        - voice_id_secret_key: secrets key for this character's voice ID
        - voice_settings: dict of ElevenLabs voice settings
        - avatar_emoji: emoji for chat avatar
    """
    st.set_page_config(
        page_title=config["page_title"],
        page_icon=config["page_icon"],
        layout="centered"
    )

    # Shared styling
    st.markdown("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Special+Elite&family=IM+Fell+English:ital@0;1&display=swap');
      html, body, [class*="css"] { font-family: 'Special Elite', monospace; }
      .stChatMessage { font-family: 'IM Fell English', serif; font-size: 1rem; }
    </style>
    """, unsafe_allow_html=True)

    # Login gate
    if not check_login():
        return

    usage_sidebar()

    # API keys from secrets
    api_key = get_secret("ANTHROPIC_API_KEY")
    eleven_key = get_secret("ELEVENLABS_API_KEY")
    voice_id = get_secret(config["voice_id_secret_key"])

    if not api_key:
        st.error("System configuration error: API key not found. Please contact the administrator.")
        return

    with st.sidebar:
        voice_enabled = st.toggle(f"🔊 Enable Voice", value=True, key=f"voice_{config['char_key']}")
        st.markdown("---")
        st.markdown("### Suggested Questions")
        for q in config["starter_questions"]:
            if st.button(q, use_container_width=True, key=f"starter_{config['char_key']}_{q[:20]}"):
                st.session_state[f"starter_{config['char_key']}"] = q

    # Header and briefing
    st.markdown(config["header_html"], unsafe_allow_html=True)
    st.markdown(config["briefing_html"], unsafe_allow_html=True)

    # Chat state - namespaced per character
    msg_key = f"messages_{config['char_key']}"
    if msg_key not in st.session_state:
        st.session_state[msg_key] = [
            {"role": "assistant", "content": config["opening_message"]}
        ]

    audio_key = f"latest_audio_{config['char_key']}"

    def process_message(user_text):
        if not has_messages_remaining():
            return
        st.session_state[msg_key].append({"role": "user", "content": user_text})
        with st.spinner(""):
            reply = get_ai_response(
                st.session_state[msg_key], api_key, config["system_prompt"]
            )
            st.session_state[msg_key].append({"role": "assistant", "content": reply})
            increment_usage()
            if voice_enabled and eleven_key and voice_id:
                b64 = generate_audio(reply, eleven_key, voice_id, config["voice_settings"])
                st.session_state[audio_key] = b64
            else:
                st.session_state[audio_key] = None
        st.rerun()

    # Handle starter question click
    starter_state_key = f"starter_{config['char_key']}"
    if st.session_state.get(starter_state_key):
        q = st.session_state[starter_state_key]
        st.session_state[starter_state_key] = None
        process_message(q)

    # Render chat history
    for i, msg in enumerate(st.session_state[msg_key]):
        with st.chat_message(
            "user" if msg["role"] == "user" else "assistant",
            avatar=config["avatar_emoji"] if msg["role"] == "assistant" else "👤"
        ):
            st.write(msg["content"])
            is_last = (i == len(st.session_state[msg_key]) - 1)
            if is_last and msg["role"] == "assistant":
                audio_b64 = st.session_state.get(audio_key)
                if audio_b64:
                    play_audio(audio_b64, config["char_key"])
                    st.session_state[audio_key] = None

    # Chat input
    placeholder = f"Speak with {config['character_name']}..."
    if prompt := st.chat_input(placeholder):
        process_message(prompt)

    # Transcript download
    st.markdown("---")
    transcript = build_transcript(
        st.session_state[msg_key], config["character_name"], config["scene_label"]
    )
    st.download_button(
        label="📄 Download Conversation Transcript",
        data=transcript,
        file_name=f"{config['char_key']}_conversation.txt",
        mime="text/plain",
    )
