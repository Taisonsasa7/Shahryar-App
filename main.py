import streamlit as st

st.set_page_config(page_title="منصة شهريار", layout="wide")

# تهيئة حالة الغرف إذا لم تكن موجودة
if 'room_data' not in st.session_state:
    st.session_state.room_data = {i: {"name": f"غرفة {i}", "type": "🎙️ صوتي"} for i in range(1, 100)}

st.markdown("""
    <style>
    .stApp { background-color: #0d0d0d; color: #ffffff; }
    .room-card { background-color: #1a1a1a; border: 2px solid #FFD700; padding: 15px; border-radius: 15px; margin: 10px; text-align: center; }
    .badge { background: #FFD700; color: black; padding: 5px; border-radius: 5px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# دالة لوحة التحكم
def room_admin_panel(room_id):
    st.title(f"⚙️ لوحة تحكم {st.session_state.room_data[room_id]['name']}")
    with st.form("edit_room"):
        new_name = st.text_input("تغيير اسم الغرفة", st.session_state.room_data[room_id]['name'])
        new_type = st.selectbox("تغيير نوع الغرفة", ["🎙️ صوتي", "📺 بث مباشر", "🎮 ألعاب"], 
                                index=["🎙️ صوتي", "📺 بث مباشر", "🎮 ألعاب"].index(st.session_state.room_data[room_id]['type']))
        
        if st.form_submit_button("حفظ التغييرات"):
            st.session_state.room_data[room_id]['name'] = new_name
            st.session_state.room_data[room_id]['type'] = new_type
            st.success("تم التحديث بنجاح!")
            st.rerun()

# المنطق الرئيسي للعرض
if 'current_room' in st.session_state:
    room_admin_panel(st.session_state.current_room)
    if st.button("⬅️ العودة للرئيسية"):
        del st.session_state.current_room
        st.rerun()
else:
    st.title("🌙 منصة شهريار العالمية")
    cols = st.columns(4)
    for i in range(1, 13):
        with cols[(i-1) % 4]:
            st.markdown('<div class="room-card">', unsafe_allow_html=True)
            st.subheader(st.session_state.room_data[i]['name'])
            st.markdown(f'<span class="badge">{st.session_state.room_data[i]["type"]}</span>', unsafe_allow_html=True)
            if st.button("دخول الغرفة", key=f"btn_{i}"):
                st.session_state.current_room = i
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
