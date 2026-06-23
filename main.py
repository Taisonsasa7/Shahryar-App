import streamlit as st
from supabase import create_client

# إعدادات الصفحة
st.set_page_config(page_title="منصة شهريار العالمية", layout="wide")

# الاتصال بقاعدة البيانات
supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

# جلب البيانات
try:
    response = supabase.table("roomsr").select("*").execute()
    st.session_state.rooms = response.data
except Exception as e:
    st.error(f"خطأ في الاتصال: {e}")
    st.session_state.rooms = []

def show_main_page():
    st.title("منصة شهريار العالمية 🌙")
    st.subheader("الغرف المتاحة حالياً 🔥")
    
    if st.session_state.rooms:
        cols = st.columns(3)
        for i, room in enumerate(st.session_state.rooms):
            with cols[i % 3]:
                # عرض البيانات بناءً على الأعمدة الموجودة في قاعدة بياناتك
                status = "نشطة" if room.get('is_active') else "غير نشطة"
                st.markdown(f"""
                <div style="border: 2px solid #FFD700; padding: 20px; border-radius: 15px; text-align: center;">
                    <h3>{room['room_name']}</h3>
                    <p>الحالة: {status} | الألماس: {room['diamonds']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"دخول {room['room_name']}", key=f"btn_{i}"):
                    st.session_state.current_room = room['room_name']
                    st.rerun()
    else:
        st.write("لا توجد غرف متاحة حالياً في قاعدة البيانات.")

# منطق التنقل
if 'current_room' not in st.session_state:
    show_main_page()
else:
    st.title(f"🏠 {st.session_state.current_room}")
    if st.button("⬅️ العودة للرئيسية"):
        del st.session_state.current_room
        st.rerun()
