import streamlit as st

st.set_page_config(page_title="منصة شهريار", layout="wide")

# الرابط الافتراضي لصورة الشهريار (يجب استضافة الصورة ووضع رابطها هنا)
DEFAULT_IMAGE = "https://i.ibb.co/L0Yn4yB/1000142830.jpg" 

st.markdown("""
    <style>
    .stApp { background-color: #0d0d0d; color: #ffffff; }
    .room-card { 
        background-color: #1a1a1a; 
        border: 2px solid #FFD700; 
        padding: 15px; 
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
    # هنا ربطنا كل الغرف بصورة الشهريار الافتراضية
    return [{"id": i, "name": f"غرفة {i}", "image": DEFAULT_IMAGE} for i in range(start, end)]

page = st.number_input("رقم الصفحة", min_value=1, value=1)
rooms = get_rooms(page)

cols = st.columns(4)
for i, room in enumerate(rooms):
    with cols[i % 4]:
        st.markdown('<div class="room-card">', unsafe_allow_html=True)
        st.image(room["image"], use_container_width=True)
        st.subheader(room["name"])
        # هنا يمكنك لاحقاً إضافة نوع الغرفة (صوتية، ألعاب، بث)
        st.button("دخول الغرفة", key=f"btn_{room['id']}")
        st.markdown('</div>', unsafe_allow_html=True)
