import streamlit as st

# سنستخدم دوال عادية بدلاً من الكلاس لتجنب مشاكل الذاكرة
def get_rooms():
    return ["غرفة الألعاب", "غرفة الموسيقى"]

def calculate_shares(amount):
    return amount * 0.6, amount * 0.4

# واجهة التطبيق
st.title("🌙 شهريار")
st.subheader("الغرف المتاحة:")

# عرض الغرف مباشرة
rooms = get_rooms()
for room in rooms:
    st.write(f"✅ {room}")

st.divider()

val = st.number_input("أدخل المبلغ بالدولار:", min_value=0.0)
if st.button("حساب الأرباح"):
    admin, host = calculate_shares(val)
    st.write(f"حصة الإدارة: {admin} دولار")
    st.write(f"حصة المضيف: {host} دولار")
