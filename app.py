 import streamlit as st
from supabase import create_client
from database_manager import get_all_agencies

# 1. إعداد الصفحة (يجب أن يكون أول أمر دائماً)
st.set_page_config(page_title="Shahryar-App", layout="centered")

# 2. إعدادات الاتصال بـ Supabase
url = "ضع_رابط_Supabase_هنا"
key = "ضع_مفتاح_API_هنا"
supabase = create_client(url, key)

# 3. تنسيق CSS
st.markdown("""
<style>
.stApp { background-color: #0e0e0e; color: white; }
.room-card { background-color: #1a1a1a; border-radius: 15px; padding: 15px; margin-bottom: 15px; border: 1px solid #333; }
</style>
""", unsafe_allow_html=True)

# 4. العنوان
st.title("لوحة تحكم السوبر أدمن")
st.write("جاري تحميل البيانات...") 

# 5. جلب وعرض بيانات الغرف من Supabase
st.subheader("إدارة الغرف")
try:
    response = supabase.table("roomsr").select("*").execute()
    rooms = response.data
    if rooms:
        for room in rooms:
            st.markdown(f"""
            <div class="room-card">
                <h4>{room.get('room_name')}</h4>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.write("لا توجد غرف مسجلة.")
except Exception as e:
    st.error(f"خطأ في الاتصال بـ Supabase: {e}")

# 6. جلب وعرض بيانات الوكالات من Google Sheets
st.divider()
st.subheader("وكالات المنصة (Google Sheets)")

agencies = get_all_agencies()

if agencies:
    st.table(agencies)
else:
    st.write("لا توجد وكالات مسجلة في Google Sheets.")
[4:26 م، 2026/6/24] taisonsasa8: import streamlit as st
from database_manager import get_all_agencies

st.set_page_config(page_title="Shahryar-App", layout="centered")

st.title("لوحة تحكم السوبر أدمن")

st.write("جاري جلب بيانات الوكالات...")

# جلب بيانات الوكالات من Google Sheets
agencies = get_all_agencies()

if agencies:
    st.table(agencies)
else:
    st.write("لم يتم العثور على وكالات.")


