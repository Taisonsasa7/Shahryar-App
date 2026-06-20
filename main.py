from room_manager import RoomManager

# تهيئة النظام
manager = RoomManager()

# تجربة الطلب (تغيير مشروب)
manager.swap_item("user_01", "Saudi", "saudi_gahwa", "moroccan_tea")

# تجربة إعطاء إكرامية
manager.process_tip(20)
# في ملف main.py
manager.swap_item("user_01", "Egypt", "koshary", "refissa")
# في ملف main.py
manager = RoomManager()

# تجربة الاقتراح التلقائي
manager.suggest_menu("Morocco") # جرب تغيير الدولة لـ Saudi أو Egypt
[6:00 م، 2026/6/20] T T: from mining_engine import MiningEngine
from admin_panel import AdminVault

# تشغيل المحرك
miner = MiningEngine()
vault = AdminVault()

# محاكاة: مستخدم عدّن عملات (خلف الكواليس)
miner.miners_pool['user_01'] = {'coins': 150.5} 

# المدير (أنت) يقوم بسحب الأرباح
vault.collect_earnings(miner)

