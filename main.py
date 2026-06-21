import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="شهريار", layout="wide")

# تصميم الألوان والخلفية
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .room-card {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #FFD700;
        margin-bottom: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌙 لوحة تحكم شهريار")

# إنشاء الغرف بشكل مرئي
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="room-card"><h3>🎤 غرف الدردشة</h3><p>دردش مع الآخرين</p></div>', unsafe_allow_html=True)
    st.button("دخول الغرفة", key="chat")

with col2:
    st.markdown('<div class="room-card"><h3>🎥 البث المباشر</h3><p>شاهد البث الآن</p></div>', unsafe_allow_html=True)
    st.button("مشاهدة البث", key="live")

with col3:
    st.markdown('<div class="room-card"><h3>🎮 قسم الألعاب</h3><p>تحدى أصدقائك</p></div>', unsafe_allow_html=True)
    st.button("بدء اللعب", key="games")
