import streamlit as st
from supabase import create_client

st.title("لوحة تحكم السوبر أدمن 🌙")

try:
    # قراءة الإعدادات من الـ Secrets
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]

    # الاتصال بقاعدة البيانات
    supabase = create_client(url, key)

    # جلب البيانات
    response = supabase.table("roomsr").select("*").execute()
    st.table(response.data)

except Exception as e:
    st.error(f"خطأ: {e}")
