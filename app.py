import streamlit as st
from supabase import create_client

# إعدادات الصفحة
st.set_page_config(page_title="Shahryar-App", layout="centered")

st.title("لوحة تحكم السوبر أدمن 🌙")

try:
    # جلب الإعدادات من الـ Secrets
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    
    # إنشاء الاتصال
    supabase = create_client(url, key)
    st.write("✅ تم الاتصال بقاعدة البيانات.")
    
    # جلب البيانات
    response = supabase.table("roomsr").select("*").execute()
    
    if response.data:
        st.table(response.data)
    else:
        st.write("الجدول فارغ حالياً.")

except Exception as e:
    st.error(f"حدث خطأ: {e}")
    st.write("تأكد أن SUPABASE_URL و SUPABASE_KEY معرفان في إعدادات التطبيق.")
