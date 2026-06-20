

import google.generativeai as genai
from data_store import db

# تفعيل مفتاح الـ API الخاص بك
genai.configure(api_key="YOUR_API_KEY")

class AIEngine:
    def _init_(self):
        self.db = db
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def process_intelligence(self, user_id, message, room_id):
        # 1. صياغة السؤال للمحرك الذكي
        prompt = f"المستخدم {user_id} يسأل في الغرفة {room_id}: {message}. أجب بنفس لهجة المستخدم وكن خبيراً في مجاله."
        
        # 2. الحصول على الرد الفعلي
        response = self.model.generate_content(prompt)
        ai_reply = response.text

        # 3. حفظ المحادثة في الذاكرة (DataStore)
        history = self.db.get_data().get('chat_history', [])
        history.append({"user": user_id, "msg"…
