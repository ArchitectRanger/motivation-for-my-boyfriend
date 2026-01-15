import streamlit as st
import streamlit.components.v1 as components
from datetime import date
import os
import time
import random
import base64

# 1. Page Configuration
st.set_page_config(page_title="For Him ❤️", layout="centered")

# 2. Image Encoder
def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

script_directory = os.path.dirname(__file__)
photo_path = os.path.join(script_directory, "US.JPG")
img_base64 = get_base64(photo_path)

# 3. CSS: The "Nuclear Option" for Highlights and Pacifico Font
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');

    /* 1. FORCE FONT & BACKGROUND ON EVERYTHING */
    html, body, [data-testid="stAppViewContainer"], .stApp {{
        background-color: #DCD0FF !important; 
        font-family: 'Pacifico', cursive !important;
        overflow: hidden !important; 
        height: 100vh;
    }}

    /* 2. THE CARD - NO CHOPPING */
    div[data-testid="stVerticalBlock"] {{
        background: rgba(255, 255, 255, 0.98);
        padding: 20px 25px;
        border-radius: 25px;
        max-width: 480px;
        margin: auto;
        text-align: center;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.05);
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    /* 3. THE "NO HIGHLIGHT" RULE - Removing all Streamlit internal backgrounds */
    [data-testid="stMarkdownContainer"], 
    .stMarkdown, 
    .element-container, 
    div[stMarkdown] {{
        background-color: transparent !important;
        background: none !important;
        border: none !important;
    }}

    h1, p, span, div, label {{
        font-family: 'Pacifico', cursive !important;
        color: #4B0082 !important;
        background: transparent !important;
        background-color: transparent !important;
        text-decoration: none !important;
        user-select: none;
    }}

    /* 4. PHOTO CENTERING */
    .centered-photo {{
        max-height: 180px; 
        width: auto;
        border-radius: 20px;
        margin: 10px auto;
        display: block;
    }}

    /* 5. GREY BUTTONS */
    div.stButton > button {{
        background-color: #E0E0E0 !important;
        color: #4B0082 !important;
        font-family: 'Pacifico', cursive !important;
        border-radius: 20px !important;
        border: 1px solid #CCC !important;
        width: 100%;
        font-size: 18px !important;
        transition: 0.3s;
    }}

    /* 6. FLOATING EMOJI ANIMATION - EVERYWHERE */
    @keyframes floatUpRandom {{
        0% {{ transform: translateY(110vh) rotate(0deg); opacity: 0; }}
        10% {{ opacity: 1; }}
        90% {{ opacity: 1; }}
        100% {{ transform: translateY(-20vh) rotate(360deg); opacity: 0; }}
    }}

    .medical-emoji {{
        position: fixed;
        bottom: -100px;
        font-size: 4rem;
        z-index: 999999;
        pointer-events: none;
        animation: floatUpRandom 8s linear forwards;
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. App Logic
if 'first_load' not in st.session_state: st.session_state.first_load = True
if 'music' not in st.session_state: st.session_state.music = False
if 'burst_id' not in st.session_state: st.session_state.burst_id = 0

# Content
st.markdown("<h1 style='margin:0;'>Hey Love 💕</h1>", unsafe_allow_html=True)

if img_base64:
    st.markdown(f'<img src="data:image/jpeg;base64,{img_base64}" class="centered-photo">', unsafe_allow_html=True)

# Countdown
target = max(0, (date.today().year - 2025) * 12 + (date.today().month - 3))
placeholder = st.empty()

if st.session_state.first_load:
    for i in range(target + 1):
        placeholder.markdown(f'<p style="font-size: 22px; margin:0;">We\'ve been us for {i} month{"s" if i != 1 else ""} 💗</p>', unsafe_allow_html=True)
        time.sleep(0.3)
    st.session_state.first_load = False
else:
    placeholder.markdown(f'<p style="font-size: 22px; margin:0;">We\'ve been us for {target} month{"s" if target != 1 else ""} 💗</p>', unsafe_allow_html=True)

st.markdown('<p style="font-size: 16px; margin: 5px 0;">We met in March 2025, and you became my favorite person.</p>', unsafe_allow_html=True)

# 5. Compact Music
if not st.session_state.music:
    if st.button("Play our song? 🎵"):
        st.session_state.music = True
        st.rerun()
else:
    spotify_embed = """
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/249fRCHoYWdcWK4p1SSEhJ?utm_source=generator&theme=0" 
    width="100%" height="152" frameBorder="0" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    """
    components.html(spotify_embed, height=160)

# 6. Emojis Burst
if st.button("Click for a surprise 🥰... and again for another"):
    st.session_state.burst_id += 1 

if st.session_state.burst_id > 0:
    medical_emojis = ["🩺", "💊", "🧪", "💉", "🏥", "🧬", "🩹"]
    emoji_html = f"" 
    for _ in range(40):
        left_pos = random.randint(0, 100) 
        delay = random.uniform(0, 2)
        emoji = random.choice(medical_emojis)
        emoji_html += f'<div class="medical-emoji" style="left: {left_pos}%; animation-delay: {delay}s;">{emoji}</div>'
    
    st.markdown(emoji_html, unsafe_allow_html=True)
    st.markdown('<p style="font-size: 14px; margin:0;">Save lives today or I\'ll commit that crime on you 😉</p>', unsafe_allow_html=True)