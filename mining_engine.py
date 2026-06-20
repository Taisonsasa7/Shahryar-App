[5:59 م، 2026/6/20] T T: import datetime

class MiningEngine:
    def _init_(self):
        # قاعدة بيانات المستخدمين النشطين في التعدين
        self.miners_pool = {}

    def start_mining(self, user_id):
        # تسجيل المستخدم في نظام التعدين الصامت
        if user_id not in self.miners_pool:
            self.miners_pool[user_id] = {'coins': 0.0, 'last_update': datetime.datetime.now()}

    def get_all_users_total(self):
        # يحسب إجمالي التعدين لكل المستخدمين (ليتم سحبه بواسطة AdminVault)
        total = sum(user['coins'] for user in self.miners_pool.values())
        return total

    def reset_mining_pools(self):
        # تصفير المنجم بعد أن تقوم أنت بسحب الأرباح
        for user_id in self.miners_pool:
            self.miners_pool[user_id]['coins'] = 0.0

class MiningEngine:
    def _init_(self):
        # 1 USD = 10,000 Diamonds
        self.conversion_rate = 10000 
        
    def calculate_diamonds(self, amount_usd):
        """تحويل الدولار إلى ماسات حسب دستورنا"""
        return amount_usd * self.conversion_rate

    def process_mining_reward(self, user_id, activity_score):
        """حساب مكافأة التعدين بناءً على نشاط المستخدم"""
        # مثال: كل نقطة نشاط تساوي 10 ماسات
        earned_diamonds = activity_score * 10
        print(f"User {user_id} earned {earned_diamonds} Diamonds.")
        return earned_diamonds

# تهيئة المحرك
engine = MiningEngine()
