import streamlit as st

st.set_page_config(page_title="منصة شهريار", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0d0d0d; color: #ffffff; }
    .room-card { 
        background-color: #1a1a1a; 
        border: 2px solid #FFD700; 
        padding: 10px; 
        border-radius: 15px; 
        margin: 10px; 
        text-align: center; 
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌙 منصة شهريار العالمية")

def get_rooms(page=1):
    start = (page - 1) * 20 + 1
    end = start + 20
    return [{"id": i, "name": f"Room {i}", "image": "https://picsum.photos/300/200"} for i in range(start, end)]

page = st.number_input("Page Number", min_value=1, value=1)
rooms = get_rooms(page)

cols = st.columns(4)
for i, room in enumerate(rooms):
    with cols[i % 4]:
        st.markdown('<div class="room-card">', unsafe_allow_html=True)
        st.image(room["image"], use_container_width=True)
        st.subheader(room["name"])
        st.button("Enter", key=f"btn_{room['id']}")
        st.markdown('</div>', unsafe_allow_html=True)
