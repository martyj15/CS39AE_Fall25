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
PHOTO_PATH = "https://www.google.com/imgres?q=bo%20nix&imgurl=https%3A%2F%2Fs.yimg.com%2Fny%2Fapi%2Fres%2F1.2%2FtpbUlXPybWdfAZqcj03vkw--%2FYXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTQ5NDtjZj13ZWJw%2Fhttps%3A%2F%2Fwww.gannett-cdn.com%2Fauthoring%2Fimages%2Fsmg%2F2024%2F08%2F29%2FSMGW%2F74765926007-USATSI_23974296-e1723465828419.jpeg&imgrefurl=https%3A%2F%2Fsports.yahoo.com%2Fbo-nix-near-perfect-against-005748942.html&docid=V7UdSyVmuzjVoM&tbnid=iUjMr141AjEY4M&vet=12ahUKEwjPst6p87iQAxXoFjQIHeo8HgUQM3oECBoQAA..i&w=640&h=494&hcb=2&ved=2ahUKEwjPst6p87iQAxXoFjQIHeo8HgUQM3oECBoQAA"  # Put a file in repo root or set a URL

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
