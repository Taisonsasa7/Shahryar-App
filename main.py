import streamlit as st

# 1. إعداد التصميم (الأسود الملكي، الذهبي، والبنفسجي)
st.markdown("""
    <style>
    .stApp { background-color: #0d0d0d; color: #ffffff; }
    .room-card {
        background-color: #1a1a1a;
        border: 2px solid #FFD700;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        text-align: center;
    }
    h1 { color: #FFD700 !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. النظام الأساسي (ShahryarCore & Economy)
class ShahryarSystem:
    def _init_(self):
        self.rooms = {
            "غرفة البث المباشر": "🔴",
            "غرفة الدردشة الصوتية": "🎙️",
            "غرفة الألعاب": "🎮"
        }
        self.EXCHANGE_RATE = 100  # معدل تحويل الماس

    def trigger_event(self, amount):
        # حساب الحصص: الإدارة (60%)، المضيف (40%)
        return amount * 0.6, amount * 0.4

system = ShahryarSystem()

# 3. واجهة التطبيق الكاملة
st.title("🌙 شهريار")

# عرض الغرف
col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

for i, (name, icon) in enumerate(system.rooms.items()):
    with cols[i]:
        st.markdown(f"""
        <div class="room-card">
            <h1>{icon}</h1>
            <h3>{name}</h3>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# 4. النظام المالي
st.subheader("💰 لوحة التحكم المالية")
val = st.number_input("أدخل كمية الماس:", min_value=0)
if st.button("توزيع الأرباح"):
    admin, host = system.trigger_event(val)
    st.success(f"حصة الإدارة: {admin:.2f}")
    st.success(f"حصة المضيف: {host:.2f}")
