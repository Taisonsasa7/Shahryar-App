import streamlit as st
import random
from supabase import create_client

# إعداد الاتصال
supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

# تهيئة الجلسة
if 'step' not in st.session_state: st.session_state['step'] = 'login'
if 'authenticated' not in st.session_state: st.session_state['authenticated'] = False

# 1. شاشة الدخول الأولى
if st.session_state['step'] == 'login':
    st.title("🔒 دخول الإدارة العليا")
    email = st.text_input("البريد الإلكتروني:")
    password = st.text_input("كلمة المرور:", type="password")
    if st.button("إرسال رمز التحقق"):
        # 👉 ضع إيميلك وباسوردك هنا للتحقق
        if email == "admin@shahryar.com" and password == "admin123":
            st.session_state['otp'] = str(random.randint(100000, 999999))
            st.info(f"تم إرسال الرمز (للأغراض التجريبية: {st.session_state['otp']})")
            st.session_state['step'] = 'verify'
            st.rerun()
        else:
            st.error("خطأ في البيانات!")

# 2. شاشة التحقق (الخطوة الثانية)
elif st.session_state['step'] == 'verify':
    st.title("🛡️ التحقق بخطوتين")
    user_otp = st.text_input("أدخل الرمز المكون من 6 أرقام:")
    if st.button("تأكيد الدخول"):
        if user_otp == st.session_state['otp']:
            st.session_state['authenticated'] = True
            st.session_state['step'] = 'dashboard'
            st.rerun()
        else:
            st.error("رمز غير صحيح!")

# 3. لوحة التحكم (التي تظهر لك فقط)
elif st.session_state['step'] == 'dashboard' and st.session_state['authenticated']:
    st.title("🌙 لوحة تحكم السوبر أدمن")
    if st.sidebar.button("خروج"):
        st.session_state['authenticated'] = False
        st.session_state['step'] = 'login'
        st.rerun()

    # عرض البيانات
    try:
        response = supabase.table("roomsr").select("*").execute()
        rooms = response.data
        cols = st.columns(3)
        for i, room in enumerate(rooms):
            with cols[i % 3]:
                st.markdown(f"*{room.get('room_name')}*")
                st.button("⚙️ إدارة", key=f"btn_{i}")
    except Exception as e:
        st.error("خطأ في جلب البيانات.")
