iimport streamlit as st

st.set_page_config(page_title="منصة شهريار", layout="wide")

# تهيئة بيانات الغرفة
if 'room_mode' not in st.session_state:
    st.session_state.room_mode = "🎙️ غرفة صوتية"
if 'mics' not in st.session_state:
    st.session_state.mics = {i: {"user": None, "cam_on": False} for i in range(25)}

st.title("🌙 منصة شهريار العالمية")

# قائمة اختيار نوع الغرفة
mode = st.sidebar.selectbox("اختر نوع الغرفة:", ["🎙️ غرفة صوتية", "📺 بث مباشر", "🎮 غرف ألعاب"])
st.session_state.room_mode = mode

st.header(f"الوضع الحالي: {st.session_state.room_mode}")

# 1. حالة الغرفة الصوتية
if st.session_state.room_mode == "🎙️ غرفة صوتية":
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
                if st.button("إنزال المايك", key=f"kick_{i}"):
                    st.session_state.mics[i] = {"user": None, "cam_on": False}
                    st.rerun()

# 2. حالة البث المباشر
elif st.session_state.room_mode == "📺 بث مباشر":
    st.write("📺 شاشة البث المباشر ستظهر هنا...")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# 3. حالة غرف الألعاب
elif st.session_state.room_mode == "🎮 غرف ألعاب":
    st.write("🎮 منطقة الألعاب: قائمة الألعاب المتاحة:")
    games = ["لعبة الدومينو", "لعبة الطاولة", "لعبة الورق"]
    for game in games:
        if st.button(f"بدء {game}"):
            st.write(f"جاري تشغيل {game}...")
