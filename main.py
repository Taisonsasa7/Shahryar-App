import streamlit as st
from shahryar_core import shahryar_system

st.title("🌙 شهريار")

# عرض الغرف
try:
    rooms = shahryar_system.get_all_rooms()
    for room in rooms:
        st.write(f"### {room['name']}")
except Exception as e:
    st.error(f"خطأ في عرض الغرف: {e}")

st.divider()

# حساب الأرباح
amount = st.number_input("أدخل المبلغ بالدولار", min_value=0)
if st.button("حساب الأرباح"):
    try:
        results = shahryar_system.calculate_money(amount)
        st.write(results)
    except Exception as e:
        st.error(f"خطأ في الحساب: {e}")
