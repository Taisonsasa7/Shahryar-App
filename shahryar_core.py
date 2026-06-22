class ShahryarCore:
    def _init_(self):
        # تعريف الغرف كقائمة من القواميس تحتوي على الاسم فقط
        self.rooms = [{"name": "غرفة الألعاب"}, {"name": "غرفة الموسيقى"}]
    
    def get_all_rooms(self):
        return self.rooms

    def calculate_money(self, amount):
        # عملية حسابية بسيطة
        return {
            "إجمالي": amount,
            "حصة الإدارة": amount * 0.60,
            "حصة المضيف": amount * 0.30
        }

# إنشاء الكائن الموحد
shahryar_system = ShahryarCore()
