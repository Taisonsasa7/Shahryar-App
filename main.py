import streamlit as st

st.set_page_config(page_title="غرفة شهريار", layout="wide")

# 1. إعادة تهيئة البيانات بشكل آمن لمنع الأخطاء
if 'mics' not in st.session_state or not isinstance(st.session_state.mics, dict):
    st.session_state.mics = {i: {"user": None, "cam_on": False} for i in range(25)}

st.title("🎙️ غرفة شهريار (صوت وصورة)")

# 2. منطقة عرض المايكات
st.subheader("🎤 منصة المتحدثين")
cols = st.columns(5)

for i in range(25):
    with cols[i % 5]:
        # نصل للبيانات من الـ session_state
        mic = st.session_state.mics[i]
        
        if mic["user"] is None:
            if st.button(f"🎤 {i+1} (متاح)", key=f"join_{i}"):
                st.session_state.mics[i]["user"] = "عضو"
                st.rerun()
        else:
            st.success(f"🎙️ {mic['user']}")
            
            # زر الكاميرا
            cam_label = "📸 إيقاف الكاميرا" if mic["cam_on"] else "🎥 فتح الكاميرا"
            if st.button(cam_label, key=f"cam_{i}"):
                st.session_state.mics[i]["cam_on"] = not mic["cam_on"]
                st.rerun()
                
            if st.button("إنزال", key=f"kick_{i}"):
                st.session_state.mics[i] = {"user": None, "cam_on": False}
                st.rerun()

# 3. زر لتصفير الغرفة بالكامل في حال حدوث أي خطأ مستقبلاً
if st.sidebar.button("🔄 إعادة ضبط الغرفة"):
    st.session_state.mics = {i: {"user": None, "cam_on": False} for i in range(25)}
    st.rerun()
