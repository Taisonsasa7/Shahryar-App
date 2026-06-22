import streamlit as st
from shahryar_core import shahryar_system

st.title("🌙 شهريار")

# عرض الغرف
try:
    rooms = shahryar_system.get_all_rooms()
    for room in rooms:
        st.write(f"### {room['name']}")
except AttributeError:
    st.error("خطأ: النظام لا يجد قائمة الغرف. تأكد من تحديث ملف shahryar_core.py")

st.divider()

# حساب الأرباح
amount = st.number_input("أدخل المبلغ بالدولار", min_value=0.0)
if st.button("حساب التوزيع"):
    result = shahryar_system.trigger_event(amount)
    st.json(result)
