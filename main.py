import streamlit as st
import streamlit.components.v1 as components

st.title("🎙️ غرفة شهريار (صوت وصورة)")

# تهيئة المايكات مع حالة الكاميرا
if 'mics' not in st.session_state:
    st.session_state.mics = {i: {"user": None, "cam_on": False} for i in range(25)}

st.subheader("🎤 منصة المتحدثين (صوت + فيديو)")
cols = st.columns(5)

for i in range(25):
    with cols[i % 5]:
        mic = st.session_state.mics[i]
        
        # إذا كان المايك فارغاً
        if mic["user"] is None:
            if st.button(f"🎤 {i+1} (متاح)", key=f"join_{i}"):
                st.session_state.mics[i]["user"] = "عضو"
                st.rerun()
        else:
            # إذا كان المايك مشغولاً، نظهر خيار الكاميرا
            st.success(f"🎙️ {mic['user']}")
            
            # زر تشغيل/إيقاف الكاميرا
            cam_label = "📸 إيقاف الكاميرا" if mic["cam_on"] else "🎥 فتح الكاميرا"
            if st.button(cam_label, key=f"cam_{i}"):
                st.session_state.mics[i]["cam_on"] = not mic["cam_on"]
                st.rerun()
            
            # إذا كانت الكاميرا مفتوحة، نظهر إطار الفيديو
            if mic["cam_on"]:
                st.warning("⚠️ إطار الكاميرا نشط (فيديو)")
                
            if st.button("إنزال", key=f"kick_{i}"):
                st.session_state.mics[i] = {"user": None, "cam_on": False}
                st.rerun()
