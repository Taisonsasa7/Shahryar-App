# throne_engine.py
from chair_registry import get_throne_data
import time

class ThroneEngine:
    def _init_(self, chair_id):
        self.chair_id = chair_id
        self.data = get_throne_data(chair_id)
        
    def activate_showcase(self):
        """تشغيل العرض الأسطوري: الخروج، الطيران، والتفاعل"""
        if not self.data:
            return "الكرسي غير موجود!"
            
        print(f"بدء العرض لـ: {self.data['name']}...")
        
        # 1. حركة الخروج من الخشب
        self.emerge_from_wood()
        
        # 2. الطيران حول الغرفة
        self.orbit_room()
        
        # 3. العودة للكرسي
        self.return_to_chair()
        
        return "تم العرض بنجاح!"

    def emerge_from_wood(self):
        print(f"التنين يخرج من الخشب مع صوت: {self.data['sound_effect']}")
        # هنا سنضيف كود الربط مع المحرك الرسومي (Animation)
        
    def orbit_room(self):
        print(f"الكائن يطير في الغرفة بسرعة {self.data['movement_speed']}...")
        
    def return_to_chair(self):
        print("العودة إلى داخل الخشب بسلام.")

    def deliver_gift(self, receiver_name):
        """نظام توزيع الهدايا بناءً على العنصر"""
        effect = self.data['gift_effect']
        print(f"التنين يوزع الهدية باستخدام: {effect} لـ {receiver_name}"
# throne_engine.py - الكود الكامل المحدث
from chair_registry import get_throne_data

class ThroneEngine:
    def _init_(self, chair_id):
        self.chair_id = chair_id
        self.data = get_throne_data(chair_id)
        self.state = "idle"  # الحالة الافتراضية: خمول طبيعي

    # 1. الذكاء السلوكي (الحركة التلقائية)
    def run_behavior(self):
        """الذكاء الاصطناعي: يقرر ماذا يفعل التنين الآن"""
        if self.state == "idle":
            self.natural_movement_cycle()

    def natural_movement_cycle(self):
        """الحركة التلقائية الطبيعية"""
        print(f"التنين {self.data['name']} يتحرك بحرية في الغرفة ككائن حي.")

    # 2. نظام الهدايا الأسطوري
    def trigger_gift_sequence(self, receiver_name):
        """التحول الفوري من الحركة الطبيعية إلى توزيع الهدايا"""
        self.state = "gift_mode"
        print(f"تفعيل التنين: توزيع هدية لـ {receiver_name} باستخدام {self.data['gift_effect']}")
        
        # استدعاء الحركات المدمجة
        self.emerge_from_wood()
        self.orbit_room()
        
        self.state = "idle" # العودة للوضع الطبيعي

    # 3. الدوال الحركية الأساسية
    def emerge_from_wood(self):
        print(f"خروج من الخشب بصوت: {self.data['sound_effect']}")

    def orbit_room(self):
        print(f"الطيران في الغرفة بسرعة: {self.data['movement_speed']}")

    def return_to_chair(self):
        print("العودة إلى داخل الخشب بسلام.")
