import json
import os

class ShahryarEconomy:
    def _init(self):  # <--- لاحظ الشرطتين _
        self.ADMIN_SHARE = 0.60
        self.AGENT_SHARE = 0.10
        self.HOST_SHARE = 0.30
        self.EXCHANGE_RATE = 10000

    def calculate_distribution(self, usd_amount):
        total_diamonds = usd_amount * self.EXCHANGE_RATE
        return {
            "total_diamonds": total_diamonds,
            "admin": total_diamonds * self.ADMIN_SHARE,
            "agent": total_diamonds * self.AGENT_SHARE,
            "host": total_diamonds * self.HOST_SHARE
        }

class ShahryarCore:
    def _init(self, db_file="shahryar_data.json"): # <--- لاحظ الشرطتين _
        self.db_file = db_file
        self.economy = ShahryarEconomy()
        self._init_db()
        
        self.rooms = {
            "gaming": {"name": "غرفة الألعاب"},
            "music": {"name": "غرفة الموسيقى"},
            "iran_scandal": {"name": "فضيحة إيران"},
            "throne": {"name": "مجلس العرش"}
        }

    def _init_db(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, 'w') as f:
                json.dump({"appeals": [], "balances": {}}, f)

    def get_all_rooms(self):
        return [{"id": k, "name": v["name"]} for k, v in self.rooms.items()]

    def trigger_event(self, event_type, amount):
        if event_type == "GIFT_RECEIVED":
            return self.economy.calculate_distribution(amount)
        return None

# هذا هو الكائن الموحد للنظام
shahryar_system = ShahryarCore()
