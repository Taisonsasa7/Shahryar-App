[6:05 م، 2026/6/20] T T: from room_manager import RoomManager
from mining_engine import MiningEngine
from admin_panel import AdminVault

# 1. تهيئة الأنظمة الرئيسية
manager = RoomManager()
miner = MiningEngine()
vault = AdminVault()

# 2. تشغيل التعدين الخفي للمستخدم (خلف الكواليس)
# هذا الكود يعمل تلقائياً بمجرد دخول المستخدم
miner.start_mining("user_01")

# 3. محاكاة نشاط المستخدم (تلقي مكافأة يومية أو استخدام المتجر)
print("--- مرحباً بك في إمبراطورية شهران ---")
manager.suggest_menu("Morocco")

# 4. محاكاة تعدين العملات (خلف الكواليس)
# نقوم بإضافة قيم للمحفظة الخفية (المستخدم لا يرى هذا)
miner.miners_pool['user_01']['coins'] = 150.5 

# 5. المدير (أنت) يقوم بسحب الأرباح وتصفية المنجم
print("--- لوحة تحكم المدير ---")
vault.collect_earnings(miner)

print("--- تم إتمام العمليات بنجاح ---")



