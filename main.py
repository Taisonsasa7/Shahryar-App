import streamlit as st

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

# نظام الملايين: لا نولد الغرف مسبقاً، بل نولدها عند الطلب
def get_rooms(page=1):
    # نحدد 20 غرفة فقط في كل صفحة لضمان السرعة
    start = (page - 1) * 20 + 1
    end = start + 20
    return [{"id": i, "name": f"غرفة رقم {i}"} for i in range(start, end)]

# اختيار الصفحة (للتنقل بين الملايين)
page = st.number_input("رقم الصفحة (للتنقل بين الملايين)", min_value=1, value=1)

rooms = get_rooms(page)
cols = st.columns(4)

for i, room in enumerate(rooms):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="room-card">
            <h3>{room['name']} 👑</h3>
        </div>
        """, unsafe_allow_html=True)
        st.button("دخول", key=f"btn_{room['id']}")
