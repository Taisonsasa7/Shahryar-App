import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="شهريار", layout="centered")

# CSS للتصميم المظلم (Dark Theme) المطابق للصورة
st.markdown("""
    <style>
    .stApp { background-color: #0e0e0e; color: white; }
    .room-card { 
        background-color: #1a1a1a; border-radius: 15px; padding: 15px; 
        margin-bottom: 15px; border: 1px solid #333;
    }
    </style>
""", unsafe_allow_html=True)

# الجزء التقني: مكون الـ SDK
def pi_auth_component():
    return components.html(
        """
        <script src="https://sdk.minepi.com/pi-sdk.js"></script>
        <button id="pi-btn" style="background: #d63384; border:none; padding:10px 20px; color:white; border-radius:10px;">Sign in with Pi</button>
        <script>
            const Pi = window.Pi;
            Pi.init({ version: "2.0", sandbox: true });
            document.getElementById('pi-btn').onclick = async () => {
                const auth = await Pi.authenticate(["username"]);
                alert("Welcome " + auth.user.username);
            };
        </script>
        """, height=100
    )

# الواجهة الرئيسية
st.title("شهريار")
pi_auth_component() # زر الدخول

st.markdown("---")
st.subheader("الغرف المتاحة")

# توزيع الغرف (كما في الصورة)
col1, col2 = st.columns(2)
rooms = [
    {"name": "غرفة الألعاب", "views": "567", "likes": "312"},
    {"name": "غرفة الموسيقى", "views": "890", "likes": "456"},
    {"name": "دردشة عامة", "views": "123", "likes": "45"},
    {"name": "جلسة راب", "views": "456", "likes": "234"},
]

for i, room in enumerate(rooms):
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"""
        <div class="room-card">
            <h4>{room['name']}</h4>
            <p>👁️ {room['views']} | ❤️ {room['likes']}</p>
        </div>
        """, unsafe_allow_html=True
