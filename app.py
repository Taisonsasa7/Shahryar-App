import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="شهريار", layout="centered")

# CSS الخاص بالتصميم الجذاب (نفس شكل LiveGuest)
st.markdown("""
    <style>
    .stApp { background-color: #0e0e0e; color: white; }
    .room-card { 
        background-color: #1a1a1a; border-radius: 15px; padding: 15px; 
        margin-bottom: 15px; border: 1px solid #333;
    }
    </style>
""", unsafe_allow_html=True)

# العنوان
st.title("شهريار")

# التصنيفات
st.tabs(["🔥 الكل", "💬 دردشة", "🎮 ألعاب", "🎵 موسيقى"])

# عرض الغرف (التصميم الذي أعجبك)
col1, col2 = st.columns(2)
rooms = [
    {"name": "أليكس", "title": "سهرة ألعاب"},
    {"name": "صوفيا", "title": "موسيقى لايف"},
    {"name": "كريم", "title": "دردشة عامة"},
    {"name": "دي جي ماكس", "title": "راب سيشن"},
]

for i, room in enumerate(rooms):
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"""
        <div class="room-card">
            <h4 style="margin:0;">{room['name']}</h4>
            <p style="font-size: 0.8em; color: #aaa;">{room['title']}</p>
        </div>
        """, unsafe_allow_html=True)
from data_store import DataStore

# تعريف القاعدة هنا (مرة واحدة فقط)
db = DataStore()
