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
class AssetsManager:
    def _init_(self):
        # هنا قمنا بتوزيع المشروبات والأكلات إلى "فئات سعرية"
        self.tiers = {
            "tier_1_drinks": ["saudi_gahwa", "moroccan_tea", "egyptian_karkade", "espresso"],
            "tier_2_snacks": ["koshary", "refissa", "mansaf_cup", "samosa"],
            "tier_3_feasts": ["royal_lamb", "stuffed_camel", "large_kabsa"]
        }
        
        # وصف الخصائص (هنا سنضع المسارات والتأثيرات لاحقاً)
        self.registry = {
            "saudi_gahwa": {"price_tier": "tier_1", "effect": "coffee_steam"},
            "moroccan_tea": {"price_tier": "tier_1", "effect": "mint_steam"},
            "koshary": {"price_tier": "tier_2", "effect": "hot_steam"},
            "refissa": {"price_tier": "tier_2", "effect": "rich_aroma"}
        }

    def can_swap(self, item_a, item_b):
        """الخادم الذكي يتأكد إذا كان التبديل مسموحاً"""
        tier_a = self.registry.get(item_a, {}).get("price_tier")
        tier_b = self.registry.get(item_b, {}).get("price_tier")
        return tier_a == tier_b and tier_a is not Non
import random

class AssetsManager:
    def _init_(self):
        # قاعدة بيانات المشروبات والأكلات بالفئات
        self.registry = {
            "saudi_gahwa": {"price_tier": "tier_1", "region": "Saudi"},
            "moroccan_tea": {"price_tier": "tier_1", "region": "Morocco"},
            "egyptian_karkade": {"price_tier": "tier_1", "region": "Egypt"},
            "koshary": {"price_tier": "tier_2", "region": "Egypt"},
            "refissa": {"price_tier": "tier_2", "region": "Morocco"}
        }

    def can_swap(self, item_a, item_b):
        tier_a = self.registry.get(item_a, {}).get("price_tier")
        tier_b = self.registry.get(item_b, {}).get("price_tier")
        return tier_a == tier_b and tier_a is not None
class AssetsManager:
    def _init_(self):
        # قاعدة بيانات المشروبات والأكلات بالفئات
        self.registry = {
            "saudi_gahwa": {"price_tier": "tier_1", "region": "Saudi"},
            "moroccan_tea": {"price_tier": "tier_1", "region": "Morocco"},
            "egyptian_karkade": {"price_tier": "tier_1", "region": "Egypt"},
            "koshary": {"price_tier": "tier_2", "region": "Egypt"},
            "refissa": {"price_tier": "tier_2", "region": "Morocco"}
        }

    def can_swap(self, item_a, item_b):
        tier_a = self.registry.get(item_a, {}).get("price_tier")
        tier_b = self.registry.get(item_b, {}).get("price_tier")
        return tier_a == tier_b and tier_a is not Non
