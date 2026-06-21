import streamlit as st

# التأكد من وجود اسم الغرفة
room_name = st.session_state.get("current_room", "غرفة غير معروفة")

st.title(f"🎤 أنت الآن داخل: {room_name}")

# محاكاة واجهة الغرفة
st.markdown("### أدوات التحكم")
col1, col2 = st.columns(2)

with col1:
    st.button("🔊 فتح الصوت")
with col2:
    st.button("🔇 كتم الصوت")

st.write("---")
st.write("👥 *المتواجدون:* 5 أشخاص")

# زر العودة
if st.button("الخروج للرئيسية"):
    st.switch_page("main.py")
