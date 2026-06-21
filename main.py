import streamlit as st

st.set_page_config(page_title="شهريار", layout="wide")

# تصميم الخلفية والبطاقات
st.markdown("""
    <style>
    .stApp { background-color: #121016; color: white; }
    .room-card { background-color: #1E1A23; border-radius: 20px; padding: 20px; margin: 10px; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌙 شهريار")

rooms_data = [
    {"name": "غرفة الألعاب", "id": "gaming"},
    {"name": "غرفة الموسيقى", "id": "music"},
]

cols = st.columns(2)
for i, room in enumerate(rooms_data):
    with cols[i % 2]:
        st.markdown(f'<div class="room-card"><h3>{room["name"]}</h3>', unsafe_allow_html=True)
        if st.button(f"دخول {room['name']}", key=room['id']):
            st.session_state.current_room = room['name']
            st.switch_page("pages/room.py")
        st.markdown('</div>', unsafe_allow_html=True)
