import streamlit as st

st.set_page_config(
    page_title="About — History Lives",
    page_icon="📖",
    layout="centered"
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Special+Elite&family=IM+Fell+English:ital@0;1&display=swap');
  html, body, [class*="css"] { font-family: 'IM Fell English', serif; }
  h1, h2, h3 { font-family: 'Special Elite', monospace; }
</style>
""", unsafe_allow_html=True)

st.title("📖 About This Project")

st.markdown("""
### Who built this

My name is Pete O. I am not a developer, not an educator, and not an
entrepreneur. I have a regular day job that has nothing to do with any
of this. I built History Lives because I got curious about where AI
technology was heading and thought: this combination — AI-driven
conversation with historical figures, grounded in real research — seemed
like something genuinely useful that I hadn't seen done before.

So I tried to build it.

---

### Why World War Two

I have always been drawn to World War Two — not as a collection of battles
and dates, but as a moment when history compressed itself into a few years
and asked ordinary people to do extraordinary things.

I have stood on the beaches of Normandy. I have been inside Churchill's
underground bunker in London. I have walked through Dachau. I have visited
Pearl Harbor. These are not places you forget. Standing where things
actually happened changes how you understand them in a way that reading
about them never quite does.

World War Two brought out the very best and the very worst in humanity,
sometimes in the same person, sometimes on the same day. And what happened
*after* the war — how the victors treated the defeated, how the world was
rebuilt, what was learned and what was forgotten — may matter as much as
the war itself.

My mother once told me: *the victors write the history.* History
Lives is an attempt to make room for some of the other voices too — the
people on every side, in every theater, whose stories don't always make
it into the textbook version.

---

### Why this could go beyond World War Two

This project is focused on World War Two because that's where my interest
runs deepest. But the technology is not limited to any single period.
The same approach could work for the American Civil War, the French
Revolution, the Space Race, or any moment in history where human beings
made difficult choices under pressure.

World War Two is the starting point. It doesn't have to be the only one.

---

### A note on the voices

The voices you hear are AI-generated approximations. They are not real
recordings of Churchill, Eisenhower, or Rommel, and I did not attempt
to exactly replicate how those people actually sounded. Partly this is
for legal reasons — the rights around voice likeness are unsettled
territory — and partly because for a prototype at this stage, the
conversation matters more than the voice quality. The voices are
directionally right: Churchill sounds British and deliberate, Eisenhower
sounds American and plain-spoken. That is enough for now.

If this becomes worth building further, more authentic voice work
would be part of it.

---

### What I am asking for

This site exists to answer one question: **is this worth building?**

Not whether it is impressive. Not whether it is technically interesting.
Whether it is actually useful — to teachers, to students, to anyone trying
to understand history as something that happened to real people rather than
as a sequence of events to be memorized.

I would genuinely like to know:

- Did the conversations feel historically honest?
- Did they produce something in you — or in your students — that a
  textbook doesn't?
- Is there a version of this you would actually use in a classroom?
- And honestly: **would you pay for it?** If so, what would make it
  worth paying for?

That last question is the important one. Polite enthusiasm is easy to
come by. Actual intent is what I need to know.

---

### Where this could go

If it is worth building further, here is what the next version could look like:

- **Photorealistic avatars** — each character rendered as a lifelike
  human face using tools like Unreal Engine
- **VR headsets** — sitting across from Eisenhower the night before
  D-Day, in the room with him, rather than reading text on a screen
- **A mobile app** — for use outside the classroom, independently,
  at the student's own pace

I am genuinely asking whether any of that matters to you. There is a
short feedback survey here: **[History Lives Feedback Survey](https://forms.gle/Na4JCYTzWi5Yej727)**

Or email me directly: **livinghistorypete@gmail.com**

I read every message.

— Pete O
""")
