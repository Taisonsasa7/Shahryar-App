
import streamlit as st

# إعدادات الواجهة
st.set_page_config(page_title="منصة شهريار", layout="wide")
st.markdown("""<style>.stApp { background-color: #0e0e10; color: white; }</style>""", unsafe_allow_html=True)

# 1. تهيئة البيانات الثابتة
if 'room_name' not in st.session_state: st.session_state.room_name = "🌙 منصة شهريار العالمية"
if 'admins' not in st.session_state: st.session_state.admins = ["Admin1", "Admin2"]
if 'mode' not in st.session_state: st.session_state.mode = "🎙️ غرفة صوتية"

# 2. وظيفة الهوية البصرية
def get_user_badge(username):
    if username == "Shahryar": return "👑", "#FFD700"
    if username in st.session_state.admins: return "🛡️", "#00FF00"
    return "👤", "#FFFFFF"

# 3. لوحة الإدارة (Sidebar)
with st.sidebar:
    st.header("⚙️ لوحة الإدارة")
    st.session_state.room_name = st.text_input("تغيير اسم الغرفة:", value=st.session_state.room_name)
    st.session_state.mode = st.selectbox("نوع الغرفة:", ["🎙️ غرفة صوتية", "📺 بث مباشر", "🎮 غرف ألعاب"])
    st.divider()
    new_admin = st.text_input("إضافة أدمن:")
    if st.button("حفظ الأدمن"): st.session_state.admins.append(new_admin)

# 4. محتوى المنصة
st.title(f"{st.session_state.room_name}")

if st.session_state.mode == "🎙️ غرفة صوتية":
    st.subheader("🎤 منصة التحدي (25 مايك)")
    cols = st.columns(5)
    for i in range(25):
        with cols[i % 5]:
            st.markdown(f"*مايك {i+1}*")
            # أزرار تحكم للأدمنية
            col1, col2 = st.columns(2)
            col1.button("🚫", key=f"k_{i}", help="طرد")
            col2.button("🔇", key=f"m_{i}", help="كتم")

elif st.session_state.mode == "📺 بث مباشر":
    st.subheader("📺 البث الحي")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # هنا يوضع رابط البث
    st.text_input("تغيير رابط يوتيوب:")

elif st.session_state.mode == "🎮 غرف ألعاب":
    st.subheader("🎮 منطقة التحديات")
    st.button("تحدي الدومينو")
    st.button("تحدي الأسئلة")
