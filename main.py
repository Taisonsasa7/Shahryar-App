import streamlit as st

# إعدادات الواجهة الداكنة والاحترافية
st.set_page_config(page_title="منصة شهريار", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0e0e10; color: white; }
    .room-card { background: linear-gradient(145deg, #1c1c21, #121215); border-radius: 20px; padding: 20px; border: 1px solid #333; }
    .challenge-box { border: 2px solid #ff4b4b; padding: 15px; border-radius: 15px; background: #1a1a1a; }
    </style>
    """, unsafe_allow_html=True)

# تهيئة البيانات
if 'room_mode' not in st.session_state: st.session_state.room_mode = "🎙️ غرفة صوتية"
if 'challenge' not in st.session_state: st.session_state.challenge = {"active": False, "score_a": 0, "score_b": 0}
if 'mics' not in st.session_state: st.session_state.mics = {i: {"user": None} for i in range(25)}

st.title("🌙 منصة شهريار العالمية")

# التحكم في الغرفة (Sidebar)
mode = st.sidebar.selectbox("اختر نوع الغرفة:", ["🎙️ غرفة صوتية", "📺 بث مباشر", "🎮 غرف ألعاب"])
st.session_state.room_mode = mode

# حالة التحدي (تظهر في الغرفة الصوتية فقط)
if st.session_state.room_mode == "🎙️ غرفة صوتية":
    # 1. لوحة التحدي (يتحكم بها المالك/الأدمن)
    with st.expander("🔥 ساحة التحديات"):
        if st.button("بدء/إعادة التحدي"): st.session_state.challenge = {"active": True, "score_a": 0, "score_b": 0}
        if st.session_state.challenge["active"]:
            c1, c2 = st.columns(2)
            if c1.button("نقطة للفريق (أ)"): st.session_state.challenge["score_a"] += 1
            if c2.button("نقطة للفريق (ب)"): st.session_state.challenge["score_b"] += 1
            st.metric("النتيجة", f"{st.session_state.challenge['score_a']} - {st.session_state.challenge['score_b']}")

    # 2. منصة الـ 25 مايك
    st.subheader("🎤 منصة المتحدثين")
    cols = st.columns(5)
    for i in range(25):
        with cols[i % 5]:
            if st.session_state.mics[i]["user"] is None:
                if st.button(f"🎤 {i+1} (متاح)", key=f"j_{i}"):
                    st.session_state.mics[i]["user"] = "عضو"
                    st.rerun()
            else:
                st.success(f"🎙️ {st.session_state.mics[i]['user']}")
                if st.button("إنزال", key=f"k_{i}"):
                    st.session_state.mics[i]["user"] = None
                    st.rerun()

elif st.session_state.room_mode == "📺 بث مباشر":
    st.markdown('<div class="room-card"><h3>📺 البث المباشر</h3><p>محتوى البث سيظهر هنا</p></div>', unsafe_allow_html=True)
elif st.session_state.room_mode == "🎮 غرف ألعاب":
    st.markdown('<div class="room-card"><h3>🎮 غرف الألعاب</h3><p>اختر اللعبة للبدء</p></div>', unsafe_allow_html=True)
