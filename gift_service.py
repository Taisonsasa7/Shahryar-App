
# استيراد قاعدة بيانات الهدايا من الملف الذي أنشأناه سابقاً
from assets_manager import LEGENDARY_GIFTS

class GiftService:
    def _init_(self):
        # محاكاة بسيطة لقاعدة بيانات أرصدة المستخدمين (يمكنك ربطها بـ SQL أو Firebase لاحقاً)
        self.user_balances = {"user_123": 500000} 

    def purchase_gift(self, user_id, gift_id):
        # 1. التحقق من وجود الهدية
        gift = LEGENDARY_GIFTS.get(gift_id)
        if not gift:
            return {"status": "error", "message": "الهدية غير موجودة في إمبراطورية شهران!"}

        # 2. التحقق من الرصيد
        user_balance = self.user_balances.get(user_id, 0)
        if user_balance < gift['price']:
            return {"status": "error", "message": "رصيدك غير كافٍ يا ملك/ملكة!"}

        # 3. إتمام عملية الشراء
        self.user_balances[user_id] -= gift['price']
        
        # 4. إرجاع التأكيد وتفعيل التأثير
        return {
            "status": "success", 
            "message": f"تم تفعيل {gift['name']} بنجاح!",
            "animation_url": gift['animation_url']
        }

# إنشاء نسخة من الخدمة
gift_system = GiftService()
