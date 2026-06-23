import streamlit as st
from supabase import create_client

# إعداد الاتصال بقاعدة البيانات
supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

# جلب البيانات من الجدول الصحيح roomsr
try:
    response = supabase.table("roomsr").select("*").execute()
    rooms_data = response.data
except Exception as e:
    st.error(f"خطأ في الاتصال: {e}")
    rooms_data = []

st.title("منصة شهريار العالمية 🌙")
response = supabase.table("roomsr").select("*").execute()
if rooms_data:
    # عرض الغرف
    cols = st.columns(3)
    for i, room in enumerate(rooms_data):
        with cols[i % 3]:
            # تحديد الحالة (نشطة أو غير نشطة)
            status = "نشطة" if room.get('is_active') else "غير نشطة"
            
            st.markdown(f"""
            <div style="border: 2px solid #FFD700; padding: 20px; border-radius: 15px; text-align: center;">
                <h3>{room['room_name']}</h3>
                <p>الحالة: {status} | الألماس: {room['diamonds']}</p>
            </div>
            """, unsafe_allow_html=True)
else:
    st.write("لا توجد غرف متاحة حالياً في قاعدة البيانات.")
