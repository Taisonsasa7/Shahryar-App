import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="شهريار", layout="centered")

# CSS المظلم
st.markdown("""
    <style>
    .stApp { background-color: #0e0e0e; color: white; }
    .room-card { background-color: #1a1a1a; border-radius: 15px; padding: 15px; margin-bottom: 15px; border: 1px solid #333; }
    </style>
""", unsafe_allow_html=True)

# التحقق من حالة تسجيل الدخول
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("مرحباً بك في شهريار")
    components.html("""
        <button id="pi-btn" style="background: #d63384; color:white; padding:15px; border:none; border-radius:10px; width:100%;">Sign in with Pi</button>
        <script src="https://sdk.minepi.com/pi-sdk.js"></script>
        <script>
            const Pi = window.Pi;
            Pi.init({ version: "2.0", sandbox: true });
            document.getElementById('pi-btn').onclick = async () => {
                const auth = await Pi.authenticate(["username"]);
                window.location.href = window.location.href + "?auth=success";
            };
        </script>
    """, height=100)
    
    # التحقق من نجاح التوثيق عبر المتغير
    params = st.experimental_get_query_params()
    if 'auth' in params and params['auth'][0] == 'success':
        st.session_state.logged_in = True
        st.experimental_rerun()
else:
    # واجهة الغرف (تظهر فقط بعد تسجيل الدخول)
    st.title("غرف شهريار")
    col1, col2 = st.columns(2)
    rooms = [{"name": "غرفة الألعاب"}, {"name": "غرفة الموسيقى"}]
    for i, room in enumerate(rooms):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f'<div class="room-card"><h4>{room["name"]}</h4></div>', unsafe_allow_html=True)
