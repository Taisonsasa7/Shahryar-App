# throne_engine.py - النسخة النهائية الفائقة السرعة
import asyncio
from chair_registry import get_throne_data

class ThroneEngine:
    def _init_(self, chair_id):
        self.chair_id = chair_id
        self.data = get_throne_data(chair_id)
        self.state = "idle"

    # دالة الاستجابة الفورية (بدون أي تأخير)
    async def on_payment_success_instant(self, receiver_id):
        """يتم استدعاؤها من الكاشير فور إتمام الدفع"""
        # تنفيذ المهمة في خلفية النظام فوراً
        asyncio.create_task(self.perform_gift_animation_instant(receiver_id))

    async def perform_gift_animation_instant(self, receiver_id):
        """تنفيذ الحركة البصرية للهدية"""
        self.state = "gift_mode"
        print(f"[{self.data['name']}] يطلق الهدية لـ {receiver_id} فوراً!")
        self.deliver_gift(receiver_id)
        self.state = "idle"

    def deliver_gift(self, receiver_id):
        """توزيع الهدايا بناءً على الكائن"""
        effect = self.data['gift_effect']
        print(f"التنفيذ البصري: {effect} موجهة نحو {receiver_id}")

    def natural_movement(self):
        """الحركة التلقائية في الغرفة"""
        if self.state == "idle":
            print(f"{self.data['name']} يتحرك بشكل طبيعي..
# تحديث داخل throne_engine.py

def natural_movement(self):
    entity = self.data['entity_type']
    if entity == "dragon":
        print(f"{self.data['name']} يطير في أرجاء الغرفة.")
    elif entity == "elephant":
        print(f"{self.data['name']} يتمشى بخطوات ثقيلة.")
    elif entity == "peacock":
        print(f"{self.data['name']} يستعرض جمال ريشه.")
    elif entity == "lion":
        print(f"{self.data['name']} يزأر ويتمشى بهيبة.")

def deliver_gift(self, receiver_id):
    # هنا يتم توزيع الهدايا بناءً على الكائن
    # سيعرف النظام تلقائياً الكائن من الـ data['entity_type']
    print(f"يقوم {self.data['name']} بتوزيع الهدية لـ {receiver_id} بطريقته الخاصة!")
