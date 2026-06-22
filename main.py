import streamlit as st
from shahryar_core import shahryar_system

st.title("🌙 شهريار")

# هنا نحاول استدعاء الغرف
try:
    rooms = shahryar_system.get_all_rooms()
    for room in rooms:
        st.write(f"### {room['name']}")
except Exception as e:
    st.error(f"حدث خطأ في عرض الغرف: {e}")
