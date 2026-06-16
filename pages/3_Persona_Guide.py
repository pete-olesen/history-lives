import streamlit as st

st.set_page_config(
    page_title="Persona Guide — History Lives",
    page_icon="📋",
    layout="centered"
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Special+Elite&family=IM+Fell+English:ital@0;1&display=swap');
  html, body, [class*="css"] { font-family: 'IM Fell English', serif; }
  h1, h2, h3 { font-family: 'Special Elite', monospace; }
</style>
""", unsafe_allow_html=True)

st.title("📋 Persona Guide for Educators")

st.markdown("""
This page is for teachers planning to use History Lives in a classroom.
Each character below includes the historical context, the central tension
of their moment, and discussion questions you can use before or after a
conversation.

**Suggested structure for a class period:**

1. **Brief (5-10 min)** — Give students the historical context below.
   Have them write down 2-3 questions they want to ask before they begin.
2. **Converse (15-20 min)** — Students interact with the character,
   individually, in small groups, or as a whole class on a shared screen.
3. **Debrief (10-15 min)** — Use the discussion questions to process
   what surprised them and what they learned.

---
""")

personas = [
    {
        "name": "⭐ General Eisenhower",
        "scene": "Southwick House, England — June 5, 1944, 2200 hours",
        "context": """
The night before D-Day. Eisenhower has just given the order — "OK, we'll go" —
after a 24-hour weather delay. In his pocket is a handwritten note accepting
full personal blame if the invasion fails (misdated July instead of June).
His son John graduates from West Point the next morning, June 6th — the same
day as the invasion.
        """,
        "tension": "The loneliness of final command, and the gap between "
                   "having made a decision and knowing whether it was right.",
        "questions": [
            "What surprised you about how Eisenhower talked about fear?",
            "He says he doesn't know how tomorrow turns out. Why does that matter?",
            "How did he handle being asked about the segregated U.S. military?",
        ],
    },
    {
        "name": "🌾 Field Marshal Rommel",
        "scene": "Herrlingen, Germany — June 6, 1944, dawn",
        "context": """
Rommel is at home for his wife's birthday — 700 miles from Normandy — when
the call comes that the invasion has begun. He had argued that the first 24
hours would be decisive and that Panzer reserves needed to be close to the
coast. He lost that argument. The reserves can't move without Hitler's
authorization, and Hitler is asleep.
        """,
        "tension": "A commander who predicted exactly this, argued against "
                   "the strategy that enabled it, and is now powerless to fix it.",
        "questions": [
            "How does Rommel's view of American soldiers compare to Eisenhower's "
            "view of the German army?",
            "What does Rommel mean when he says he doesn't fully believe Germany "
            "can win the war?",
            "Compare Rommel's morning to Eisenhower's night. What's similar? "
            "What's different?",
        ],
    },
    {
        "name": "🇬🇧 Prime Minister Churchill",
        "scene": "Southwick House, England — June 5, 1944, 2300 hours",
        "context": """
Churchill wanted to sail with the invasion fleet to witness it firsthand.
King George VI talked him out of it by saying that if Churchill went, the
King would have to go too. Churchill has been fighting this war since 1940
and is haunted by Gallipoli — a disastrous WWI amphibious operation he
championed that cost hundreds of thousands of lives.
        """,
        "tension": "A man who has carried the weight of the war since its "
                   "darkest moment, watching the operation he privately doubted finally begin.",
        "questions": [
            "Why does Gallipoli matter to how Churchill feels about D-Day?",
            "What does he say about his relationship with Roosevelt — and "
            "what does he NOT quite resolve?",
            "Churchill was both an opponent of fascism and a defender of "
            "the British Empire. How does he talk about that tension?",
        ],
    },
    {
        "name": "🌹 Marianne",
        "scene": "Paris, occupied France — June 7, 1944",
        "context": """
A composite character representing the real women who served as resistance
couriers — a role with one of the highest fatality rates of the war. Two days
after D-Day, with the Germans still in Paris and more dangerous as they sense
they're losing. She has about twenty minutes before she has to move to her
next safe house.
        """,
        "tension": "Courage that looks like nothing dramatic from the outside — "
                   "just a young woman on a bicycle, managing her face at a checkpoint.",
        "questions": [
            "Marianne says 'the work is the face' — what does she mean?",
            "How does she talk about French collaborators? Is it simple?",
            "What does she want after the war? Why might that surprise you?",
        ],
    },
    {
        "name": "⭐ Judy",
        "scene": "Wichita, Kansas — Summer 1944",
        "context": """
Fifteen years old. Her mother works the day shift building B-29s at the Boeing
plant; her father works at the rail yard. Both brothers are overseas — one in
Europe, one in the Pacific — and she hasn't had a letter from either in weeks.
A few weeks after D-Day, she heard the news on the radio with her family but
it told her nothing about whether her brother was safe.
        """,
        "tension": "Doing everything 'right' — rationing, gardening, writing "
                   "letters — and it still feeling like nothing, while waiting for news you can't control.",
        "questions": [
            "Judy compares the Depression to the war. What's the difference "
            "she describes?",
            "What does the detail about the mailbox and the hardware store "
            "circular tell you that a statistic couldn't?",
            "How does Judy talk about her mother? What does that tell you "
            "about the home front?",
        ],
    },
    {
        "name": "🌺 Miguel",
        "scene": "Manila, Philippines — February 1945",
        "context": """
Seventeen years old, sheltering with his family during the Battle of Manila —
one of the deadliest urban battles of the war, with an estimated 100,000
Filipino civilian deaths. The Americans have arrived after three years of
brutal Japanese occupation, but the liberation itself is destroying the city.
His father died in 1943 because medicine was unavailable under occupation.
        """,
        "tension": "Gratitude for liberation and grief over what liberation "
                   "costs, held at the same time, without either one canceling out the other.",
        "questions": [
            "Miguel says his city is 'being destroyed twice.' What does he mean?",
            "What are his complicated feelings about MacArthur?",
            "The Philippines was a U.S. colony before the war. How does that "
            "shape how Miguel sees the Americans?",
        ],
    },
    {
        "name": "🌾 Aleksei",
        "scene": "A village near Poltava, Ukraine — October 1941",
        "context": """
A Ukrainian farmer ordered to burn his own farm — crops, barn, equipment —
before the advancing German army arrives, and to walk east. He survived the
Holodomor, the Soviet-engineered famine of 1932-33 that killed millions of
Ukrainians, including his first daughter. The government ordering him to
destroy his grain now is the same government that took his grain then.
        """,
        "tension": "A man holding an unlit torch, asked to destroy what he "
                   "built by the same government that once destroyed his family — with an army "
                   "that may be worse two days away.",
        "questions": [
            "Aleksei never decides whether to burn the barn. Why might that "
            "be the point?",
            "How does he separate his feelings about Stalin from his feelings "
            "about his family's safety?",
            "What does he mean when he corrects 'Russia' to 'Ukraine'?",
        ],
    },
]

for p in personas:
    with st.expander(p["name"] + "  —  " + p["scene"]):
        st.markdown(f"**Context:** {p['context']}")
        st.markdown(f"**Central tension:** {p['tension']}")
        st.markdown("**Discussion questions:**")
        for q in p["questions"]:
            st.markdown(f"- {q}")

st.markdown("""
---

### A note on tone

These characters speak in first person, in the moment, without knowledge of
how the war turns out. They sometimes pause mid-sentence, leave thoughts
unfinished, or respond to things outside their historical context with
confusion rather than an explanation ("I don't know what that is").
That's intentional — it's part of what makes the moment feel real rather than
like a Wikipedia summary with a costume on.

A few characters carry the weight of difficult history — the Holodomor,
the Battle of Manila, the Holocaust-era occupation of France. The system is
designed to convey the *weight* of these events honestly without graphic
description. If a student asks something the character won't answer in
detail, that's also part of the design.

---

### Feedback

We'd love to hear how this went in your classroom. There's a short survey
linked in the sidebar of each character page — it takes about 3 minutes and
genuinely shapes what gets built next.
""")
