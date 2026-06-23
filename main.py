import streamlit as st
import random

# إعدادات الواجهة
st.set_page_config(page_title="منصة شهريار العالمية", layout="wide")
st.markdown("""<style>.stApp { background-color: #0e0e10; color: white; }</style>""", unsafe_allow_html=True)

# 1. تهيئة الغرف (في الواقع هذا سيأتي من قاعدة بيانات)
from supabase import create_client

# الاتصال بقاعدة البيانات
supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

if 'rooms' not in st.session_state:
    # جلب البيانات من جدول rooms في قاعدة بياناتك
    response = supabase.table("rooms").select("*").execute()
    st.session_state.rooms = response.data

# 2. الواجهة الرئيسية (قائمة الغرف مرتبة حسب النشاط)
def show_main_page():
    st.title("🌙 منصة شهريار العالمية")
    st.subheader("الغرف الأكثر نشاطاً")
    
    # ترتيب الغرف تلقائياً (النشاط = مشاهدات + ماسات)
    sorted_rooms = sorted(st.session_state.rooms, key=lambda x: (x['viewers'] + x['diamonds']), reverse=True)
    
    cols = st.columns(3)
    for i, room in enumerate(sorted_rooms):
        with cols[i % 3]:
            st.markdown(f"""
                <div style="border: 2px solid #FFD700; padding: 20px; border-radius: 15px; text-align: center;">
st.markdown(f"""
            <div style="border: 2px solid #FFD700; padding: 20px; border-radius: 15px; text-align: center;">
                <h3>{room['room_name']}</h3>
                <p>👁️ {room['viewers']} | 💎 {room['diamonds']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"دخول {room['room_name']}", key=f"btn_{i}"):
            st.session_state.current_room = room['room_name']
            st.rerun()

# 3. واجهة داخل الغرفة (بالتصميم الذي بنيناه)
def show_room_interface():
    st.sidebar.button("⬅️ عودة للرئيسية", on_click=lambda: st.session_state.pop('current_room'))
    st.title(f"🏠 {st.session_state.current_room}")
    
    # المايكات والألقاب (👑 المالك، 🛡️ الأدمن)
    st.subheader("🎤 منصة المتحدثين")
    cols = st.columns(5)
    for i in range(10):
        with cols[i % 5]:
            badge = "👑" if i == 0 else "🛡️" if i == 1 else "👤"
            st.markdown(f"{badge} *مايك {i+1}*")
            st.button("🚫", key=f"mic_{i}")

# منطق التنقل
if 'current_room' not in st.session_state:
    show_main_page()
else:
    show_room_interface()
