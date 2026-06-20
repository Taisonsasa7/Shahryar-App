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

