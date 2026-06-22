class ShahryarCore:
    def _init_(self):
        # هنا قمنا بتعريف الغرف داخل الـ _init_ لضمان أنها موجودة
        self.rooms = [{"name": "غرفة الألعاب"}, {"name": "غرفة الموسيقى"}]
    
    def get_all_rooms(self):
        return self.rooms

# هذا السطر مهم جداً: نقوم بإنشاء نسخة من الكلاس ليتم استيرادها
shahryar_system = ShahryarCore()
