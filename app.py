import streamlit as st

# إعداد الصفحة لتناسب تصميم التطبيق الداكن
st.set_page_config(page_title="شهريار", layout="centered")

# إضافة نمط CSS مخصص ليعطي نفس شكل الألوان والبطاقات في "1000142843.jpg"
st.markdown("""
    <style>
    .stApp { background-color: #0e0e0e; color: white; }
    .room-card { 
        background-color: #1a1a1a; 
        border-radius: 15px; 
        padding: 15px; 
        margin-bottom: 15px; 
        border: 1px solid #333;
    }
    </style>
""", unsafe_allow_html=True)

# العنوان العلوي
st.title("شهريار")

# شريط التصنيفات العلوي
tabs = st.tabs(["🔥 الكل", "💬 دردشة", "🎮 ألعاب", "🎵 موسيقى"])

# محتوى تجريبي يشبه توزيع البطاقات في "1000142843.jpg"
col1, col2 = st.columns(2)

rooms = [
    {"name": "أليكس", "title": "سهرة ألعاب", "views": 234, "likes": 89},
    {"name": "صوفيا", "title": "موسيقى لايف", "views": 567, "likes": 312},
    {"name": "كريم", "title": "دردشة عامة", "views": 123, "likes": 45},
    {"name": "دي جي ماكس", "title": "راب سيشن", "views": 456, "likes": 234},
]

for i, room in enumerate(rooms):
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"""
        <div class="room-card">
            <h4 style="margin:0;">{room['name']}</h4>
            <p style="font-size: 0.8em; color: #aaa;">{room['title']}</p>
            <p style="font-size: 0.8em;">👁️ {room['views']} | ❤️ {room['likes']}</p>
        </div>
        """, unsafe_allow_html=True)

# زر الإضافة العائم (في الأسفل)
st.markdown("""
    <div style="position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%);">
        <button style="background-color: #d63384; border-radius: 50%; width: 60px; height: 60px; border: none; color: white; font-size: 30px;">+</button>
    </div>
""", unsafe_allow_html=Tru
