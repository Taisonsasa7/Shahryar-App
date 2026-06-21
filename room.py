import streamlit as st

st.set_page_config(page_title="غرفة شهريار", layout="centered")

# تصميم صفحة الغرفة
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .admin-panel { border: 1px solid #FFD700; padding: 15px; border-radius: 10px; background: #1E1A23; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎤 غرفة الدردشة الحية")

# محاكاة حالة الصوت
if 'audio_status' not in st.session_state:
    st.session_state.audio_status = "صامت"

# أدوات التحكم
col1, col2 = st.columns(2)
with col1:
    if st.button("🔊 فتح/كتم الصوت"):
        st.session_state.audio_status = "مسموع" if st.session_state.audio_status == "صامت" else "صامت"
st.write(f"الحالة الحالية: *{st.session_state.audio_status}*")

# لوحة تحكم الأدمن (تظهر فقط إذا كنت الأدمن)
with st.sidebar:
    st.markdown('<div class="admin-panel"><h3>⚙️ تحكم الأدمن</h3></div>', unsafe_allow_html=True)
    admin_password = st.text_input("كلمة مرور الأدمن", type="password")
    if admin_password == "123456":
        st.success("أنت الآن تتحكم في الغرفة")
        st.button("طرد مستخدم")
        st.button("إغلاق الغرفة")
    else:
        st.warning("أدخل كلمة المرور للتحكم")

# قائمة المتواجدين (محاكاة)
st.write("---")
st.subheader("👥 المتواجدون الآن")
st.write("👤 مستخدم 1")
st.write("👤 مستخدم 2")
