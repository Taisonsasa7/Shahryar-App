import streamlit as st
from supabase import create_client

# إعدادات الصفحة
st.set_page_config(page_title="Shahryar-App", layout="centered")

st.title("لوحة تحكم السوبر أدمن 🌙")

try:
    # جلب الإعدادات من الأسرار
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    
    # محاولة الاتصال
    supabase = create_client(url, key)
    st.write("✅ تم الاتصال بقاعدة البيانات.")
    
    # محاولة جلب بيانات
    response = supabase.table("roomsr").select("*").execute()
    st.table(response.data)

except KeyError as e:
    st.error(f"❌ خطأ: لم يتم العثور على المفتاح {e} في إعدادات Secrets.")
except Exception as e:
    st.error(f"❌ حدث خطأ غير متوقع: {e
