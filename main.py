import streamlit as st

# إعداد الصفحة الرئيسية
st.set_page_config(page_title="ألف ليلة وليلة", layout="wide")

st.title("🌙 مرحباً بك في عالم ألف ليلة وليلة")
st.subheader("المنصة الترفيهية المتكاملة")

st.write("استمتع بأفضل تجربة للدردشة، الألعاب، والبث المباشر.")

# أزرار للتنقل السريع داخل المنصة
col1, col2, col3 = st.columns(3)
with col1:
    st.button("🎤 غرف الدردشة")
with col2:
    st.button("🎥 البث المباشر")
with col3:
    st.button("🎮 قسم الألعاب")

st.sidebar.info("مرحباً بك! اختر القسم الذي تود زيارته
