
# throne_engine.py - المحدث
from chair_registry import get_throne_data

class ThroneEngine:
    def _init_(self, chair_id):
        self.chair_id = chair_id
        self.data = get_throne_data(chair_id)

    def natural_movement(self):
        """الحركة التلقائية بناءً على نوع الكائن"""
        entity = self.data['entity_type']
        if entity == "dragon":
            print(f"{self.data['name']} يحلق ويقوم بلفات استعراضية.")
        elif entity == "elephant":
            print(f"{self.data['name']} يتمشى بخطوات ثقيلة في الغرفة.")
        elif entity == "peacock":
            print(f"{self.data['name']} يستعرض ريشه الملون ببطء.")

    def deliver_gift(self, receiver_name):
        """توزيع الهدايا بناءً على الكائن"""
        entity = self.data['entity_type']
        effect = self.data['gift_effect']
        
        if entity == "elephant":
            print(f"الفيل يرفع خرطومه ويقدم الهدية لـ {receiver_name} بـ {effect}")
        elif entity == "dragon":
            print(f"التنين يبخ نيرانه ليشكل الهدية لـ {receiver_name} بـ {effect}")
        else:
            print(f"يقوم {self.data['name']} بتقديم الهدية لـ {receiver_name}"
