import streamlit as st

# تعريف الكلاس داخل نفس الملف لضمان عدم وجود خطأ استيراد
class ShahryarCore:
    def _init_(self):
        self.rooms = [
            {"id": "gaming", "name": "غرفة الألعاب"},
            {"id": "music", "name": "غرفة الموسيقى"}
        ]
    
    def get_all_rooms(self):
        return self.rooms

    def trigger_event(self, amount):
        return {
            "المبلغ": amount,
            "حصة الإدارة": amount * 0.6,
            "حصة المضيف": amount * 0.4
        }

# إنشاء الكائن
system = ShahryarCore()

# واجهة المستخدم
st.title("🌙 شهريار")
st.subheader("الغرف المتاحة:")

# عرض الغرف
for room in system.get_all_rooms():
    st.write(f"✅ {room['name']}")

st.divider()

# حساب الأرباح
amount = st.number_input("أدخل المبلغ بالدولار", min_value=0.0)
if st.button("حساب التوزيع"):
    result = system.trigger_event(amount)
    st.json(result)
