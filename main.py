import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="شهريار", layout="wide")

# إضافة CSS لتغيير الخلفية والألوان
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    div.stButton > button {
        background-color: #FFD700;
        color: black;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌙 مرحباً بك في لوحة تحكم شهريار")
st.subheader("المنصة الترفيهية المتكاملة")

# هنا يمكنك إضافة الغرف
st.write("استمتع بأفضل تجربة للدردشة، الألعاب، والبث المباشر.")

col1, col2, col3 = st.columns(3)
with col1:
    st.button("🎤 غرف الدردشة")
with col2:
    st.button("🎥 البث المباشر")
with col3:
    st.button("🎮 قسم الألعاب")
