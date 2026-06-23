# 1. تهيئة قائمة الداعمين في ذاكرة التطبيق
if 'supporters' not in st.session_state:
    st.session_state.supporters = {"Shahryar": 1000, "User_X": 800, "User_Y": 600} # أمثلة أولية

# دالة لإضافة دعم
def add_support(username, points):
    if username in st.session_state.supporters:
        st.session_state.supporters[username] += points
    else:
        st.session_state.supporters[username] = points

# 2. إضافة لوحة الصدارة في الـ Sidebar
with st.sidebar:
    st.divider()
    st.header("🏆 قائمة كبار الداعمين")
    # ترتيب الداعمين حسب النقاط وعرض أول 10
    sorted_supporters = sorted(st.session_state.supporters.items(), key=lambda x: x[1], reverse=True)
    
    for i, (name, score) in enumerate(sorted_supporters[:10]):
        medal = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else f"{i+1}."
        st.write(f"{medal} *{name}*: {score} نقطة")

# 3. زر إرسال هدية (في واجهة المستخدم)
st.subheader("🎁 إرسال دعم للغرفة")
if st.button("إرسال هدية (100 ماسة)"):
    if st.session_state.diamonds >= 100:
        st.session_state.diamonds -= 100
        add_support("أنت", 100) # هنا يوضع اسم المستخدم الحالي
        st.success("تم إرسال الهدية بنجاح!")
        st.rerun()
    else:
        st.error("رصيدك غير كافٍ!")
