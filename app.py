import streamlit as st
from supabase import create_client

# إعداد الصفحة
st.set_page_config(page_title="شهريار", layout="centered")

# إعدادات الاتصال بـ Supabase (ضع القيم الخاصة بمشروعك هنا)
url = "ضع_هنا_رابط_Supabase_URL"
key = "ضع_هنا_مفتاح_API_KEY"
supabase = create_client(url, key)

# تنسيق CSS
st.markdown("""
<style>
.stApp { background-color: #0e0e0e; color: white; }
.room-card {
    background-color: #1a1a1a; border-radius: 15px; padding: 15px;
    margin-bottom: 15px; border: 1px solid #333;
}
</style>
""", unsafe_allow_html=True)

# العنوان
st.title("شهريار")

# جلب البيانات من قاعدة البيانات
try:
    response = supabase.table("roomsr").select("*").execute()
    rooms = response.data
except Exception as e:
    st.error(f"حدث خطأ في الاتصال بقاعدة البيانات: {e}")
    rooms = []

# عرض الغرف
col1, col2 = st.columns(2)

if rooms:
    for i, room in enumerate(rooms):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f"""
            <div class="room-card">
                <h4 style="margin:0;">{room.get('room_name', 'غرفة بدون اسم')}</h4>
                <p style="font-size:0.8em; color:#aaa;">الماس: {room.get('diamonds', 0)}</p>
            </div>
            """, unsafe_allow_html=True)
else:
    st.write("لا توجد غرف حالياً.")
