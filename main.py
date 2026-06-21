import streamlit as st

st.set_page_config(page_title="شهريار", layout="wide")

# بيانات تجريبية (تخيل هذه قادمة من قاعدة بياناتك)
rooms_data = [
    {"name": "Alex", "title": "Soirée gaming", "viewers": 234, "likes": 89},
    {"name": "Sofia", "title": "Session musique", "viewers": 567, "likes": 312},
    {"name": "Karim", "title": "نقاش مفتوح", "viewers": 123, "likes": 45},
    {"name": "Luna", "title": "تحدي رقص", "viewers": 890, "likes": 456},
    {"name": "Yuki", "title": "Best anime", "viewers": 345, "likes": 178},
    {"name": "DJ Max", "title": "Freestyle rap", "viewers": 456, "likes": 234},
]

st.markdown("""
    <style>
    .room-card { background-color: #1E1A23; border-radius: 20px; padding: 15px; margin: 10px; color: white; }
    .live-badge { ba…
[11:21 م، 2026/6/21] taisonsasa8: import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="شهريار", layout="wide")

# بيانات الغرف (يمكنك إضافة المزيد هنا)
rooms_data = [
    {"name": "Alex", "title": "Soirée gaming", "viewers": 234, "likes": 89},
    {"name": "Sofia", "title": "Session musique", "viewers": 567, "likes": 312},
    {"name": "Karim", "title": "نقاش مفتوح", "viewers": 123, "likes": 45},
    {"name": "Luna", "title": "تحدي رقص", "viewers": 890, "likes": 456},
    {"name": "Yuki", "title": "Best anime", "viewers": 345, "likes": 178},
    {"name": "DJ Max", "title": "Freestyle rap", "viewers": 456, "likes": 234},
]

# تنسيق الألوان (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #121016; color: white; }
    .room-card { 
        background-color: #1E1…
