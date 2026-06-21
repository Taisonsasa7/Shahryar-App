import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="شهريار", layout="wide")

# تصميم CSS للبطاقات والخلفية
st.markdown("""
    <style>
    .stApp { background-color: #121016; color: white; }
    .room-card { 
        background-color: #1E1A23; 
        border-radius: 20px; 
        padding: 15px; 
        margin: 10px; 
        color: white;
        border: 1px solid #333;
    }
    .room-img { width: 100%; height: 150px; object-fit: cover; border-radius: 15px; margin-bottom: 10px; }
    .live-badge { background-color: #FF4B4B; padding: 2px 8px; border-radius: 5px; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# بيانات الغرف (يمكنك استبدال الروابط بصور من جهازك لاحقاً)
rooms_data = [
    {"name": "Alex", "title": "Soirée gaming", "viewers": 234, "likes": 89, "img": "https://img.freepik.com/free-vector/gaming-background-with-neon-lights_23-2148906660.jpg"},
    {"name": "Sofia", "title": "Session musique", "viewers": 567, "likes": 312, "img": "https://img.freepik.com/free-photo/headphones-near-musical-instruments_23-2148154371.jpg"},
    {"name": "Karim", "title": "نقاش مفتوح", "viewers": 123, "likes": 45, "img": "https://img.freepik.com/free-photo/group-people-sitting-together-talking_23-2149176435.jpg"},
    {"name": "Luna", "title": "تحدي رقص", "viewers": 890, "likes": 456, "img": "https://img.freepik.com/free-photo/young-woman-dancing-hip-hop_23-2148163013.jpg"},
]

st.title("🌙 لوحة تحكم شهريار")

# عرض الغرف في شبكة (عمودين)
cols = st.columns(2)
for i, room in enumerate(rooms_data):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="room-card">
            <img src="{room['img']}" class="room-img">
            <span class="live-badge">LIVE</span> 👁️ {room['viewers']} ❤️ {room['likes']}
            <h3>{room['name']}</h3>
            <p>{room['title']}</p>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"دخول {room['name']}", key=f"btn_{i}")
