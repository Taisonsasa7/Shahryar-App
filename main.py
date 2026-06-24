import streamlit as st
from supabase import create_client

# إعدادات الصفحة
st.title("لوحة تحكم السوبر أدمن 🌙")

# جلب الأسرار والاتصال
try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase = create_client(url, key)

    # جلب البيانات
    response = supabase.table("roomsr").select("*").execute()
    
    # عرض البيانات
    st.table(response.data)

except Exception as e:
    st.error(f"خطأ: {e}")
