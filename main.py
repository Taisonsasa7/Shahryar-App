import streamlit as st

# إعدادات التصميم
st.set_page_config(page_title="منصة شهريار", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0d0d0d; color: #ffffff; }
    .room-card { 
        background-color: #1a1a1a; 
        border: 2px solid #FFD700; 
        padding: 20px; 
        border-radius: 15px; 
        margin: 10px; 
        text-align: center; 
    }
    h3 { color: #FFD700; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌙 منصة شهريار العالمية")

# دالة محلية لجلب الغرف (تم تعريفها هنا مباشرة لمنع ظهور الخطأ)
def get_rooms_from_db(search_query):
    # محاكاة لآلاف الغرف
    all_rooms = [{"id": i, "name": f"غرفة رقم {i}"} for i in range(1, 5001)]
    if search_query:
        return [r for r in all_rooms if search_query.lower() in r['name'].lower()]
    return all_rooms[:50] # يعرض أول 50 غرفة فقط للتسريع

# نظام البحث
search_query = st.text_input("🔍 ابحث عن غرفة...")

# عرض الغرف
rooms = get_rooms_from_db(search_query)

cols = st.columns(4)
for i, room in enumerate(rooms):
    with cols[i % 4]:
 # --- تعديل لعرض الشارة ---
        user_role = get_user_privilege(db, room['id'], current_user_id) # استدعاء الصلاحية
        badge = get_role_badge(user_role) # الحصول على الرمز
        
        st.markdown(f"""
        <div class="room-card">
            <h3>{room['name']} {badge}</h3>
        </div>
        """, unsafe_allow_html=True)
        # ------------------------  
        """, unsafe_allow_html=True)
        st.button(f"دخول", key=f"btn_{room['id']}")
