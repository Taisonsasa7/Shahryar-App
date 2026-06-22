import streamlit as st
import sys
import os

# إضافة المجلد الحالي للمسار لضمان أن بايثون يرى الملفات
sys.path.append(os.getcwd())

try:
    from shahryar_core import shahryar_system
    st.title("🌙 شهريار")
    
    # عرض الغرف
    rooms = shahryar_system.get_all_rooms()
    for room in rooms:
        st.write(f"### غرفة: {room['name']}")
        
    st.divider()
    st.subheader("حساب الأرباح")
    amount = st.number_input("أدخل المبلغ بالدولار", min_value=0.0)
    if st.button("حساب التوزيع"):
        result = shahryar_system.trigger_event(amount)
        st.json(result)

except Exception as e:
    st.error(f"حدث خطأ أثناء تحميل نظام شهريار: {e}")
