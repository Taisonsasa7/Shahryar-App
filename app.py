 import streamlit as st
from supabase import create_client

# 1. إعداد الصفحة
st.set_page_config(page_title="Shahryar-App", layout="centered")

# 2. إعدادات الاتصال بـ Supabase (ضع بياناتك هنا)
url = "ضع_رابط_Supabase_هنا"
key = "ضع_مفتاح_API_هنا"
supabase = create_client(url, key)

st.title("لوحة تحكم السوبر أدمن")

# 3. جلب وعرض بيانات الغرف (من جدول roomsr)
st.subheader("إدارة الغرف")
try:
    response_rooms = supabase.table("roomsr").select("*").execute()
    if response_rooms.data:
        st.table(response_rooms.data)
    else:
        st.write("لا توجد غرف.")
except Exception as e:
    st.error(f"خطأ في الغرف: {e}")

# 4. جلب وعرض بيانات الوكالات (من جدول agencies في Supabase)
st.divider()
st.subheader("وكالات المنصة (من Supabase)")
try:
    response_agencies = supabase.table("agencies").select("*").execute()
    if response_agencies.data:
        st.table(response_agencies.data)
    else:
        st.write("لا توجد وكالات مسجلة.")
except Exception as e:
    st.error(f"خطأ في الوكالات: {e}")

