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
