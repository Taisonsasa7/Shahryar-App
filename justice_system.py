
import json
import os

class JusticeSystem:
    def _init_(self, db_file="shahryar_data.json"):
        self.db_file = db_file

    def submit_appeal(self, user_id, reason):
        """إضافة شكوى جديدة إلى سجل العدالة"""
        try:
            # التأكد من وجود الملف أولاً
            if not os.path.exists(self.db_file):
                data = {"appeals": []}
            else:
                with open(self.db_file, 'r') as f:
                    data = json.load(f)
            
            # إضافة الشكوى
            new_appeal = {
                "user_id": user_id,
                "reason": reason,
                "status": "pending"
            }
            
            # التأكد من وجود مفتاح الشكاوى
            if "appeals" not in data:
                data["appeals"] = []
                
            data["appeals"].append(new_appeal)
            
            # حفظ الملف
            with open(self.db_file, 'w') as f:
                json.dump(data, f, indent=4)
                
            return {"status": "success", "message": "تم تقديم الشكوى بنجاح"}
            
        except Exception as e:
            return {"status": "error", "message": str(e)}

# إنشاء نسخة لاستخدامها في النظام
justice_system = JusticeSystem
