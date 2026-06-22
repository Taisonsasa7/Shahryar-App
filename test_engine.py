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
# --- كود الاختبار (أضفه في نهاية الملف) ---
if _name_ == "_main_":
    # محاكاة لكرسي برقم 01
    throne = ThroneEngine(chair_id="throne_01")
    
    print("--- بدء محاكاة حركة العرش ---")
    throne.run_behavior() # تجربة الحركة الطبيعية
    
    print("\n--- محاكاة وصول هدية ---")
    throne.trigger_gift_sequence(receiver_name="المستخدم_شهريار")
