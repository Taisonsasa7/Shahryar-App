# avatar_system/animation_controller.py

class AnimationController:
    def _init_(self, avatar_name):
        self.avatar_name = avatar_name
        self.current_state = "idle"

    def execute_action(self, action_type):
        """
        يتحكم في الحركات الواقعية: الرقص، الشيشة، العطر، تمشيط الشعر.
        """
        animations = {
            "shisha": "إمساك الشيشة مع حركات تنفس واقعية",
            "perfume": "حركة رش العطر بأسلوب أنيق",
            "hair_style": "تمشيط الشعر بحركة هادئة",
            "dance": "بدء وصلة رقص متناغمة مع الموسيقى",
            "idle_natural": "حركة عشوائية للعين وتلفت طبيعي"
        }
        
        action = animations.get(action_type)
        if action:
            self.current_state = action_type
            return f"[{self.avatar_name}] يقوم الآن بـ: {action}"
        return "حركة غير معروفة"

    def navigate_to_mic(self, mic_id):
        """
        تحريك الأفاتار بسلاسة (دوران 360 درجة) للوصول للمايك.
        """
        return f"الأفاتار يتحرك 360 درجة ويتجه نحو المايك رقم: {mic_id}"

# تفعيل السلوك الطبيعي للشخصية
def setup_natural_behaviors():
    return "تم ضبط نظام العيون التلقائي وحركات الخمول الواق
