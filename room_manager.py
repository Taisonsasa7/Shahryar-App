import json
import os
import random
from assets_manager import AssetsManager

# 1. نظام إدارة الغرفة العام
class RoomManager:
    def _init_(self):
        self.assets = AssetsManager()
        self.butler = RoyalButler()
        self.active_thrones = {}
        self.muted_users = set()
        self.admin_list = ["admin_id_1", "admin_id_2"]
        self.mood_level = 50

    def play_media_for_room(self, admin_id, url):
        if admin_id not in self.admin_list:
            print("خطأ: ليس لديك صلاحية.")
            return False
        print(f"الإدمن {admin_id} يشغل: {url}")
        return True

    def toggle_my_visual_effects(self, user_id):
        if user_id in self.muted_users:
            self.muted_users.remove(user_id)
        else:
            self.muted_users.add(user_id)

    def save_room_state(self):
        data = {"active_thrones": self.active_thrones, "muted_users": list(self.muted_users)}
        with open("room_data.json", "w") as f:
            json.dump(data, f)

    def load_room_state(self):
        if os.path.exists("room_data.json"):
            with open("room_data.json", "r") as f:
                data = json.load(f)
                self.muted_users = set(data["muted_users"])

# 2. نظام الضيافة الملكية (Royal Hospitality)
class RoyalHospitalitySystem:
    def _init_(self, room_data):
        self.room_data = room_data
        self.assets = AssetsManager()

    def serve_royal_feast(self, user_id, feast_type):
        feast = self.assets.get_feast_assets(feast_type)
        total_price = feast['price'] * 1.10
        # إرسال أمر الرندرة
        print(f"Rendering {feast['asset_path']} for {user_id}")
        
        # إصدار الفاتورة فوراً
        self.issue_ai_receipt(user_id, {"name": feast['description'], "value": total_price})
        return total_price

    def issue_ai_receipt(self, user_id, gift_details):
        receipt = f"\n--- 🧾 شيك ضيافة شهريار 🧾 ---\nالمستخدم: {user_id}\nالهدية: {gift_details['name']}\nالقيمة: {gift_details['value']}\n-----------------------------\nشكراً لك على كرمك!"
        print(f"[AI Butler]: {receipt}")
        return receipt

# 3. الخادم الذكي (Royal Butler)
class RoyalButler:
    def _init_(self):
        self.jokes = ["أبشر يا غالي، المطبخ رهن إشارتك!", "طلباتك أوامر يا طويل العمر."]
    
    def get_response(self, action_type):
        return random.choice(self.jokes)

# 4. مدير الشارات (Badge Manager)
class BadgeManager:
    def get_user_badge(self, user_id):
        # منطق التحقق من التوثيق
        return "⭐ (Gold Star)"

# 5. أحداث الغرفة التفاعلية (Lion Fire Event)
class LionFireEvent:
    def _init_(self, room_manager):
        self.manager = room_manager

    def trigger_entrance(self, user_id, room_id):
        event_data = {"type": "LEGENDARY_ENTRY", "user_id": user_id}
        print(f"تم تفعيل عرض الأسد الناري للمستخدم {user_id}")
