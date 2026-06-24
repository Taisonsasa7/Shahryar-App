import streamlit as st
from supabase import create_client

# إعدادات الصفحة
st.title("لوحة تحكم السوبر أدمن 🌙")

try:
    # الربط مع Supabase باستخدام الأسرار
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase = create_client(url, key)

    # جلب وعرض البيانات
    response = supabase.table("roomsr").select("*").execute()
    st.table(response.data)

except Exception as e:
    st.error(f"خطأ في الاتصال: {e}")
