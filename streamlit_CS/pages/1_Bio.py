import streamlit as st

st.title("👋 My Bio")

# ---------- TODO: Replace with your own info ----------
NAME = "Martin Jimenez"
PROGRAM = "Computer Science / Martial Arts Enthusiast"
INTRO = (
    "Hello, I am Martin Jimenez. I am a first-generation Hispanic college student "
    "pursuing a degree in Computer Science. Outside of academics, I have a passion for martial arts, "
    "which has taught me discipline and perseverance."
    "I look forward to finishing my degree and take advantage of the opportunities my parents have given me."
)
FUN_FACTS = [
    "I love training jiu jitsu amd muay thai.",
    "I’m very excited to graduate in May",
    "My team and I for our senior project are building a really unique app that I can't wait to share.",
]
PHOTO_PATH = "assets/BO_NIX.jpg"  # Put a file in repo root or set a URL

# ---------- Layout ----------
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    try:
        st.image(PHOTO_PATH, caption=NAME, use_container_width=True)
    except Exception:
        st.info("Add a photo named `your_photo.jpg` to the repo root, or change PHOTO_PATH.")
with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun facts")
for i, f in enumerate(FUN_FACTS, start=1):
    st.write(f"- {f}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")
