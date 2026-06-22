import streamlit as st

def get_rooms():
    return ["غرفة الألعاب", "غرفة الموسيقى"]

def calculate_shares(amount):
    return amount * 0.6, amount * 0.4

st.title("🌙 شهريار")
st.subheader("الغرف المتاحة:")

for room in get_rooms():
    st.write(f"✅ {room}")

st.divider()

# استخدام session_state لحفظ القيم
if 'result' not in st.session_state:
    st.session_state.result = None

val = st.number_input("أدخل المبلغ بالدولار:", min_value=0.0, value=0.0)

if st.button("حساب الأرباح"):
    admin, host = calculate_shares(val)
    st.session_state.result = (admin, host)

# عرض النتيجة إذا كانت موجودة في الذاكرة
if st.session_state.result:
    admin, host = st.session_state.result
    st.success(f"حصة الإدارة: {admin:.2f} دولار")
    st.success(f"حصة المضيف: {host:.2f} دولار")
