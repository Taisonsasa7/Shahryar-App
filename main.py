import streamlit as st
import random

# إعدادات الصفحة
st.set_page_config(page_title="منصة شهريار", layout="wide")
st.markdown("""<style>.stApp { background-color: #0e0e10; color: white; }</style>""", unsafe_allow_html=True)

# 1. تهيئة البيانات الأساسية (Session State)
if 'room_name' not in st.session_state: st.session_state.room_name = "🌙 منصة شهريار العالمية"
if 'diamonds' not in st.session_state: st.session_state.diamonds = 1000
if 'ticker_message' not in st.session_state: st.session_state.ticker_message = "📢 مرحبا بكم في منصة شهريار!"
if 'viewers' not in st.session_state: st.session_state.viewers = random.randint(500, 1000)
if 'supporters' not in st.session_state: st.session_state.supporters = {"Shahryar": 1000, "User_X": 800}

# 2. شريط الإعلانات العالمي
st.markdown(f"""
    <div style="background-color: #FFD700; color: black; padding: 10px; border-radius: 5px; font-weight: bold; text-align: center; margin-bottom: 20px;">
        {st.session_state.ticker_message}
    </div>
""", unsafe_allow_html=True)

# 3. اللوحة الجانبية (الإدارة + الإعلانات + لوحة الشرف)
with st.sidebar:
    st.header("⚙️ لوحة التحكم")
    st.session_state.room_name = st.text_input("اسم الغرفة:", value=st.session_state.room_name)
    
    st.divider()
    st.header("💎 الإعلان الممول (500 ماسة)")
    ad_text = st.text_input("نص الإعلان (50 حرف):", max_chars=50)
    if st.button("نشر الإعلان"):
        if st.session_state.diamonds >= 500:
            st.session_state.diamonds -= 500
            st.session_state.ticker_message = f"إعلان ممول: {ad_text}"
            st.rerun()
        else:
            st.error("رصيدك غير كافٍ!")

    st.divider()
    st.header("🏆 قائمة كبار الداعمين")
    sorted_supporters = sorted(st.session_state.supporters.items(), key=lambda x: x[1], reverse=True)
    for i, (name, score) in enumerate(sorted_supporters[:10]):
        medal = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else f"{i+1}."
        st.write(f"{medal} *{name}*: {score} نقطة")

# 4. واجهة الغرفة
st.title(f"{st.session_state.room_name} | 👁️ {st.session_state.viewers} مشاهد")

st.subheader("🎁 إرسال دعم للغرفة")
if st.button("إرسال هدية (100 ماسة)"):
    if st.session_state.diamonds >= 100:
        st.session_state.diamonds -= 100
        st.session_state.supporters["أنت"] = st.session_state.supporters.get("أنت", 0) + 100
        st.success("تم إرسال الهدية!")
        st.rerun()
    else:
        st.error("رصيدك غير كافٍ!")

st.subheader("🎤 منصة المتحدثين")
cols = st.columns(5)
for i in range(25):
    with cols[i % 5]:
        st.markdown(f"*مايك {i+1}*")
        st.button("🚫", key=f"k_{i}")
