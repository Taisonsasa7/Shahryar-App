import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Shahryar Global", layout="wide")

# 1. نظام "الاسم القابل للتعديل" والبيانات العامة
if 'room_name' not in st.session_state: st.session_state.room_name = "🌙 منصة شهريار العالمية"
if 'owner' not in st.session_state: st.session_state.owner = "Shahryar"
if 'admins' not in st.session_state: st.session_state.admins = ["Admin1", "Admin2"]

# 2. وظيفة التحقق (للملايين: يجب أن تربط هذا لاحقاً بقاعدة بيانات SQL)
def is_admin(user):
    return user == st.session_state.owner or user in st.session_state.admins

# 3. واجهة التحكم (تظهر فقط للأدمن والمالك)
with st.sidebar:
    st.header("⚙️ لوحة الإدارة العليا")
    if is_admin("Admin1"): # هنا يوضع اسم المستخدم الفعلي الحالي
        new_name = st.text_input("تغيير اسم الغرفة:", value=st.session_state.room_name)
        if st.button("حفظ الاسم"):
            st.session_state.room_name = new_name
            st.rerun()
        
        st.divider()
        st.write("أضف أدمن جديد:")
        new_admin = st.text_input("اسم الأدمن:")
        if st.button("إضافة أدمن"):
            st.session_state.admins.append(new_admin)
            st.success(f"تم إضافة {new_admin} كأدمن!")

# 4. العنوان الرئيسي (يتحدث فوراً)
st.title(f"{st.session_state.room_name}")

# 5. عرض المايكات (التحديات)
st.subheader("🎤 منصة التحدي العالمية")
cols = st.columns(5)
for i in range(25):
    with cols[i % 5]:
        st.markdown(f"*مايك {i+1}*")
        if is_admin("Admin1"):
            if st.button("🚫 طرد", key=f"kick_{i}"): st.warning("تم الطرد!")
            if st.button("🔇 كتم", key=f"mute_{i}"): st.warning("تم الكتم!")

st.success("المنصة جاهزة للتشغيل!")
