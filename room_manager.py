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
import json
import os

# ... داخل class RoomManager ...

    def save_room_state(self):
        """حفظ حالة الغرفة في ملف"""
        data = {
            "active_thrones": {uid: throne.data for uid, throne in self.active_thrones.items()},
            "muted_users": list(self.muted_users)
        }
        with open("room_data.json", "w") as f:
            json.dump(data, f)
        print("تم حفظ حالة الغرفة بنجاح.")

    def load_room_state(self):
        """استعادة حالة الغرفة عند التشغيل"""
        if os.path.exists("room_data.json"):
            with open("room_data.json", "r") as f:
                data = json.load(f)
                # هنا يمكنك إعادة بناء الـ active_thrones
                self.muted_users = set(data["muted_users"])
            print("تم استعادة بيانات الغرفة من آخر جلسة.")
from assets_manager import AssetsManager

class RoomManager:
    def _init_(self):
        self.assets = AssetsManager()  # ربط المدير بالأصول
        # باقي الإعدادات...

    def get_user_requested_item(self, category, item_id):
        """جلب أي عنصر (وليمة/خلفية) من المخزن الداخلي"""
        path = self.assets.get_asset(category, item_id)
        if path:
            print(f"تم تحميل الأصول بنجاح من: {path}")
            return path
        else:
            print("عذراً، العنصر غير موجود في المخزن الداخلي.")
            return None
class RoyalHospitalitySystem:
    def _init_(self, room_data):
        self.room_data = room_data

    def serve_royal_feast(self, user_id, feast_type):
        # 1. إعداد الهدية مع تأثيرات البخار والحركة
        feast = self.get_feast_assets(feast_type)
        
        # 2. إضافة 10% ضريبة ملكية
        total_price = feast['price'] * 1.10
        
        # 3. "بث" الأكلة في الغرفة (الرندرة البصرية)
        # هذا الأمر يخبر كل المتصلين: "ارسموا الخروف المندي هنا"
        self.render_object_to_room(user_id, feast['asset_path'], effect="steam_animation")
        
        # 4. إعلان الذكاء الاصطناعي (الشيف)
        self.ai_chef_announce(user_id, feast['description'])
        
        return total_price
# في ملف room_manager.py
    def swap_gift(self, user_id, old_item_id, new_item_id):
        """دالة تبديل المشروبات بنفس القيمة"""
        # (هنا سنضيف المنطق الخاص بجلب البيانات ومقارنة الأسعار)
        print(f"جاري تبديل {old_item_id} بـ {new_item_id}...")
        # يمكنك إضافة منطق التحقق من السعر هنا لاحقاً
        return True
def update_guest_order(self, user_id, current_item, new_item):
        """الخادم الذكي يغير الطلب بنفس القيمة"""
        # 1. التحقق من تطابق الأسعار
        if self.assets.get_price(current_item) == self.assets.get_price(new_item):
            # 2. تغيير الشكل (Rendering)
            self.remove_from_room(user_id, current_item)
            self.place_in_room(user_id, new_item)
            
            # 3. رد الذكاء الاصطناعي التفاعلي
            print(f"[AI Butler]: أبشر يا سيدي، تم استبدال {current_item} بـ {new_item} فوراً!")
            return True
        else:
            print("[AI Butler]: عذراً، قيمة الطلبات غير متطابقة، يرجى اختيار بديل بنفس السعر.")
            return False
