mport streamlit as st

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

# دالة لجلب الغرف
def get_rooms_from_db(search_query):
    all_rooms = [{"id": i, "name": f"Room {i}"} for i in range(1, 1000001)]
    if search_query:
        return [r for r in all_rooms if search_query.lower() in r['name'].lower()]
    return all_rooms[:20]

# نظام البحث
search_query = st.text_input("🔍 Search for a room...")

# عرض الغرف
rooms = get_rooms_from_db(search_query)
cols = st.columns(4)

for i, room in enumerate(rooms):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="room-card">
            <h3>{room['name']} 👑</h3>
        </div>
        """, unsafe_allow_html=True)
        # هذا السطر هو الذي كان يسبب الخطأ، تم تصحيحه هنا:
        st.button("Enter", key=f"btn_{room['id']}")
