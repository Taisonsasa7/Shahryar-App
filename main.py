import json
import os

class ShahryarEconomy:
    def _init_(self):
        self.EXCHANGE_RATE = 10000

    def calculate_distribution(self, amount):
        return {
            "total_diamonds": amount * self.EXCHANGE_RATE,
            "admin": (amount * self.EXCHANGE_RATE) * 0.60,
            "host": (amount * self.EXCHANGE_RATE) * 0.30
        }

class ShahryarCore:
    def _init_(self):
        self.economy = ShahryarEconomy()
        self.rooms = {
            "gaming": "غرفة الألعاب",
            "music": "غرفة الموسيقى",
            "iran_scandal": "فضيحة إيران",
            "throne": "مجلس العرش"
        }

    def get_all_rooms(self):
        # يرجع قائمة الغرف مباشرة
        return [{"id": k, "name": v} for k, v in self.rooms.items()]

    def trigger_event(self, amount):
        return self.economy.calculate_distribution(amount)

# إنشاء الكائن الموحد
shahryar_system = ShahryarCore()
