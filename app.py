import streamlit as st
import google.generativeai as genai
from audio_recorder_streamlit import audio_recorder

# 1. إعداد الـ API
genai.configure(api_key="ضع_مفتاحك_هنا")
model = genai.GenerativeModel('gemini-pro')

st.title("غرفة الذكاء الاصطناعي - 1001 شهرزاد")

# 2. تسجيل الصوت
audio_bytes = audio_recorder("اضغط للتحدث")

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")
    # هنا سنقوم لاحقاً بإضافة دالة تحويل الصوت إلى نص (STT)
    st.write("تم استلام الصوت... جاري المعالجة")
    
    # 3. الرد الذكي
    response = model.generate_content("أجب على المستخدم كأنك مساعد خبير")
    st.write(response.text)
