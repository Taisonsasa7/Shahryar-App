import streamlit as st
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))
from gifts_system.gifts_db import gifts
from avatar_system.clothing_db import arab_heritage_wardrobe
from avatar_system.animation_controller import AnimationController

if 'avatar' not in st.session_state:
    st.session_state.avatar = AnimationController("الأفاتار")

st.title("🎤 الغرفة التفاعلية - نظام الخصوصية")

# اختيار المايك للهمس
target_mic = st.selectbox("اختر المايك للذهاب إليه:", [f"مايك {i}" for i in range(1, 26)])

if st.button("التحرك للهمس"):
    # 1. تنفيذ المشي
    mic_number = int(target_mic.split()[1])
    path = st.session_state.avatar.walk_to_mic(mic_number)
    
    for step in path:
        st.write(f"🚶 {step}")
        time.sleep(0.5) # وقت المشي الواقعي
    
    # 2. تفعيل وضع الهمس بعد الوصول
    st.session_state.avatar.whisper_mode()
    st.success("لقد وصلت! حالة الخصوصية مفعلة الآن.")
    
    # 3. التأخير الزمني قبل "فتح الصوت"
    with st.spinner("جاري الاستعداد للكلام..."):
        time.sleep(2) # ينتظر المستخدم ثواني
        st.info("تم كتم الصوت عن الآخرين، أنت الآن في وضع الهمس.")

else:
    # الحركة الطبيعية
    action = st.session_state.avatar.get_random_natural_action()
    st.write(f"الحالة الطبيعية: الأفاتار يقوم بـ {action}")
