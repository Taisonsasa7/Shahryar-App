import streamlit as st
from shahryar_core import shahryar_system

st.title("🌙 شهريار")

# عرض الغرف باستخدام الدالة الصحيحة
rooms = shahryar_system.get_all_rooms()
for room in rooms:
    st.write(f"### {room['name']}")

st.divider()
amount = st.number_input("أدخل المبلغ بالدولار", min_value=0)
if st.button("حساب الأرباح"):
    results = shahryar_system.calculate_money(amount)
    st.write(results)
