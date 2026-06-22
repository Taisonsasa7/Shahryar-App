import streamlit as st

# تعريف النظام داخل نفس الملف لضمان عمله
class ShahryarCore:
    def _init_(self):
        # تعريف الغرف هنا بوضوح
        self.rooms = [
            {"id": "gaming", "name": "غرفة الألعاب"},
            {"id": "music", "name": "غرفة الموسيقى"}
        ]
    
    def get_all_rooms(self):
        return self.rooms

    def trigger_event(self, amount):
        # حساب بسيط للأرباح
        return {
            "المبلغ": amount,
            "حصة الإدارة": amount * 0.6,
            "حصة المضيف": amount * 0.4
        }

# إنشاء كائن النظام
system = ShahryarCore()

# واجهة التطبيق
st.title("🌙 شهريار")

st.subheader("الغرف المتاحة:")
for room in system.get_all_rooms():
    st.write(f"✅ {room['name']}")

st.divider()

amount = st.number_input("أدخل المبلغ بالدولار", min_value=0.0)
if st.button("حساب التوزيع"):
    result = system.trigger_event(amount)
    st.json(result)
