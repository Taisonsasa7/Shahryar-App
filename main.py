import streamlit as st
from supabase import create_client

# إعداد الاتصال
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

st.title("لوحة تحكم السوبر أدمن 🌙")

# عرض البيانات
try:
    response = supabase.table("roomsr").select("*").execute()
    st.table(response.data)
except Exception as e:
    st.error(f"خطأ في عرض البيانات: {e}")
