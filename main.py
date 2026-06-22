import streamlit as st
from shahryar_core import shahryar_system

st.set_page_config(page_title="شهريار", layout="wide")

st.title("🌙 شهريار")

# جلب الغرف
rooms = shahryar_system.get_all_rooms()

# عرض الغرف والصور
cols = st.columns(len(rooms))
for i, room in enumerate(rooms):
    with cols[i]:
        # عرض الصورة (يجب أن تكون الصور في مجلد باسم images)
        st.image(f"images/{room['id']}.jpg", use_container_width=True)
        
        # عرض زر الدخول
        if st.button(f"دخول {room['name']}", key=room['id']):
            st.success(f"جاري الدخول إلى {room['name']}...")
