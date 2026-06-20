# room_manager.py - المحدث للتحكم بالصلاحيات

class RoomManager:
    def _init_(self):
        self.active_thrones = {}
        self.muted_users = set()  # قائمة المستخدمين الذين كتموا المؤثرات البصرية
        self.admin_list = ["admin_id_1", "admin_id_2"] # قائمة الإدمنية

    # --- صلاحيات الإدارة فقط (Media Control) ---
    def play_media_for_room(self, admin_id, url):
        if admin_id not in self.admin_list:
            print("خطأ: ليس لديك صلاحية تشغيل الوسائط.")
            return False
        
        # فلترة المحتوى
        blocked = ["porn", "xxx", "adult"]
        if any(word in url.lower() for word in blocked):
            print("تحذير: محتوى غير مسموح به.")
            return False
        
        print(f"الإدمن {admin_id} قام بتشغيل: {url}")
        self.activate_noise_cancellation()
        return True

    # --- صلاحيات عامة (للمستخدمين العاديين) ---
    def toggle_my_visual_effects(self, user_id):
        """أي مستخدم يستطيع كتم المؤثرات البصرية لنفسه فقط"""
        if user_id in self.muted_users:
            self.muted_users.remove(user_id)
            print(f"المستخدم {user_id}: تم تفعيل المؤثرات البصرية.")
        else:
            self.muted_users.add(user_id)
            print(f"المستخدم {user_id}: تم كتم المؤثرات البصرية.")

    def activate_noise_cancellation(self):
        print("نظام عزل الصوت نشط للغرفة بالكامل.")
def activate_noise_cancellation(self):
        """تفعيل عزل الصوت"""
        print("نظام عزل الصوت نشط للغرفة بالكامل.")
