import streamlit as st
import random

# إعدادات الواجهة
st.set_config(page_title="منصة شهريار", layout="wide")
st.markdown("""<style>.stApp { background-color: #0e0e10; color: white; }</style>""", unsafe_allow_html=True)

# 1. تهيئة البيانات (المالك، الأدمن، النشاط)
if 'rooms' not in st.session_state:
    # قائمة غرف افتراضية مع "نقاط نشاط" تعتمد على الماسات والمشاهدين
    st.session_state.rooms = [
        {"name": "غرفة السهرة الذهبية", "viewers": 1500, "diamonds": 5000, "price": 100},
        {"name": "تحديات الملوك", "viewers": 800, "diamonds": 2000, "price": 50},
        {"name": "غرفة صوتية عامة", "viewers": 200, "diamonds": 100, "price": 0}
    ]

# وظيفة ترتيب الغرف (الأكثر نشاطاً في الأعلى)
def get_sorted_rooms():
    return sorted(st.session_state.rooms, key=lambda x: (x['viewers'] + x['diamonds']), reverse=True)

# 2. واجهة اختيار الغرف (الواجهة الرئيسية)
st.title("🌙 منصة شهريار العالمية")
st.subheader("الغرف الأكثر نشاطاً الآن")

# عرض الغرف مرتبة
sorted_rooms = get_sorted_rooms()
cols = st.columns(3)
for i, room in enumerate(sorted_rooms):
    with cols[i % 3]:
        st.markdown(f"""
            <div style="border: 2px solid #FFD700; padding: 10px; border-radius: 10px;">
                <h3>{room['name']}</h3>
                <p>👁️ {room['viewers']} | 💎 {room['diamonds']}</p>
                <button>دخول الغرفة</button>
            </div>
        """, unsafe_allow_html=True)

st.divider()

# 3. داخل الغرفة (نظام الألقاب والتحكم)
def get_user_badge(is_owner, is_admin):
    if is_owner: return "👑 المالك"
    if is_admin: return "🛡️ الأدمن"
    return "👤 مستخدم"

st.subheader("داخل الغرفة")
col1, col2 = st.columns([1, 3])
with col1:
    st.write(f"الألقاب: {get_user_badge(True, False)}")
with col2:
    st.write("المايكات هنا...")
