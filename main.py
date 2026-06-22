import streamlit as st

# النظام كامل داخل هذا الكلاس في ملف واحد
class ShahryarCore:
    def _init_(self):
        self.rooms = ["غرفة الألعاب", "غرفة الموسيقى"]
    
    def get_rooms(self):
        return self.rooms

    def calculate(self, amount):
        # حساب الأرباح (60% للإدارة، 40% للمضيف)
        return amount * 0.6, amount * 0.4

# إنشاء كائن النظام
system = ShahryarCore()

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
