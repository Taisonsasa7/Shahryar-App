import streamlit as st

# إعداد الصفحة لتكون واسعة وبخلفية داكنة
st.set_page_config(page_title="منصة شهريار", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e0e10; color: white; }
    .room-card {
        background: linear-gradient(145deg, #1c1c21, #121215);
        border-radius: 20px;
        padding: 20px;
        margin: 10px;
        border: 1px solid #333;
        text-align: center;
        transition: 0.3s;
    }
    .room-card:hover { border: 1px solid #ff4b4b; }
    .live-badge { background-color: #ff4b4b; color: white; padding: 2px 8px; border-radius: 5px; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌙 منصة شهريار")

# إنشاء بطاقات البث
cols = st.columns(3)
rooms = [("Alex", "Gaming Session", "234"), ("Sofia", "Music Live", "567"), ("Luna", "Dance Challenge", "890")]

for i, (name, title, viewers) in enumerate(rooms):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="room-card">
            <span class="live-badge">LIVE</span>
            <h3>{name}</h3>
            <p>{title}</p>
            <p>👁️ {viewers} مشاهدة</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"دخول {name}", key=f"btn_{i}"):
            st.session_state.current_room = name
            st.rerun()
