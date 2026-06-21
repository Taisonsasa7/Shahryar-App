import streamlit as st
import sys
import os

# 1. إعداد مسار المجلدات ليقرأ الملفات الأخرى
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))
from gifts_system.gifts_db import gifts

# 2. إعداد الصفحة
st.set_page_config(page_title="داخل الغرفة", layout="wide")

# 3. التصميم (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #121016; color: white; }
    .room-box { background-color: #1E1A23; padding: 20px; border-radius: 20px; border: 1px solid #444; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎤 أنت الآن داخل الغرفة")

# 4. عرض الهدايا (باستخدام نظام الهدايا الخاص بك)
st.markdown('<div class="room-box">', unsafe_allow_html=True)
st.write("### 🎁 متجر الهدايا")

# عرض الهدايا من ملفك gifts_db.py
cols = st.columns(len(gifts))
for i, (gift_name, details) in enumerate(gifts.items()):
    with cols[i]:
        if st.button(f"إرسال {gift_name}"):
            st.success(f"تم إرسال {gift_name} بقيمة {details['price']}!")
            st.balloons() # تأثير احتفالي بسيط

st.markdown('</div>', unsafe_allow_html=True)

# 5. زر العودة
if st.button("الخروج للرئيسية"):
    st.switch_page("main.py")
