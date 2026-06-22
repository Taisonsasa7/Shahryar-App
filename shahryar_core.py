class ShahryarCore:
    def _init_(self):
        # تعريف الغرف هنا بوضوح
        self.rooms = [
            {"id": "gaming", "name": "غرفة الألعاب"},
            {"id": "music", "name": "غرفة الموسيقى"}
        ]
    
    def get_all_rooms(self):
        return self.rooms

    def trigger_event(self, amount):
        # حساب بسيط للأرباح
        return {
            "المبلغ": amount,
            "حصة الإدارة": amount * 0.6,
            "حصة المضيف": amount * 0.4
        }

# إنشاء الكائن الموحد
shahryar_system = ShahryarCore()
