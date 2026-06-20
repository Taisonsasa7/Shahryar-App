import streamlit as st
from mining_engine import MiningEngine # سنربط ملفك هنا

st.title("تطبيق شهريار - لوحة التحكم")

# استخدام محركك المالي
engine = MiningEngine()

usd = st.number_input("أدخل المبلغ بالدولار:", min_value=0)
if st.button("احسب الماسات"):
    diamonds = engine.calculate_diamonds(usd)
    st.success(f"الرصيد المحول: {diamonds} ماسة")

st.write("---")
st.write("مرحباً بك في نظام شهريار الرقمي")
