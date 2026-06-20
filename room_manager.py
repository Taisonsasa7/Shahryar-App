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
import random

class RoyalButler:
    def _init_(self):
        self.jokes = [
            "أبشر يا غالي، المطبخ رهن إشارتك! بس لا تطلب شي مو موجود في الفئة حقته، خلك ملك!",
            "تبي تغير؟ تدلل! بس تذكر.. اللي يطلب رخيص وهو كاش، يزعل الشيف شهريار!",
            "يا هلا والله، المطبخ من المحيط للخليج تحت أمرك.. وش ودك تذوق الحين؟",
            "طلباتك أوامر يا طويل العمر، بس لا تكثر من الحلا، ودنا نحافظ على الرشاقة!"
        ]

    def get_response(self, action_type, success=True):
        if not success:
            return "يا خوي، ما يصح كذا! تبديل بنفس القيمة.. لا تكسر اقتصاد المجلس!"
        return random.choice(self.jokes)
# في ملف room_manager.py
def execute_order(self, user_id, action, item_name):
    # المنطق البرمجي للتبديل...
    # بعد التنفيذ مباشرة:
    response = self.butler.get_response("swap", success=True)
    self.send_chat_to_room(f"شيف شهريار: {response}")
def accept_tip(self, user_id, amount):
        """نظام الإكرامية للخادم الذكي"""
        if amount > 0:
            print(f"[AI Butler]: الله يبارك فيك يا راعي الكرم! {amount} لمسة وصلت، تسلم إيدك!")
            # هنا سنضيف لاحقاً كود يضيف الإكرامية لرصيد البوت أو لزيادة "مستوى البوت"
            return True
        return False
import random
from assets_manager import AssetsManager

class RoyalButler:
    def _init_(self):
        self.greetings = {
            "Saudi": ["يا هلا ومرحبا يا طويل العمر،", "أبشر بعزك،"],
            "Morocco": ["مرحبا بك أسي،", "على الراس والعين يا غالي،"],
            "Egypt": ["يا باشا نورتنا،", "من عنيا الاتنين يا برنس،"]
        }

    def get_response(self, region):
        return random.choice(self.greetings.get(region, ["أهلاً بك،"]))

class RoomManager:
    def _init_(self):
        self.assets = AssetsManager()
        self.butler = RoyalButler()
        self.mood_level = 50

    def swap_item(self, user_id, user_region, current_item, new_item):
        if self.assets.can_swap(current_item, new_item):
            greeting = self.butler.get_response(user_region)
            print(f"[AI Butler]: {greeting} تم تبديل {current_item} بـ {new_item}!")
            return True
        else:
            print("[AI Butler]: عذراً يا غالي، القيم غير متطابقة، لا يمكن التبديل!")
            return False

    def process_tip(self, amount):
        self.mood_level += amount
        print(f"[AI Butler]: الله يبارك فيك! ارتفعت معنوياتي، مزاجي الآن {self.mood_level}%!")
class BadgeManager:
    def get_user_badge(self, user_id):
        user = self.get_user(user_id)
        
        if user['pi_verified']: # موثق عبر Pi Browser
            return "⭐ (Gold Star)"
        elif user['id_card_verified']: # موثق بالبطاقة محلياً
            return "🟢 (Green Star)"
        else:
            return "No Status"

    def upgrade_to_gold(self, user_id):
        # عندما يتأكد النظام أن المستخدم وصله توثيق Pi
        user = self.get_user(user_id)
        user['pi_verified'] = True
        user['badge'] = "GOLD_STAR
def play_entry_animation(self, user_id, gift_id):
    if gift_id == "lion_fire_entry":
        # 1. إرسال أمر لكل المستخدمين في الغرفة بتشغيل الأنيميشن
        self.broadcast_to_room("SCREEN_SHAKE", duration=2)
        self.broadcast_to_room("PLAY_FIRE_LION_ANIMATION", asset="lion_fire_spawn")
        
        # 2. رسالة ترحيبية في الشات
        self.send_chat_message(f"--- الملك {user_id} دخل الغرفة على ظهر الأسد الناري! ---")
