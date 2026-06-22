class ShahryarCore:
    def _init_(self):
        # تعريف الغرف كقائمة بسيطة
        self.rooms = [{"name": "غرفة الألعاب"}, {"name": "غرفة الموسيقى"}]
    
    def get_all_rooms(self):
        # إرجاع القائمة مباشرة
        return self.rooms

    def calculate_money(self, amount):
        return {
            "إجمالي": amount,
            "حصة الإدارة": amount * 0.60,
            "حصة المضيف": amount * 0.30
        }

# إنشاء الكائن لاستخدامه في الملف الآخر
shahryar_system = ShahryarCore()
