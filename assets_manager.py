class AssetsManager:
    """إدارة الأصول داخل التطبيق (خلفيات، ولائم، هدايا)"""
    def _init_(self):
        # القاموس الداخلي لكل ما يوجد في "متجر شهريار"
        self.registry = {
            "backgrounds": {
                "majlis_royal": {"path": "assets/bg/majlis.png", "price": 1000},
                "desert_tent": {"path": "assets/bg/tent.png", "price": 500}
            },
            "feasts": {
                "royal_lamb": {"path": "assets/food/lamb.png", "price": 2000},
                "stuffed_camel": {"path": "assets/food/camel.png", "price": 5000}
            }
        }

    def get_asset(self, category, item_id):
        """جلب رابط الصورة لأي عنصر من داخل التطبيق"""
        return self.registry.get(category, {}).get(item_id, {}).get("path")
# افتح ملف assets_manager.py واضفه داخل الـ _init_
self.registry['cafe_shahryar'] = {
    "arabian": {
        "saudi_gahwa": {"price": 100, "description": "قهوة سعودية"},
        "moroccan_tea": {"price": 120, "description": "شاي مغربي"},
        "egyptian_karkade": {"price": 80, "description": "كركديه مصري"}
    },
    "international": {
        "italian_espresso": {"price": 150, "description": "إسبريسو إيطالي"},
        "french_latte": {"price": 160, "description": "لاتيه فرنسي"}
    }
}
