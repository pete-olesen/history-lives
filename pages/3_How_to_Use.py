import streamlit as st

st.set_page_config(
    page_title="How to Use This — History Lives",
    page_icon="🗺️",
    layout="centered"
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Special+Elite&family=IM+Fell+English:ital@0;1&display=swap');
  html, body, [class*="css"] { font-family: 'IM Fell English', serif; }
  h1, h2, h3 { font-family: 'Special Elite', monospace; }
  .tip-box {
      background: #f5f0e8;
      border-left: 3px solid #8b7355;
      padding: 0.8rem 1rem;
      border-radius: 4px;
      margin: 0.8rem 0;
      font-size: 0.95rem;
  }
</style>
""", unsafe_allow_html=True)

st.title("🗺️ How to Use History Lives")

st.markdown("""
Welcome. This page walks you through everything you need to know to get
started. The whole experience is designed to be simple — but a few things
are worth knowing before your first conversation.

---

### Step 1 — Enter your access code

When you click on any character in the left sidebar, you'll see a login
screen asking for an access code. Enter the code you were given and
click **Enter**.

If you don't have a code, email **livinghistorypete@gmail.com** to request one.
""")

st.markdown("""
<div class="tip-box">
💡 <strong>Tip:</strong> Your access code gives you a set number of messages
across all characters combined. Use them thoughtfully — have a real
conversation rather than testing with one-word questions.
</div>
""", unsafe_allow_html=True)

st.markdown("""
---

### Step 2 — Read the briefing

At the top of each character page is a short briefing that sets the scene —
who this person is, where they are, and what moment in history you're
entering. Read it before you start. It makes the conversation richer.

---

### Step 3 — Ask a question

Type your question in the box at the bottom of the page and press Enter.
The character will respond in a few seconds.
""")

st.markdown("""
<div class="tip-box">
💡 <strong>The pause is normal.</strong> After you ask a question, there is
a 3-5 second pause before the response appears. The AI is generating a
thoughtful, in-character answer. This is not a bug — think of it as the
character taking a moment to consider what you've asked.
</div>
""", unsafe_allow_html=True)

st.markdown("""
---

### Step 4 — Listen to the voice

After the text response appears, an audio player will load below it.
**Scroll down** to see it — it appears beneath the text, not above it.

Click the **Play button** if the audio doesn't start automatically.
Some browsers restrict autoplay, so you may always need to click play manually.
""")

st.markdown("""
<div class="tip-box">
💡 <strong>About the voices:</strong> The voices are AI-generated
approximations — not real recordings of Churchill, Eisenhower, or anyone
else. They are directionally right (Churchill sounds British and deliberate,
Eisenhower sounds American and plain-spoken) but they are not perfect
replicas. For a prototype, they are enough to add presence to the
conversation. A more polished version would have more authentic voices.
</div>
""", unsafe_allow_html=True)

st.markdown("""
---

### Step 5 — Keep the conversation going

These characters are built for real conversation, not one-question answers.
Ask follow-up questions. Push back. Ask something personal. Ask something
they might not want to answer.

The suggested questions in the left sidebar are a starting point —
but your own questions will often produce the most interesting responses.

Some things worth trying:

- Ask about something they regret
- Ask what they're afraid of
- Ask about someone they love
- Ask what they think happens next
- Ask something they probably don't want to answer

---

### Step 6 — Download your transcript

At the bottom of every character page is a **Download Conversation Transcript**
button. Click it to save a text file of your full conversation.

This is useful for classroom discussion, reflection assignments, or just
keeping a record of what was said.

---

### Step 7 — Try another character

Each character offers a completely different perspective on the same period
of history. A conversation with Eisenhower and then with Rommel — the same
night, two sides of the same decision — is a very different experience than
either one alone.

**Suggested starting points:**

- **New to the project?** Start with **Judy** — she's the most immediately
  relatable and requires no prior historical knowledge to connect with.
- **Want the military perspective?** Try **Eisenhower** followed by **Rommel**
  — the contrast is extraordinary.
- **Want the civilian experience?** **Marianne**, **Miguel**, and **Aleksei**
  each offer something no commander can.

---

### If the site looks like it's asleep

If you visit and see a sleeping emoji with the message "This app has gone
to sleep due to inactivity" — just click the **Wake it up** button and
wait about 30 seconds. This happens when the site hasn't been visited
for a while. Everything will be working normally once it wakes up.

---

### Questions or feedback

If something isn't working, or you have thoughts on what could be better,
email **livinghistorypete@gmail.com** or use the feedback survey linked
in the sidebar.

Honest reactions — including what doesn't work — are exactly what this
project needs right now.
""")
