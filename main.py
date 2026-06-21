import streamlit as st
import pandas as pd

# 1. التنسيق (الأسود، الذهبي، البنفسجي)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; font-family: Arial; }
    h1, h2, h3 { color: #D4AF37; text-align: center; }
    div.stDataFrame { border: 2px solid #800080; }
    </style>
""", unsafe_allow_html=True)

# 2. إعداد البيانات
def get_room_data():
    data = {
        "الغرفة": ["غرفة 1", "غرفة 2", "غرفة 3", "غرفة 4"],
        "المضيف": ["Ahmed", "Sara", "Mohamed", "Laila"],
        "إجمالي المبيعات": [1000, 5000, 1500, 3000]
    }
    df = pd.DataFrame(data)
    
    # الحسابات
    df["N60"] = df["إجمالي المبيعات"] * 0.60
    df["N30"] = df["إجمالي المبيعات"] * 0.30
    df["N10"] = df["إجمالي المبيعات"] * 0.10
    return df

# 3. عرض الواجهة
st.title("لوحة تحكم شهريار")
st.subheader("التقرير المالي للغرف")

df = get_room_data()

# عرض الجدول بالتنسيق المطلوب
st.dataframe(df.style.format({
    "إجمالي المبيعات": "${:,.2f}",
    "N60": "${:,.2f}",
    "N30": "${:,.2f}",
    "N10": "${:,.2f}"
}))
