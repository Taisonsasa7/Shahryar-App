import json
import os
import streamlit as st

class ShahryarCore:
    def _init_(self, db_file="shahryar_data.json"):
        self.db_file = db_file
        self._init_db()
        
        # مكتبة الألعاب والعروش المدمجة
        self.games = {
            "gaming": {"name": "غرفة الألعاب", "type": "internal"},
            "music": {"name": "غرفة الموسيقى", "type": "internal"}
        }
        self.thrones = {
            "dragon_fire": {"name": "عرش التنين الناري", "element": "fire"},
            "dragon_ice": {"name": "عرش التنين الثلجي", "element": "ice"}
        }

    def _init_db(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, 'w') as f:
                json.dump({"users": {}, "appeals": [], "balances": {}}, f)

    # --- إدارة الشكاوى ---
    def submit_appeal(self, user_id, reason):
        with open(self.db_file, 'r+') as f:
            data = json.load(f)
            data["appeals"].append({"user": user_id, "reason": reason, "status": "pending"})
            f.seek(0)
            json.dump(data, f, indent=4)
        return True

    # --- إدارة الألعاب ---
    def get_all_rooms(self):
        return [{"id": k, "name": v["name"]} for k, v in self.games.items()]

    # --- إدارة الهدايا ---
    def purchase_gift(self, user_id, gift_price):
        # منطق الشراء المدمج
        return {"status": "success", "message": "تم الخصم"}

# إنشاء المحرك ليكون متاحاً للمشروع كله
core = ShahryarCore()
