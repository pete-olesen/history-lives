import streamlit as st

st.set_page_config(
    page_title="History Lives",
    page_icon="📖",
    layout="centered"
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Special+Elite&family=IM+Fell+English:ital@0;1&display=swap');
  html, body, [class*="css"] { font-family: 'IM Fell English', serif; }
  .main-title {
      font-family: 'Special Elite', monospace;
      font-size: 2.2rem;
      text-align: center;
      margin-bottom: 0.2rem;
  }
  .subtitle {
      text-align: center;
      font-style: italic;
      color: #6a6a6a;
      margin-bottom: 2rem;
  }
  .character-card {
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 1rem 1.2rem;
      margin-bottom: 0.8rem;
      background: #fafaf7;
  }
  .character-card h4 {
      margin: 0 0 0.3rem 0;
      font-family: 'Special Elite', monospace;
  }
  .character-card p {
      margin: 0;
      font-size: 0.92rem;
      color: #444;
  }
  .scene-tag {
      font-size: 0.8rem;
      color: #888;
      font-style: italic;
  }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📖 History Lives</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Conversations with the people who lived it</div>',
    unsafe_allow_html=True
)

st.markdown("""
### What is this?

History Lives lets students have real conversations with people who lived
through pivotal moments of World War Two — generals and farmers, prime
ministers and teenagers, on every side of the conflict.

Each character is grounded in historical research and speaks from a single,
specific moment in time. They don't know how the war ends. They don't know
what happens next. They only know what they know, right now, in the moment
you're talking to them.

The goal isn't to memorize dates or battles. It's **historical empathy** —
understanding that history was made by real people, all of whom believed they
were right, most of whom were afraid, none of whom knew how the story would end.

As one of the people involved in building this likes to say: *the victors
write the history.* This project is an attempt to make room for some of the
other voices too.

---

### How to use this

1. **Enter your access code** on any character page (provided separately)
2. **Pick a character** from the menu on the left
3. **Read the briefing** at the top of each page — it sets the scene
4. **Ask anything** — type your own questions, or use the suggested ones
   in the sidebar to get started
5. **Download the transcript** at the bottom of the conversation if you want
   to save or share it

Each character has a limited, realistic understanding of the world — ask
them something from outside their moment in history and watch how they
respond. That's part of the experience too.

---

### A note on what this is (and isn't)

These are AI-generated interpretations of historical figures and composite
characters, built on careful research — not recordings, not verified quotes,
and not a substitute for primary sources. Think of it as a starting point for
curiosity, discussion, and further research, not an ending point.

Each conversation is independent — characters don't remember previous
sessions, and conversations are designed to reach natural conclusions rather
than continue indefinitely.

---

### The characters

""", unsafe_allow_html=False)

characters = [
    ("⭐", "General Eisenhower", "Southwick House, England — June 5, 1944, 2200 hours",
     "The night before D-Day. The order has been given. 175,000 men cross the Channel at dawn."),
    ("🌾", "Field Marshal Rommel", "Herrlingen, Germany — June 6, 1944, dawn",
     "700 miles from Normandy, on his wife's birthday, when the call comes."),
    ("🇬🇧", "Prime Minister Churchill", "Southwick House, England — June 5, 1944, 2300 hours",
     "He wanted to sail with the invasion fleet. The King talked him out of it."),
    ("🌹", "Marianne", "Paris, occupied France — June 7, 1944",
     "A resistance courier, two days after the landings, with twenty minutes before she has to move."),
    ("⭐", "Judy", "Wichita, Kansas — Summer 1944",
     "Fifteen years old. Two brothers overseas. A mailbox she checks every morning."),
    ("🌺", "Miguel", "Manila, Philippines — February 1945",
     "Caught between two armies as the city he loves is destroyed in its own liberation."),
    ("🌾", "Aleksei", "A village near Poltava, Ukraine — October 1941",
     "A farmer with an unlit torch, ordered to burn everything he has ever known."),
]

for emoji, name, scene, hook in characters:
    st.markdown(f"""
    <div class="character-card">
        <h4>{emoji} {name}</h4>
        <p class="scene-tag">{scene}</p>
        <p>{hook}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
---

### For educators

If you're piloting this in a classroom, see the **Persona Guide** page in the
menu for character-by-character notes on themes, suggested discussion
questions, and curriculum connections.

There's a short feedback survey linked in the sidebar of every character page.
Your honest reaction — including what doesn't work — is exactly what this
project needs.

---

### About this project

Hi — I'm Pete O. I have no background in education, and I had no experience
writing code before I built this. I have a regular day job, completely
unrelated to either of those things.

I came to this project by watching where AI and graphics technology were
heading and thinking: this combination -- AI-driven conversation with
historical figures, grounded in real research -- seemed like something
genuinely useful that I hadn't seen done before. So I tried to build it.

**Everything you're seeing is AI-generated.** The conversations are powered
by AI trained on historical research. The voices are AI-generated
approximations -- not real recordings of Churchill or Eisenhower. They're
a starting point for curiosity, not a finished performance or a substitute
for primary sources.

**This is a prototype, and I'm looking for honest feedback -- not
encouragement.** The question I'm trying to answer is whether this is
worth building further, by me or by people with more expertise in education
and software than I have.

If it is worth building, here is where it could go next:

- **Photorealistic avatars** for each character -- using tools like Unreal
  Engine, each person rendered as a lifelike human face
- **VR headsets** -- imagine sitting across from Eisenhower the night before
  D-Day, in the room with him, rather than reading text on a screen
- **A mobile app** for independent or out-of-classroom use

I would genuinely value your thoughts on all of it -- the conversations as
they stand, the voices, and whether the avatar/VR/mobile direction seems
worth pursuing for your students.

Email me directly: **livinghistorypete@gmail.com**

-- Pete O

---

*History Lives is a prototype under active development.
Built with the belief that understanding where someone else stood
is the beginning of understanding anything else about them.*
""")
