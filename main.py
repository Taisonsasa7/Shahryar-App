import streamlit as st

# إعدادات المظهر العام
st.set_page_config(page_title="منصة شهريار", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0e0e10; color: white; }
    .room-card { background: linear-gradient(145deg, #1c1c21, #121215); border-radius: 20px; padding: 20px; border: 1px solid #333; text-align: center; }
    .live-badge { background-color: #ff4b4b; color: white; padding: 2px 8px; border-radius: 5px; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# تهيئة بيانات الجلسة
if 'room_mode' not in st.session_state: st.session_state.room_mode = "🎙️ غرفة صوتية"
if 'mics' not in st.session_state: st.session_state.mics = {i: {"user": None, "cam_on": False} for i in range(25)}

st.title("🌙 منصة شهريار العالمية")

# التحكم بالوضع (للمالك)
mode = st.sidebar.selectbox("اختر نوع الغرفة:", ["🎙️ غرفة صوتية", "📺 بث مباشر", "🎮 غرف ألعاب"])
st.session_state.room_mode = mode

# عرض المحتوى حسب الوضع
if st.session_state.room_mode == "🎙️ غرفة صوتية":
    st.subheader("🎤 منصة المتحدثين (25 مايك)")
    cols = st.columns(5)
    for i in range(25):
        with cols[i % 5]:
            mic = st.session_state.mics[i]
            if mic["user"] is None:
                if st.button(f"🎤 {i+1} (متاح)", key=f"join_{i}"):
                    st.session_state.mics[i]["user"] = "عضو"
                    st.rerun()
            else:
                st.success(f"🎙️ {mic['user']}")
                if st.button("🎥 كاميرا" if not mic["cam_on"] else "🛑 إيقاف", key=f"cam_{i}"):
                    st.session_state.mics[i]["cam_on"] = not mic["cam_on"]
                    st.rerun()
                if st.button("إنزال المايك", key=f"kick_{i}"):
                    st.session_state.mics[i] = {"user": None, "cam_on": False}
                    st.rerun()

elif st.session_state.room_mode == "📺 بث مباشر":
    st.markdown('<div class="room-card"><h3>📺 منطقة البث المباشر</h3><p>لا يوجد بث نشط حالياً</p></div>', unsafe_allow_html=True)

elif st.session_state.room_mode == "🎮 غرف ألعاب":
    st.markdown('<div class="room-card"><h3>🎮 منطقة الألعاب</h3><p>اختر لعبة للبدء مع أصدقائك</p></div>', unsafe_allow_html=True)

# لوحة تحكم المالك (مخفية في الأسفل)
with st.expander("👑 لوحة تحكم المالك"):
    st.write("إضافة الأدمنية وتعديل إعدادات الغرفة هنا...")
    st.write("إضافة الأدمنية وتعديل إعدادات الغرفة هنا...")
