import json
import os
import gspread
from google.oauth2.service_account import Credentials

class MasterEngine:
    def _init_(self):
        # الإعدادات الموحدة
        self.config = {"NAME": "Shahryar App", "CURRENCY_RATE": 10000, "ADMIN": 0.6, "AGENT": 0.1, "HOST": 0.3}
        self.db_file = "shahryar_db.json"
        self._init_db()
        
        # مكتبة الألعاب المدمجة (تم دمجها هنا لمنع التشتت)
        self.games = {
            "pubg": {"type": "external", "url": "https://www.pubgmobile.com/play"},
            "ludo": {"type": "internal", "src": "https://games.example.com/ludo"}
        }

    def _init_db(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, 'w') as f:
                json.dump({"users": {}, "rooms": {}, "transactions": []}, f)

    # وظائف المحاسبة
    def calculate_share(self, amount):
        return {
            "admin": amount * self.config["ADMIN"],
            "agent": amount * self.config["AGENT"],
            "host": amount * self.config["HOST"]
        }

    # إدارة الألعاب
    def get_game(self, game_id):
        return self.games.get(game_id, None)

    # إدارة المدفوعات (مكان واحد لكل شيء)
    def process_payment(self, amount, transaction_id):
        # هنا يتم دمج منطق Google Sheets والمدفوعات
        print(f"تمت معالجة العملية {transaction_id} بمبلغ {amount}")
        return True

# تعريف المحرك ليستخدمه النظام بالكامل
master = MasterEngine()
