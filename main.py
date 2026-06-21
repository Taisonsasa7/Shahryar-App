import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="شهريار", layout="wide")

# هنا نستخدم العلامات الثلاثية """ لفتح وقفل نص الـ CSS
st.markdown("""
    <style>
    .stApp { 
        background-color: #121016; 
        color: white; 
    }
    .room-card { 
        background-color: #1E1A23; 
        border-radius: 20px; 
        padding: 20px; 
        margin: 10px; 
        color: white;
        border: 1px solid #333;
    }
    .live-badge { 
        background-color: #FF4B4B; 
        padding: 2px 8px; 
        border-radius: 5px; 
        font-size: 12px; 
    }
    </style>
    """, unsafe_allow_html=True)

# بيانات الغرف
rooms_data = [
    {"name": "Alex", "title": "Soirée gaming", "viewers": 234, "likes": 89},
    {"name": "Sofia", "title": "Session musique", "viewers": 567, "likes": 312},
    {"name": "Karim", "title": "نقاش مفتوح", "viewers": 123, "likes": 45},
    {"name": "Luna", "title": "تحدي رقص", "viewers": 890, "likes": 456},
]

st.title("🌙 شهريار")

# عرض الغرف
cols = st.columns(2)
for i, room in enumerate(rooms_data):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="room-card">
            <span class="live-badge">LIVE</span> 👁️ {room['viewers']} ❤️ {room['likes']}
            <h3>{room['name']}</h3>
            <p>{room['title']}</p>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"دخول {room['name']}", key=f"btn_{i}")
