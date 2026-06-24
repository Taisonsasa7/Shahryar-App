import streamlit as st
import pyotp  # مكتبة جديدة للأمان
from supabase import create_client

# إعداد الاتصال
supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

# إعداد الـ TOTP (المصادقة)
totp = pyotp.TOTP(st.secrets["TOTP_SECRET"])

if 'step' not in st.session_state: st.session_state['step'] = 'login'
if 'authenticated' not in st.session_state: st.session_state['authenticated'] = False

# شاشة الدخول الأولى
if st.session_state['step'] == 'login':
    st.title("🔒 دخول الإدارة العليا")
    email = st.text_input("البريد الإلكتروني:")
    password = st.text_input("كلمة المرور:", type="password")
    if st.button("دخول"):
        if email == st.secrets["ADMIN_EMAIL"] and password == st.secrets["ADMIN_PASSWORD"]:
            st.session_state['step'] = 'verify_totp'
            st.rerun()

# شاشة التحقق من تطبيق Authenticator
elif st.session_state['step'] == 'verify_totp':
    st.title("🛡️ رمز المصادقة (Authenticator)")
    user_code = st.text_input("أدخل الكود المكون من 6 أرقام من التطبيق:")
    if st.button("تحقق"):
        if totp.verify(user_code):
            st.session_state['authenticated'] = True
            st.session_state['step'] = 'dashboard'
            st.rerun()
        else:
            st.error("كود غير صحيح!")

# لوحة التحكم
elif st.session_state['step'] == 'dashboard':
    st.title("🌙 لوحة تحكم السوبر أدمن")
    # ... (باقي كود عرض البيانات)
