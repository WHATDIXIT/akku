import streamlit as st
import os
import random

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Happy Birthday My Baby 💖",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "assets", "images")
VIDEO_PATH = os.path.join(BASE_DIR, "assets", "video", "our_memory.mp4")
TOTAL_IMAGES = 14

CAPTIONS = [
    "That little dance we did in the snow... my heart still skips a beat for you. ❄️🥰",
    "Just us, wrapped up cozy together — my favorite kind of warmth. ❤️",
    "Colors of Holi all around us, but you're still the brightest color in my life. 🌸💕",
    "Holding your hand, lost in your eyes, even the snow couldn't compete with your smile. ❄️💞",
    "Sweet little moments with you are sweeter than any cake. 🍰😘",
    "Movie nights are my favorite — especially when you're cuddled right next to me. 🎬💑",
    "Late night drives, closer hearts, endless laughter. 🚗✨",
    "Just two souls, one love, and a whole lot of giggles. 🌙💖",
    "Every adventure feels better with you by my side. 🏙️💞",
    "My princess on her special day, looking absolutely gorgeous. 👑🐼",
    "Your smile is honestly my favorite thing in this entire world. ☕😍",
    "Happy Birthday to the sweetest 'Bitto' there ever was. 🎂🧁",
    "Your laugh is, hands down, the best sound I have ever heard. 😂💕",
    "Dancing through life with you, one cafe and one memory at a time. 💃❤️",
]

# ----------------------------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------------------------
if "stage" not in st.session_state:
    st.session_state.stage = "login"
if "img_idx" not in st.session_state:
    st.session_state.img_idx = 0
if "no_pos" not in st.session_state:
    st.session_state.no_pos = 0  # position index of the "No" button in the 3x3 grid

YES_POS = 4  # center cell of the 3x3 grid stays fixed for the "Yes" button


def go_to(stage: str):
    st.session_state.stage = stage
    st.rerun()


# ----------------------------------------------------------------------------
# GLOBAL STYLE (pink & red romantic theme)
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Poppins:wght@300;400;600&display=swap');

    .stApp {
        background: linear-gradient(135deg, #ffe6f0 0%, #ffd1dc 35%, #ffb6c1 65%, #ff8fab 100%);
        font-family: 'Poppins', sans-serif;
    }

    /* Hide default streamlit chrome a little */
    header[data-testid="stHeader"] { background: transparent; }

    .love-title {
        font-family: 'Dancing Script', cursive;
        font-size: 3.2rem;
        text-align: center;
        color: #d6336c;
        text-shadow: 2px 2px 8px rgba(255,255,255,0.6);
        margin-bottom: 0.2rem;
        animation: pulseHeart 1.8s ease-in-out infinite;
    }

    .love-subtitle {
        font-family: 'Poppins', sans-serif;
        text-align: center;
        font-size: 1.15rem;
        color: #8a2b4c;
        margin-bottom: 1.2rem;
    }

    .pointer-text {
        text-align: center;
        font-size: 1.05rem;
        color: #c2185b;
        font-weight: 600;
        margin-top: 1.5rem;
        animation: bounceArrow 1.4s infinite;
    }

    .caption-text {
        text-align: center;
        font-size: 1.15rem;
        color: #8a2b4c;
        font-family: 'Dancing Script', cursive;
        font-weight: 700;
        margin-top: 0.6rem;
        margin-bottom: 0.6rem;
    }

    .final-message {
        background: rgba(255,255,255,0.75);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 30px rgba(214,51,108,0.25);
        text-align: center;
        font-size: 1.25rem;
        line-height: 1.9;
        color: #7a1f3d;
        font-family: 'Poppins', sans-serif;
    }

    .final-title {
        font-family: 'Dancing Script', cursive;
        font-size: 2.8rem;
        text-align: center;
        color: #d6336c;
        margin-bottom: 0.5rem;
    }

    .question-title {
        font-family: 'Dancing Script', cursive;
        font-size: 2.6rem;
        text-align: center;
        color: #d6336c;
        margin-bottom: 1.5rem;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #ff5c8d, #ff8fab);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.6rem 1.4rem;
        font-weight: 600;
        font-size: 1rem;
        box-shadow: 0 4px 14px rgba(214,51,108,0.35);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 18px rgba(214,51,108,0.5);
        color: white;
    }

    @keyframes pulseHeart {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }

    @keyframes bounceArrow {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(10px); }
    }

    .floating-hearts {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        pointer-events: none;
        overflow: hidden;
        z-index: 0;
    }
    .floating-hearts span {
        position: absolute;
        bottom: -10%;
        font-size: 1.8rem;
        opacity: 0.55;
        animation: floatUp linear infinite;
    }
    @keyframes floatUp {
        0% { transform: translateY(0) rotate(0deg); opacity: 0.6; }
        100% { transform: translateY(-110vh) rotate(360deg); opacity: 0; }
    }
    </style>

    <div class="floating-hearts">
        <span style="left:5%; animation-duration: 9s;">💖</span>
        <span style="left:20%; animation-duration: 12s; animation-delay: 2s;">💕</span>
        <span style="left:40%; animation-duration: 10s; animation-delay: 1s;">❤️</span>
        <span style="left:60%; animation-duration: 14s; animation-delay: 3s;">💗</span>
        <span style="left:80%; animation-duration: 11s; animation-delay: 0.5s;">💞</span>
        <span style="left:90%; animation-duration: 13s; animation-delay: 2.5s;">💓</span>
        <span style="left:30%; animation-duration: 15s; animation-delay: 4s;">💘</span>
        <span style="left:70%; animation-duration: 10s; animation-delay: 1.5s;">💝</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# STAGE 1: LOGIN / WELCOME PAGE
