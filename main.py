import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# 1. التنسيق (الأسود، الذهبي، البنفسجي)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; font-family: Arial; }
    h1, h2, h3 { color: #D4AF37; text-align: center; }
    div.stDataFrame { border: 2px solid #800080; }
    </style>
""", unsafe_allow_html=True)

# 2. إضافة زر تسجيل الدخول بـ Pi (مُحدث ليتوافق مع متطلبات الربط)
def login_with_pi():
    pi_auth_html = """
    <div style="text-align: center; border: 1px solid #D4AF37; padding: 20px; border-radius: 10px;">
        <h3 style="color: #D4AF37;">مرحباً بك في لوحة تحكم شهريار</h3>
        <p style="color: white;">يرجى تسجيل الدخول عبر شبكة باي لفتح التقارير المالية</p>
        <button style="padding: 15px 30px; background-color: #D4AF37; border: none; color: black; font-weight: bold; cursor: pointer; border-radius: 5px;">
            Login with Pi
        </button>
        <p style="font-size: 10px; margin-top: 10px; color: #888;">الرجاء التأكد من أنك تفتح هذا التطبيق من داخل Pi Browser</p>
    </div>
    """
    components.html(pi_auth_html, height=250)

# 3. إعداد البيانات
def get_room_data():
    data = {
        "الغرفة": ["غرفة 1", "غرفة 2", "غرفة 3", "غرفة 4"],
        "المضيف": ["Ahmed", "Sara", "Mohamed", "Laila"],
        "إجمالي المبيعات": [1000, 5000, 1500, 3000]
    }
    df = pd.DataFrame(data)
    df["N60"] = df["إجمالي المبيعات"] * 0.60
    df["N30"] = df["إجمالي المبيعات"] * 0.30
    df["N10"] = df["إجمالي المبيعات"] * 0.10
    return df

# 4. عرض الواجهة
st.title("لوحة تحكم شهريار")
st.subheader("التقرير المالي للغرف")

# نضع زر تسجيل الدخول أولاً
login_with_pi()

st.write("---")
df = get_room_data()

# عرض الجدول
st.dataframe(df.style.format({
    "إجمالي المبيعات": "${:,.2f}",
    "N60": "${:,.2f}",
    "N30": "${:,.2f}",
    "N10": "${:,.2f}"
}))
