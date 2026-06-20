from data_store import db
import datetime

class JusticeSystem:
    def _init_(self):
        self.db = db

    def submit_appeal(self, user_id, reason, original_violation_id):
        # إنشاء تذكرة تظلم جديدة
        appeal = {
            "user_id": user_id,
            "reason": reason,
            "violation_id": original_violation_id,
            "status": "pending",  # معلق (بانتظار المراجعة)
            "timestamp": str(datetime.datetime.now())
        }
        
        # حفظ التظلم في قاعدة البيانات
        appeals = self.db.get_data().get('appeals', [])
        appeals.append(appeal)
        self.db.save_data("appeals", appeals)
        
        return "تم استلام تظلمك بنجاح، سيقوم فريقنا بمراجعته خلال 24 ساعة."

# تهيئة نظام العدالة
justice_system = JusticeSystem()
