class ShahryarCore:
    def _init_(self):
        self.rooms = [{"name": "غرفة الألعاب"}, {"name": "غرفة الموسيقى"}]
    
    def get_all_rooms(self):
        return self.rooms

    def calculate_money(self, amount):
        return {"إجمالي": amount, "حصة الإدارة": amount * 0.60, "حصة المضيف": amount * 0.30}

shahryar_system = ShahryarCore()
