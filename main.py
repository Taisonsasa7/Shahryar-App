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

# دالة محلية لجلب الغرف
def get_rooms_from_db(search_query):
 بدلاً من توليد الغرف برمجياً، نجلبها من "قاعدة البيانات"
# هذا يعني أن الغرف موجودة فعلياً في القاعدة (سواء كانت 10 أو 10 ملايين)
# نحن لا نولدها في الكود، نحن نطلبها فقط.

def get_rooms_from_db(search_query, page=1):
    # هنا ستقوم قاعدة البيانات بجلب 20 غرفة فقط في كل مرة (صفحة)
    # هذا يسمى Pagination، وهو السر الذي يجعل التطبيق لا ينهار مهما كان عدد الغرف
    rooms = database.query(f"SELECT * FROM rooms LIMIT 20 OFFSET {(page-1)*20}")
    return rooms
    return all_rooms[:20]

# --- دوال الصلاحيات (الجزء المظلل بالأزرق الذي طلبته) ---
def get_user_privilege(db, room_id, user_id):
    return "admin" # مؤقتاً حتى نربط القاعدة

def get_role_badge(role):
    badges = {"admin": "👑", "user": "👤"}
    return badges.get(role, "👤")
# -----------------------------------------------------

search_query = st.text_input("🔍 ابحث عن غرفة...")
rooms = get_rooms_from_db(search_query)

cols = st.columns(4)
for i, room in enumerate(rooms):
    with cols[i % 4]:
        # استدعاء الجزء المظلل بالأزرق
        user_role = get_user_privilege(None, room['id'], "current_user") 
        badge = get_role_badge(user_role)
        
        # عرض الغرفة مع الشارة
        st.markdown(f"""
        <div class="room-card">
            <h3>{room['name']} {badge}</h3>
        </div>
        """, unsafe_allow_html=True)
        st.button(f"دخول", key=f"btn_{room['id']}")
