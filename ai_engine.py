

import google.generativeai as genai
from data_store import db

# تهيئة الذكاء الاصطناعي
genai.configure(api_key="YOUR_API_KEY")

class AIEngine:
    def _init_(self):
        self.db = db
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def process_intelligence(self, user_id, message, room_id):
        prompt = f"المستخدم {user_id} في الغرفة {room_id} يقول: '{message}'. رد عليه بذكاء وبنفس لهجته."
        try:
            response = self.model.generate_content(prompt)
            ai_reply = response.text
        except Exception:
            ai_reply = "مساعد شهريار في وضع صيانة حالياً."
        
        self._save_to_history(user_id, message, ai_reply)
        return ai_reply

    def handle_gift_event(self, gift_name, sender_name):
        gifts = {
            "الملاك المحارب": f"يا إلهي! {sender_name} استدعى حارس العرش السماوي.. النور يغمر الغرفة!",
            "الجيش السماوي": f"انتباه! {sender_name} أرسل فيلق النور العظيم.. المدد وصل!",
            "الأسد الذهبي الناري": f"اسمعوا الزئير! {sender_name} أطلق سلطان العصر الذهبي.. الأرض تهتز!"
        }
        reply = gifts.get(gift_name, f"{sender_name} قدم هدية: {gift_name}!")
        self._save_to_history("SYSTEM", "GIFT", reply)
        return reply

    def _save_to_history(self, user, msg, reply):
        history = self.db.get_data().get('chat_history', [])
        history.append({"user": user, "msg": msg, "reply": reply})
        self.db.save_data("chat_history", history)

ai_brain = AIEngine()
