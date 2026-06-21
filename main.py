import streamlit as st

st.set_page_config(page_title="شهريار", layout="wide")

# تصميم الواجهة الرئيسية
st.title("🌙 شهريار")

rooms_data = [
    {"name": "غرفة الألعاب", "id": "gaming"},
    {"name": "غرفة الموسيقى", "id": "music"},
]

# عرض البطاقات (الغرف)
for room in rooms_data:
    st.write(f"### {room['name']}")
    if st.button(f"دخول {room['name']}", key=room['id']):
        # حفظ اسم الغرفة المختارة للانتقال
        st.session_state.current_room = room['name']
        st.switch_page("pages/room.py")
