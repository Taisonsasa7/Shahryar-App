import streamlit as st
from shahryar_core import shahryar_system

st.title("🌙 شهريار")

# اختبار بسيط لاستيراد النظام
rooms = shahryar_system.get_all_rooms()
st.write("تم استيراد النظام بنجاح!")
st.write(rooms)
