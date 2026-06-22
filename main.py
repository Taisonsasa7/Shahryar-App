import streamlit as st

# قمنا بتغيير اسم الكلاس ليضطر النظام لإعادة القراءة
class ShahryarNewSystem:
    def _init_(self):
        # تعريف الغرف هنا بشكل صريح
        self.rooms_list = ["غرفة الألعاب", "غرفة الموسيقى"]
    
    def get_rooms(self):
        return self.rooms_list

    def calculate(self, amount):
        return amount * 0.6, amount * 0.4

# إنشاء كائن النظام الجديد
system = ShahryarNewSystem()

# واجهة التطبيق
st.title("🌙 شهريار")
st.write("### الغرف المتاحة:")
for room in system.get_rooms():
    st.write(f"✅ {room}")

st.divider()

val = st.number_input("أدخل المبلغ بالدولار:", min_value=0.0)
if st.button("حساب الأرباح"):
    admin, host = system.calculate(val)
    st.write(f"حصة الإدارة: {admin} دولار")
    st.write(f"حصة المضيف: {host} دولار")
