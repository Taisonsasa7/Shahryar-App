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
class ShahryarEconomy:
    def _init_(self):
        # النسب الثابتة (منع التكرار في أكثر من ملف)
        self.ADMIN_SHARE = 0.60
        self.AGENT_SHARE = 0.10
        self.HOST_SHARE = 0.30
        self.EXCHANGE_RATE = 10000 # 1 USD = 10,000 Diamonds

    def calculate_distribution(self, usd_amount):
        """
        دالة موحدة لحساب توزيع الأرباح. 
        تُستخدم في السيرفر وفي التطبيق لضمان دقة النتائج.
        """
        total_diamonds = usd_amount * self.EXCHANGE_RATE
        
        return {
            "total_diamonds": total_diamonds,
            "admin": total_diamonds * self.ADMIN_SHARE,
            "agent": total_diamonds * self.AGENT_SHARE,
            "host": total_diamonds * self.HOST_SHARE,
            "status": "Finalized - Non-Refundable"
        }

# إنشاء كائن المحرك الاقتصادي لاستخدامه في كامل المشروع
economy_engine = ShahryarEconomy(
