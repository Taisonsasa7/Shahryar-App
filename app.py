 import streamlit as st
from supabase import create_client

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shahryar-App", layout="centered")

# 2. جلب الإعدادات من Secrets (التي قمت بحفظها الآن)
try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    
    # إنشاء الاتصال
    supabase = create_client(url, key)
    
    st.title("لوحة تحكم السوبر أدمن 🌙")
    st.write("✅ تم الاتصال بقاعدة البيانات بنجاح!")
    
    # 3. عرض البيانات
    st.subheader("إدارة الغرف")
    # تأكد من أن اسم الجدول في Supabase هو 'roomsr'
    response = supabase.table("roomsr").select("*").execute()
    
    if response.data:
        st.table(response.data)
    else:
        st.info("الجدول 'roomsr' فارغ حالياً.")

except Exception as e:
    st.error(f"❌ حدث خطأ في الاتصال: {e}")
    st.write("تأكد أن أسماء المفاتيح في الـ Secrets مطابقة تماماً (SUPABASE_URL و SUPABASE_KEY).")

