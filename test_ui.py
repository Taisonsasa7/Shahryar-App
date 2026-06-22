import streamlit as st
from shahryar_core import shahryar_system

st.title("لوحة اختبار نظام شهريار")

# 1. اختبار المحرك المالي
st.subheader("التحقق من توزيع الأرباح (60/10/30)")
amount = st.number_input("أدخل المبلغ بالدولار:", value=100)
if st.button("احسب التوزيع"):
    results = shahryar_system.calculate_payout(amount)
    st.write("النتيجة المركزية:", results)

# 2. اختبار محاكي المفاوضات
st.subheader("محاكي المفاوضات السياسية")
tension = st.slider("مستوى التوتر:", 1, 10, 7)
if st.button("ابدأ المفاوضات"):
    status = shahryar_system.simulate_negotiation("Trump", "Iran", tension)
    st.success(f"النتيجة: {status}")
