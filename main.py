
import streamlit as st

# 1. تهيئة الذاكرة الدائمة (لضمان عدم ضياع الألوان والبيانات)
if 'room_name' not in st.session_state: st.session_state.room_name = "🌙 منصة شهريار العالمية"
if 'owner' not in st.session_state: st.session_state.owner = "Shahryar"
if 'admins' not in st.session_state: st.session_state.admins = ["Admin1", "Admin2"]

# دالة لتحديد الألوان بناءً على الصلاحية (ثابتة لا تتغير)
def get_user_style(username):
    if username == st.session_state.owner: return "👑", "#FFD700"  # ذهبي
    if username in st.session_state.admins: return "🛡️", "#00FF00"  # أخضر
    return "👤", "#FFFFFF"  # أبيض

# 2. لوحة الإدارة (Sidebar)
with st.sidebar:
    st.header("⚙️ لوحة الإدارة العليا")
    new_name = st.text_input("تغيير اسم الغرفة:", value=st.session_state.room_name)
    if st.button("حفظ الاسم"):
        st.session_state.room_name = new_name
        st.rerun()
    
    st.divider()
    new_admin = st.text_input("إضافة أدمن جديد:")
    if st.button("إضافة"):
        if new_admin not in st.session_state.admins:
            st.session_state.admins.append(new_admin)
            st.success(f"تمت إضافة {new_admin}")

# 3. واجهة المنصة
st.title(f"{st.session_state.room_name}")
st.subheader("🎤 منصة التحدي (25 مايك)")

# 4. عرض المايكات
cols = st.columns(5)
for i in range(25):
    with cols[i % 5]:
        st.markdown(f"*مايك {i+1}*")
        # زر الطرد والكتم بألوان ثابتة
        if st.button("🚫 طرد", key=f"kick_{i}"):
            st.warning(f"تم طرد المستخدم في مايك {i+1}")
        if st.button("🔇 كتم", key=f"mute_{i}"):
            st.info(f"تم كتم مايك {i+1}")