# ----------------------------------------------------------------------------
if st.session_state.stage == "login":
    st.markdown("<div class='love-title'>Happy Birthday My Baby! 🎂💖</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='love-subtitle'>I made this little space just for you, full of our memories "
        "and a little surprise at the end... 🌹</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='pointer-text'>👇 Tap the <b>'Thank You'</b> button below to open your surprise 👇</div>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 1.4, 1])
    with col2:
        if st.button("Thank You 💌", use_container_width=True, key="thankyou_btn"):
            go_to("gallery")

# ----------------------------------------------------------------------------
# STAGE 2: PHOTO + VIDEO GALLERY
# ----------------------------------------------------------------------------
elif st.session_state.stage == "gallery":
    idx = st.session_state.img_idx

    if idx < TOTAL_IMAGES:
        st.markdown("<div class='love-title' style='font-size:2.2rem;'>Our Little Memories 📸</div>", unsafe_allow_html=True)

        img_path = os.path.join(IMAGES_DIR, f"img{idx + 1:02d}.jpg")
        st.image(img_path, use_container_width=True)
        st.markdown(f"<div class='caption-text'>{CAPTIONS[idx]}</div>", unsafe_allow_html=True)

        st.progress((idx + 1) / (TOTAL_IMAGES + 1))

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if idx > 0:
                if st.button("⬅ Previous", use_container_width=True):
                    st.session_state.img_idx -= 1
                    st.rerun()
        with col3:
            if st.button("Next ➡", use_container_width=True):
                st.session_state.img_idx += 1
                st.rerun()
    else:
        st.markdown("<div class='love-title' style='font-size:2.2rem;'>One Last Memory 🎥</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='caption-text'>A little video to remind you how much fun we have together. 💑</div>",
            unsafe_allow_html=True,
        )
        if os.path.exists(VIDEO_PATH):
            st.video(VIDEO_PATH)
        else:
            st.info("Video not found.")

        st.progress(1.0)

        col1, col2, col3 = st.columns([1, 1.4, 1])
        with col1:
            if st.button("⬅ Previous", use_container_width=True):
                st.session_state.img_idx -= 1
                st.rerun()
        with col2:
            if st.button("Continue 💕", use_container_width=True):
                go_to("question")

# ----------------------------------------------------------------------------
# STAGE 3: THE BIG QUESTION
# ----------------------------------------------------------------------------
elif st.session_state.stage == "question":
    st.markdown("<div class='question-title'>One last question, baby... 🥺</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='love-subtitle' style='font-size:1.6rem; font-weight:600;'>Do you love me? 💗</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div class='love-subtitle'>Try clicking 'No' if you dare... 😏</div>",
        unsafe_allow_html=True,
    )

    # 3x3 grid -> Yes stays fixed in the center, No jumps around
    for row in range(3):
        cols = st.columns(3)
        for col_idx in range(3):
            cell = row * 3 + col_idx
            with cols[col_idx]:
                if cell == YES_POS:
                    if st.button("Yes, I love you! 😍💖", key="yes_btn", use_container_width=True):
                        go_to("final")
                elif cell == st.session_state.no_pos:
                    if st.button("No 🙄", key="no_btn", use_container_width=True):
                        choices = [c for c in range(9) if c != YES_POS and c != st.session_state.no_pos]
                        st.session_state.no_pos = random.choice(choices)
                        st.rerun()
                else:
                    st.write("")

# ----------------------------------------------------------------------------
# STAGE 4: FINAL LOVE MESSAGE
# ----------------------------------------------------------------------------
elif st.session_state.stage == "final":
    st.balloons()
    st.markdown("<div class='final-title'>I knew it! 🥹💕</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="final-message">
        I love you so much, baby. You're so precious to me, and you're the best thing
        that has ever happened to my life. 💗<br><br>
        Every little moment with you feels like a beautiful dream I never want to wake
        up from — your smile lights up my darkest days, your laugh is my favorite
        melody, and your hugs are the safest place I know. 🌹<br><br>
        Happy Birthday, my love. Today and every single day after, I promise to
        cherish you, pamper you, and love you more and more. You are my heart, my
        home, and my forever. 🥰💍<br><br>
        Here's to many more birthdays, adventures, and memories together — I love you,
        my baby. Forever and always. ❤️
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        img_path = os.path.join(IMAGES_DIR, "img02.jpg")
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        if st.button("🔁 Watch our memories again", use_container_width=True):
            st.session_state.stage = "login"
            st.session_state.img_idx = 0
            st.session_state.no_pos = 0
            st.rerun()
