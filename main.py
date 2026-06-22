import streamlit as st

# 1. إعداد التصميم (الأسود والذهبي)
st.markdown("""
    <style>
    .stApp { background-color: #0d0d0d; color: #ffffff; }
    .room-card { 
        background-color: #1a1a1a; 
        border: 2px solid #FFD700; 
        padding: 20px; 
        border-radius: 15px; 
        margin-bottom: 15px; 
        text-align: center; 
    }
    h1 { color: #FFD700 !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. تعريف الغرف مباشرة داخل الملف (بدون فئات خارجية لتجنب الخطأ)
rooms_data = {
    "غرفة البث المباشر": "🔴",
    "غرفة الدردشة الصوتية": "🎙️",
    "غرفة الألعاب": "🎮"
}

st.title("🌙 شهريار")

# 3. عرض الغرف
for name, icon in rooms_data.items():
    st.markdown(f"""
    <div class="room-card">
        <h1>{icon}</h1>
        <h3>{name}</h3>
    </div>
    """, unsafe_allow_html=True)
    if st.button(f"دخول {name}", key=name):
        st.write(f"جاري التوجيه إلى {name}...")

st.divider()

# 4. لوحة الحسابات
st.subheader("💰 لوحة التحكم المالية")
val = st.number_input("أدخل كمية الماس:", min_value=0, value=0)

if st.button("توزيع الأرباح"):
    admin_share = val * 0.6
    host_share = val * 0.4
    st.success(f"حصة الإدارة: {admin_share:.2f}")
    st.success(f"حصة المضيف: {host_share:.2f}")
