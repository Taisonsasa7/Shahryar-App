import streamlit as st
import sys
import os

# إعداد المسارات
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))
from gifts_system.gifts_db import gifts
from avatar_system.clothing_db import arab_heritage_wardrobe

st.set_page_config(page_title="داخل الغرفة", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #121016; color: white; }
    .room-box { background-color: #1E1A23; padding: 20px; border-radius: 20px; border: 1px solid #444; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎤 أنت الآن داخل الغرفة")

# --- قسم الملابس (الأفاتار) ---
st.subheader("👕 خزانة الملابس التراثية")
region = st.selectbox("اختر المنطقة:", list(arab_heritage_wardrobe.keys()))
country = st.selectbox("اختر الدولة:", list(arab_heritage_wardrobe[region].keys()))
outfit = st.selectbox("اختر الزي:", arab_heritage_wardrobe[region][country])

if st.button("ارتداء الزي"):
    st.success(f"لقد قمت باختيار {outfit} بنجاح!")

st.write("---")

# --- قسم الهدايا ---
st.subheader("🎁 متجر الهدايا")
cols = st.columns(len(gifts))
for i, (gift_name, details) in enumerate(gifts.items()):
    with cols[i]:
        if st.button(f"إرسال {gift_name}"):
            st.success(f"تم إرسال {gift_name}!")

if st.button("الخروج للرئيسية"):
    st.switch_page("main.py")
