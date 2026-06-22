import streamlit as st
from shahryar_core import shahryar_system

st.set_page_config(page_title="شهريار", layout="wide")

st.title("🌙 شهريار")

# جلب الغرف من المحرك المركزي
rooms = shahryar_system.get_all_rooms()

# عرض الغرف بشكل شبكي
cols = st.columns(3)
for i, room in enumerate(rooms):
    with cols[i % 3]:
        st.subheader(room['name'])
        # هنا يمكنك إضافة مسار صورتك، مثلاً:
        # st.image(f"images/{room['id']}.jpg") 
        if st.button(f"دخول {room['name']}", key=room['id']):
            st.write(f"أنت الآن في {room['name']}")
