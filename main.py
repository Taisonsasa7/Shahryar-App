import streamlit as st
from supabase import create_client

# 1. أولاً: تعريف الاتصال (هنا يتم إنشاء المتغير supabase)
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

st.title("لوحة تحكم السوبر أدمن 🌙")

# 2. ثانياً: استخدام المتغير supabase لجلب البيانات
try:
    response = supabase.table("roomsr").select("*").execute()
    st.table(response.data)
except Exception as e:
    st.error(f"خطأ في الاتصال: {e}")
