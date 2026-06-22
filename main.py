import streamlit as st

# --- تعريف النظام داخل نفس الملف ---
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
            "المبلغ الإجمالي": amount,
            "حصة الإدارة (60%)": amount * 0.6,
            "حصة المضيف (40%)": amount * 0.4
        }

# إنشاء كائن النظام
system = ShahryarCore()

# --- واجهة التطبيق ---
st.title("🌙 شهريار")

# عرض الغرف
st.subheader("الغرف المتاحة:")
for room in system.get_all_rooms():
    st.write(f"✅ {room['name']}")

st.divider()

# حساب الأرباح
st.subheader("حساب الأرباح")
amount = st.number_input("أدخل المبلغ بالدولار", min_value=0.0, step=1.0)

if st.button("حساب التوزيع"):
    result = system.trigger_event(amount)
    st.success("تم الحساب بنجاح:")
    st.json(result)
