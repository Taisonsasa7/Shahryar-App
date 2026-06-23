import streamlit as st
import random

# إعدادات الصفحة
st.set_page_config(page_title="منصة شهريار", layout="wide")
st.markdown("""<style>.stApp { background-color: #0e0e10; color: white; }</style>""", unsafe_allow_html=True)

# 1. تهيئة البيانات الأساسية
if 'room_name' not in st.session_state: st.session_state.room_name = "🌙 منصة شهريار العالمية"
if 'admins' not in st.session_state: st.session_state.admins = ["Admin1"]
if 'mode' not in st.session_state: st.session_state.mode = "🎙️ غرفة صوتية"
if 'diamonds' not in st.session_state: st.session_state.diamonds = 1000
if 'ticker_message' not in st.session_state: st.session_state.ticker_message = "📢 مرحبا بكم في منصة شهريار!"
if 'viewers' not in st.session_state: st.session_state.viewers = random.randint(500, 1000)

# قائمة الفلترة الذكية
bad_words = ["كلمة1", "كلمة2", "كلمة3"] 

# 2. شريط الإعلانات العالمي (يظهر للجميع)
st.markdown(f"""
    <div style="background-color: #FFD700; color: black; padding: 10px; border-radius: 5px; font-weight: bold; text-align: center; margin-bottom: 20px;">
        {st.session_state.ticker_message}
    </div>
""", unsafe_allow_html=True)

# 3. لوحة الإدارة والإعلانات
with st.sidebar:
    st.header("⚙️ لوحة الإدارة")
    st.session_state.room_name = st.text_input("تغيير اسم الغرفة:", value=st.session_state.room_name)
    st.session_state.mode = st.selectbox("نوع الغرفة:", ["🎙️ غرفة صوتية", "📺 بث مباشر", "🎮 غرف ألعاب"])
    
    st.divider()
    st.header("💎 الإعلان الممول")
    st.write(f"رصيدك: {st.session_state.diamonds} ماسة")
    ad_text = st.text_input("اكتب إعلانك (50 حرف):", max_chars=50)
    
    if st.button("نشر الإعلان (500 ماسة)"):
        if any(word in ad_text.lower() for word in bad_words):
            st.error("الإعلان يحتوي على كلمات غير لائقة!")
        elif st.session_state.diamonds >= 500:
            st.session_state.diamonds -= 500
            st.session_state.ticker_message = f"إعلان ممول: {ad_text}"
            st.success("تم النشر!")
            st.rerun()
        else:
            st.error("رصيد الماس غير كافٍ!")

# 4. واجهة الغرفة
st.title(f"{st.session_state.room_name} | 👁️ {st.session_state.viewers} مشاهد")

if st.session_state.mode == "🎙️ غرفة صوتية":
    cols = st.columns(5)
    for i in range(25):
        with cols[i % 5]:
            st.markdown(f"مايك {i+1}")
            c1, c2 = st.columns(2)
            c1.button("🚫", key=f"k_{i}")
            c2.button("🔇", key=f"m_{i}")

elif st.session_state.mode == "📺 بث مباشر":
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

elif st.session_state.mode == "🎮 غرف ألعاب":
    st.button("بدء تحدي الدومينو")
    st.button("بدء تحدي الأسئلة")
