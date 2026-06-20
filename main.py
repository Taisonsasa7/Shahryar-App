
 1. الاستيرادات (في أعلى الصفحة)
from room_manager import RoomManager
from mining_engine import MiningEngine
from admin_panel import AdminVault
from assets_manager import AssetsManager  # <--- هنا نضيف ملف الهدايا الجديد

# 2. التهيئة (تجهيز الأدوات)
manager = RoomManager()
miner = MiningEngine()
vault = AdminVault()
store = AssetsManager()  # <--- تجهيز المتجر

# 3. التشغيل (المنطق)
# هنا تضع الأوامر التي تريد تشغيلها عند فتح التطبيق
miner.start_mining("user_01")
manager.suggest_menu("Morocco")
vault.collect_earnings(miner)

