
import random

class AnimationController:
    def _init_(self, name):
        self.name = name
        self.current_state = "idle_natural"
        self.current_mic = 1  # البداية من المايك 1

    def execute_action(self, action):
        self.current_state = action
        return f"الأفاتار يقوم بـ {action}"

    def get_random_natural_action(self):
        # الحركات الطبيعية التي تجعل الأفاتار حياً
        natural_actions = ["idle_natural", "hair_style", "perfume", "dance"]
        return random.choice(natural_actions)

    def walk_to_mic(self, target_mic_number):
        # منطق المشي من المايك الحالي إلى المايك المستهدف
        path = []
        while self.current_mic != target_mic_number:
            if self.current_mic < target_mic_number:
                self.current_mic += 1
            else:
                self.current_mic -= 1
            path.append(f"يمشي إلى مايك {self.current_mic}")
        
        self.current_state = "at_target_mic"
        path.append(f"وصل إلى مايك {target_mic_number}، جاهز للهمس.")
        return path

    def whisper_mode(self):
        # وضعية الهمس (التي طلبتها)
        self.current_state = "whispering"
        return "الأفاتار يميل برأسه ويهمس في الأذن - الخصوصية مفعلة."
