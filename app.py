 import streamlit as st
from supabase import create_client

# 1. إعدادات الصفحة
st.set_page_config(page_title="Shahryar-App", layout="centered")

# 2. بيانات الاتصال (تم وضع مفتاحك هنا)
URL = "https://dpyavcpuhsrwozgayfxx.supabase.co"
KEY = "sb_pub_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRweWF2Y3B1aHNyd296Z2F5Znh4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTY4ODg3NzMsImV4cCI6MjAzMjQ2NDc3M30.e1-7Y96m1x2q5n_uLd5hN"

# 3. إنشاء الاتصال
try:
    supabase = create_client(URL, KEY)
    st.title("لوحة تحكم السوبر أدمن 🌙")
    
    # 4. جلب وعرض البيانات
    st.subheader("إدارة الغرف")
    # ملاحظة: تأكد أن اسم الجدول في قاعدة بياناتك هو 'roomsr'
    response = supabase.table("roomsr").select("*").execute()
    
    if response.data:
        st.table(response.data)
    else:
        st.write("الجدول فارغ أو لا توجد بيانات.")

except Exception as e:
    st.error(f"خطأ في الاتصال بقاعدة البيانات: {e}")

