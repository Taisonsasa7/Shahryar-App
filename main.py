import streamlit as st
from shahryar_core import shahryar_system

st.set_page_config(page_title="شهريار", layout="wide")
st.title("🌙 شهريار")

# جلب الغرف من المحرك الموحد
rooms = shahryar_system.get_all_rooms()

# عرض الغرف بشكل شبكي
cols = st.columns(len(rooms))
for i, room in enumerate(rooms):
    with cols[i]:
        # عرض صورة الغرفة (تأكد من وجود مجلد باسم images)
        st.image(f"images/{room['id']}.jpg", use_container_width=True)
        
        # زر الدخول
        if st.button(f"دخول {room['name']}", key=room['id']):
            st.success(f"أنت الآن في {room['name']}")

# إدارة الأرباح
with st.sidebar:
    st.header("إدارة الأرباح")
    amount = st.number_input("أدخل المبلغ بالدولار", min_value=0.0)
    if st.button("حساب التوزيع"):
        result = shahryar_system.trigger_event("GIFT_RECEIVED", amount)
        st.json(result
