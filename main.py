import streamlit as st
# ستحتاج هنا لربط قاعدة البيانات
# from database import get_rooms_from_db 

st.title("🌙 منصة شهريار العالمية")

# شريط بحث ذكي للوصول لأي غرفة من آلاف الغرف
search_query = st.text_input("🔍 ابحث عن غرفتك (مثلاً: العاب، بث مباشر)...")

# نظام عرض الغرف الديناميكي (يستبدل الكتابة اليدوية)
def display_rooms():
    # هنا يتم استدعاء الغرف من قاعدة البيانات بناءً على البحث
    rooms = get_rooms_from_db(search_query) 
    
    # عرض الغرف في صفوف (Grid)
    cols = st.columns(3) # عرض 3 غرف في الصف الواحد
    for i, room in enumerate(rooms):
        with cols[i % 3]:
            st.markdown(f"### {room['title']}")
            if st.button(f"دخول {room['id']}"):
                st.write(f"جارٍ الاتصال بالغرفة {room['id']}...")

display_rooms()
