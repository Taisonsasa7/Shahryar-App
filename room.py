import streamlit as st

st.set_page_config(page_title="داخل الغرفة", layout="wide")

# نفس تصميم الخلفية
st.markdown("""
    <style>
    .stApp { background-color: #121016; color: white; }
    .room-container { background-color: #1E1A23; padding: 30px; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

room_name = st.session_state.get("current_room", "الغرفة")
st.title(f"🎤 {room_name}")

st.markdown('<div class="room-container">', unsafe_allow_html=True)
st.write("### أدوات التحكم")
col1, col2 = st.columns(2)
with col1: st.button("🔊 فتح الصوت")
with col2: st.button("🔇 كتم الصوت")
st.markdown('</div>', unsafe_allow_html=True)

if st.button("الخروج للرئيسية"):
    st.switch_page("main.py")
