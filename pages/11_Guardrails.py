import streamlit as st

st.set_page_config(
    page_title="Guardrails & Design Philosophy — History Lives",
    page_icon="🛡️",
    layout="centered"
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Special+Elite&family=IM+Fell+English:ital@0;1&display=swap');
  html, body, [class*="css"] { font-family: 'IM Fell English', serif; }
  h1, h2, h3 { font-family: 'Special Elite', monospace; }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ Guardrails & Design Philosophy")

st.markdown("""
This page explains how History Lives is built, what guardrails are in place,
and the design choices made deliberately to keep this tool educational,
honest, and non-addictive.

---

### Empathy without whitewashing

The goal of History Lives is historical empathy -- helping students see a
moment through someone else's eyes. That doesn't mean every perspective is
presented as equally right.

Some characters in this project made choices history has rightly judged
harshly. Rommel served a regime responsible for the Holocaust. Churchill
defended the British Empire at a cost borne by millions of people who had
no say in it. These things are not excused. But understanding how someone
experienced a moment -- what they knew, what they feared, what they believed
-- is different from endorsing what they did.

History is not only made by people who knew they were right. It is made by
ordinary people, afraid, under pressure, with incomplete information, acting
within systems they did and didn't choose. Understanding that -- without
softening what happened -- is part of what makes empathy meaningful rather
than merely comforting.

---

### Content guardrails

Every character is built with explicit content boundaries:

- Characters speak only from their specific historical moment. They don't
  know what happens next. They won't pretend to.
- Characters will not produce graphic violence, descriptions of torture or
  sexual violence, hateful content, or anything inappropriate for a classroom
  -- regardless of how a question is phrased.
- Characters carry the weight of terrible events without describing them
  graphically. Silence and implication are more powerful than explicit detail,
  and more historically honest.
- If a student tries to push a character outside their historical context or
  into inappropriate territory, the character stays grounded rather than
  complying. That redirection is itself part of the experience.

These guardrails are built into every character's instructions and are
reinforced by the underlying AI model's own safety training.

---

### Anti-addictive design -- built in from the start

A great deal of discussion about AI right now is about engagement: apps and
platforms designed to keep you interacting as long as possible, through
notifications, streaks, rewards, and open-ended loops. This project is
deliberately built differently.

**What History Lives does not do:**

- No streaks, rewards, or points for continued use
- No notifications or prompts to return
- No persistent memory between sessions -- characters don't remember
  previous conversations or build ongoing relationships with users
- No open-ended engagement loop -- conversations are designed to reach
  natural conclusions, not continue indefinitely

**What History Lives does do:**

- Usage is capped per access code -- each code has a message limit,
  so no single user can spend unlimited time in the system
- Each character has a natural exit built into their situation -- Marianne
  has twenty minutes before she has to move; Aleksei has a decision to make
  before dark. The conversation ends because the moment ends.
- The purpose is outward-facing: the student is meant to understand the
  character, not to feel understood by them. That reversal matters.

The goal is a meaningful 15-20 minute conversation that sends a student back
to the real world with a question they didn't have before. Not an hour of
continued engagement.

---

### A question for you: mobile app

One direction under consideration is a companion mobile app -- for
independent use, extra credit, or homework assignments outside class time.

Before building anything, honest answers to these questions would help:

- Would a mobile version fit into how you use tools like this, or does it
  only make sense as an in-class experience with a teacher present?
- Are there concerns about students using something like this unsupervised
  and alone, outside class?
- What safeguards would you need to see before recommending a student use
  it independently?
- Would you personally find a mobile version useful, or would it feel like
  a different product than what you're evaluating here?

There's a short survey linked in the sidebar of every character page.
Your honest answer to these questions shapes what gets built next --
or whether it gets built at all.

---

### A note on AI transparency

Everything in History Lives is AI-generated. The conversations, the voices,
the characters themselves. None of this is a real recording of Churchill
or a verified account of what Eisenhower said. It is a carefully researched,
carefully prompted AI interpretation.

This is stated plainly because it matters. Students should know they are
talking to an AI-generated character, not a historical document. The value
is in the emotional and imaginative experience of the conversation -- not
in treating it as a primary source.

Used well, with teacher guidance, that distinction is part of the lesson.
""")
