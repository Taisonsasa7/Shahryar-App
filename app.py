import streamlit as st

# التنسيق (الأسود، الذهبي، والبنفسجي) مدمج مباشرة
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; font-family: Arial; }
    h1, h2 { color: #D4AF37; text-align: center; }
    div.stButton > button { 
        background-color: #800080; 
        color: #D4AF37; 
        border: 2px solid #D4AF37; 
        width: 100%;
    }
    div.stButton > button:hover { background-color: #D4AF37; color: #000; }
    input { background-color: #1a1a1a !important; color: white !important; border: 1px solid #800080 !important; }
    </style>
""", unsafe_allow_html=True)

# واجهة التطبيق
st.title("شهريار")
st.write("مرحباً بك في عالم شهريار الرقمي")

# المدخلات
usd = st.number_input("أدخل المبلغ (USD)", min_value=0)

if st.button("احسب"):
    # هنا تضع منطق الحساب الخاص بك
    st.write(f"النتيجة ستظهر هنا بناءً على المبلغ: {usd}")
