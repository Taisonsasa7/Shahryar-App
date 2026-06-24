import streamlit as st
from supabase import create_client

# إعدادات الصفحة
st.set_page_config(page_title="Shahryar-App", layout="centered")

# قراءة البيانات من الأسرار (Secrets) التي وضعتها في Streamlit
try:
    URL = st.secrets["SUPABASE_URL"]
    KEY = st.secrets["SUPABASE_KEY"]
    
    # إنشاء الاتصال
    supabase = create_client(URL, KEY)
    
    st.title("لوحة تحكم السوبر أدمن 🌙")
    
    # جلب وعرض البيانات
    st.subheader("إدارة الغرف")
    response = supabase.table("roomsr").select("*").execute()
    
    if response.data:
        st.table(response.data)
    else:
        st.write("الجدول فارغ أو لا توجد بيانات.")

except Exception as e:
    st.error(f"خطأ في الاتصال: {e}")
    st.write("تأكد أن أسماء الأسرار في Streamlit تطابق SUPABASE_URL و SUPABASE_KEY.")
