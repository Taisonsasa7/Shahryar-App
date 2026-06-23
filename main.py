import streamlit as st

# تعريف الأدمنية (يمكنك تعديل هذه القائمة)
ADMINS = ["admin1", "admin2", "admin3"] 

if 'mics' not in st.session_state:
    st.session_state.mics = [None] * 25 # 25 مايك
    st.session_state.current_user = "user1" # محاكاة للمستخدم الحالي

st.title("🎙️ منصة شهريار المفتوحة")

# منطقة المايكات (أي شخص يمكنه الضغط والصعود)
st.subheader("🎤 منصة المايكات")
cols = st.columns(5)
for i in range(25):
    with cols[i % 5]:
        if st.session_state.mics[i] is None:
            if st.button(f"مايك {i+1} (متاح)", key=f"join_{i}"):
                st.session_state.mics[i] = st.session_state.current_user
                st.rerun()
        else:
            # عرض اسم الشخص الذي على المايك
            st.success(f"🎙️ {st.session_state.mics[i]}")
            # التحكم: يظهر فقط للأدمن أو صاحب المايك نفسه
            if st.session_state.current_user in ADMINS or st.session_state.mics[i] == st.session_state.current_user:
                if st.button("إنزال المايك", key=f"kick_{i}"):
                    st.session_state.mics[i] = None
                    st.rerun()

# منطقة التحكم (للأدمنية فقط)
if st.session_state.current_user in ADMINS:
    with st.expander("🛡️ لوحة تحكم الأدمن"):
        st.write("يمكنك كتم أي مايك أو طرد أي مستخدم من الغرفة.")
        st.button("كتم الجميع")
