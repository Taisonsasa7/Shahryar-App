import json
import os
import random
from datetime import datetime
import google.generativeai as genai
from data_store import db
from game_manager import GameManager
from justice_system import justice_system
from avatar_system.avatar_shop import AvatarShop
from avatar_system.animation_controller import AnimationController

# 1. تهيئة الذكاء الاصطناعي
genai.configure(api_key="YOUR_API_KEY")

class AIEngine:
    def _init_(self):
        self.db = db
        self.model = genai.GenerativeModel('gemini-1.5-pro')
        self.shop = AvatarShop()
        self.avatar = AnimationController("Shahryar_Avatar")

    # --- نظام الذكاء الاصطناعي (معالجة الأوامر) ---
    def process_intelligence(self, user_id, message, room_id):
        prompt = f"المستخدم {user_id} في الغرفة {room_id} يقول: {message}"
        try:
            response = self.model.generate_content(prompt)
            ai_reply = response.text
        except Exception:
            ai_reply = "أنا في وضع صيانة حالياً."
        self._save_to_history(user_id, message, ai_reply)
        return ai_reply

    # --- نظام الهدايا ---
    def handle_gift_event(self, gift_name, sender_name):
        gifts = {
            "الملاك المحارب": f"يا هلا بـ {sender_name}! {gift_name} يضيء الغرفة!",
            "الجيش السماوي": f"وصل جيش {sender_name} الملكي!",
            "الأسد الذهبي الناري": f"الأرض تهتز تحت قدمي {sender_name} والأسد الذهبي الناري!"
        }
        reply = gifts.get(gift_name, f"{sender_name} أهدى هدية: {gift_name}!")
        self._save_to_history("SYSTEM", "GIFT", reply)
        return reply

    # --- نظام الألعاب ---
    def process_game_command(self, user_id, game_id):
        gm = GameManager()
        result = gm.generate_game_view(game_id)
        if result["action"] == "REDIRECT":
            return f"تم تحويلك للعبة: {result['url']}"
        return f"جارٍ تشغيل {game_id} داخل الغرفة..."

    # --- نظام العدالة ---
    def handle_user_appeal(self, user_id, reason, violation_id):
        return justice_system.submit_appeal(user_id, reason, violation_id)

    # --- نظام المتجر والحركات ---
    def process_clothing_purchase(self, user_id, item_category, user_current_balance):
        result = self.shop.purchase_item(user_current_balance, item_category)
        if result["status"] == "success":
            return f"تم شراء {item_category} بنجاح، رصيدك المتبقي: {result['remaining']}"
        return "عذراً، رصيدك لا يكفي."

    def handle_user_action(self, user_id, action_type, user_balance, mic_id=None):
        if action_type in ["shisha", "dance", "perfume", "hair_style"]:
            return self.avatar.execute_action(action_type)
        elif action_type == "move_to_mic":
            return self.avatar.navigate_to_mic(mic_id)
        return "طلب غير مفهوم"

    # --- إدارة التاريخ ---
    def _save_to_history(self, user, msg, reply):
        history = self.db.get_data().get('chat_history', [])
        history.append({"user": user, "msg": msg, "reply": reply})
        self.db.save_data("chat_history", history)

# --- نظام إدارة الفواتير (Gifts Manager) ---
class GiftsManager:
    def _init_(self):
        self.current_invoice = []

    def add_gift(self, receiver_mic, gift_name, value):
        self.current_invoice.append({'mic': receiver_mic, 'gift': gift_name, 'value': value})
        return self.get_formatted_invoice()

    def get_formatted_invoice(self):
        total = sum(item['value'] for item in self.current_invoice)
        invoice_text = "\n--- فاتورة كرمك ---\n"
        for i, entry in enumerate(self.current_invoice, 1):
            invoice_text += f"{i}. {entry['mic']}: {entry['gift']} ({entry['value']})\n"
        invoice_text += f"----------------\nإجمالي الكرم: {total}"
        return invoice_text

    def clear_invoice(self):
        self.current_invoice = []
