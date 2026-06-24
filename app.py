import streamlit as st
from supabase import create_client

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shahryar-App", layout="centered")

# 2. بيانات الاتصال (تم وضع مفاتيحك هنا)
URL = "https://dpyavcpuhsrwozgayfxx.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRweWF2Y3B1aHNyd296Z2F5Znh4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTY4ODg3NzMsImV4cCI6MjAzMjQ2NDc3M30.e1-7Y96m1x2q5n_uLd5hN"

# 3. إنشاء الاتصال
try:
    supabase = create_client(URL, KEY)
except Exception as e:
    st.error(f"خطأ في الاتصال: {e}")

st.title("لوحة تحكم السوبر أدمن 🌙")

# 4. جلب وعرض بيانات الغرف
st.subheader("إدارة الغرف")
try:
    rooms_data = supabase.table("roomsr").select("*").execute()
    if rooms_data.data:
        st.table(rooms_data.data)
    else:
        st.write("لا توجد بيانات غرف.")
except Exception as e:
    st.error(f"خطأ في جلب الغرف: {e}")

# 5. جلب وعرض بيانات الوكالات
st.divider()
st.subheader("وكالات المنصة")
try:
    agencies_data = supabase.table("agencies").select("*").execute()
    if agencies_data.data:
        st.table(agencies_data.data)
    else:
        st.write("لا توجد بيانات وكالات.")
except Exception as e:
    st.error(f"خطأ في جلب الوكالات: {e}")
