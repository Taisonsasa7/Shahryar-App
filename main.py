import streamlit as st

# تهيئة الغرفة
if 'room_type' not in st.session_state:
    st.session_state.room_type = "🎙️ غرفة صوتية" # الوضع الافتراضي
if 'mics' not in st.session_state:
    st.session_state.mics = [None] * 25

st.title("🌙 منصة شهريار العالمية")

# 1. لوحة المالك (تغيير نوع الغرفة)
with st.sidebar:
    st.header("⚙️ لوحة تحكم المالك")
    new_type = st.radio("اختر وضع الغرفة:", ["🎙️ غرفة صوتية", "📺 بث مباشر", "🎮 غرف ألعاب"])
    if st.button("تحديث وضع الغرفة"):
        st.session_state.room_type = new_type
        st.rerun()

# 2. عرض نوع الغرفة الحالي
st.info(f"الوضع الحالي للغرفة: *{st.session_state.room_type}*")

# 3. عرض المايكات (يظهر في الغرفة الصوتية فقط)
if st.session_state.room_type == "🎙️ غرفة صوتية":
    st.subheader("🎤 منصة المتحدثين")
    cols = st.columns(5)
    for i in range(25):
        with cols[i % 5]:
            if st.session_state.mics[i] is None:
                if st.button(f"🎤 {i+1}", key=f"join_{i}"):
                    st.session_state.mics[i] = "عضو"
                    st.rerun()
            else:
                st.success(f"🎙️ {st.session_state.mics[i]}")
                if st.button("إنزال", key=f"kick_{i}"):
                    st.session_state.mics[i] = None
                    st.rerun()

# 4. عرض محتوى البث أو الألعاب (بناءً على الاختيار)
elif st.session_state.room_type == "📺 بث مباشر":
    st.write("📺 جارٍ تحميل البث المباشر...")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # رابط تجريبي

elif st.session_state.room_type == "🎮 غرف ألعاب":
    st.write("🎮 منطقة الألعاب: رابط اللعبة أو التحدي سيظهر هنا.")
    st.button("بدء تحدي جديد")
