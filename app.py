import streamlit as st
from supabase import create_client

st.title("لوحة تحكم السوبر أدمن 🌙")

# إعداد الاتصال باستخدام الأسرار
try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase = create_client(url, key)

    # جلب وعرض البيانات
    response = supabase.table("roomsr").select("*").execute()
    st.table(response.data)

except Exception as e:
    st.error(f"حدث خطأ: {e}")
    st.write("تأكد أن مفاتيح Supabase موجودة في إعدادات Secrets.")
