class ShahryarCore:
    def _init_(self):
        self.rooms = [{"name": "غرفة تجريبية"}]
    
    def get_all_rooms(self):
        return self.rooms

# إنشاء الكائن
shahryar_system = ShahryarCore()
