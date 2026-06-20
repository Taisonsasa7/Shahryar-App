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
def _init_(self):
        # قاعدة البيانات الموسعة
        self.registry = {
            # مشروبات الفئة الأولى (Tier 1)
            "saudi_gahwa": {"price_tier": "tier_1", "region": "Saudi"},
            "moroccan_tea": {"price_tier": "tier_1", "region": "Morocco"},
            "egyptian_karkade": {"price_tier": "tier_1", "region": "Egypt"},
            "turkish_coffee": {"price_tier": "tier_1", "region": "Global"},
            "moroccan_atay_shiba": {"price_tier": "tier_1", "region": "Morocco"},
            
            # أكلات الفئة الثانية (Tier 2)
            "koshary": {"price_tier": "tier_2", "region": "Egypt"},
            "refissa": {"price_tier": "tier_2", "region": "Morocco"},
            "mansaf_cup": {"price_tier": "tier_2", "region": "Saudi"},
            "tajine": {"price_tier": "tier_2", "region": "Morocco"},
            "molokhia": {"price_tier": "tier_2", "region": "Egypt"},
            
            # ولائم الفئة الثالثة (Tier 3)
            "royal_lamb": {"price_tier": "tier_3", "region": "Global"},
            "mandi_platter": {"price_tier": "tier_3", "region": "Saudi"}
        }
# في ملف assets_manager.py
self.registry.update({
    # متجر شهريار للرومانسية (هدايا)
    "rose_bouquet": {"price_tier": "tier_1", "store": "romantic"},
    "perfume_bottle": {"price_tier": "tier_2", "store": "romantic"},
    "diamond_ring": {"price_tier": "tier_3", "store": "romantic"},
    
    # متجر أباطار (داخليات)
    "premium_cotton_set": {"price_tier": "tier_1", "store": "apparel"},
    "silk_robe": {"price_tier": "tier_2", "store": "apparel"}
})
# أضف هذا إلى قاموس الهدايا الأسطورية
self.legendary_gifts["lion_fire_entry"] = {
    "name": "عرش الأسد الناري",
    "rarity": "Legendary",
    "effect_type": "full_screen_animation",
    "animation_asset": "fire_lion_spawn", # هذا الرابط الذي سيشغل صورتك
    "price": 10000, # سعر ملكي
    "description": "دخول أسطوري لا يراه إلا من امتلك قوة الأسد!"
}
assets_manager.py
# إضافات إمبراطورية الجنيات
            "fairy_piano": {"name": "سيمفونية الجنيات", "price": 12000, "animation": "musical_sparkle_piano", "rarity": "Mythic"},
            "fairy_castle": {"name": "قلعة الأحلام الساحرة", "price": 15000, "animation": "floating_castle_bubbles", "rarity": "Mythic"},
            "fairy_gate": {"name": "بوابة الزهور الأبدية", "price": 11000, "animation": "glowing_floral_portal", "rarity": "Legendary"},
            "fairy_boat": {"name": "رحلة في ضوء القمر", "price": 9000, "animation": "moonlight_boat_glide", "rarity": "Epic"},
            "fairy_fox": {"name": "رفيقة الغابة المتوهجة", "price": 8500, "animation": "glowing_fox_companion", "rarity": "Epic"},
            "fairy_path": {"name": "طريق الجنيات المضيء", "price": 6000, "animation": "flower_path_bloom", "rarity": "Rare"}
# إضافات أسرار الباب المسحور
            "dream_weaver": {"name": "نساج الأحلام الأبدية", "price": 18000, "animation": "star_dust_dreamcatcher", "rarity": "Mythic"},
            "lotus_princess": {"name": "أميرة زهرة اللوتس", "price": 16000, "animation": "lotus_blooming_reveal", "rarity": "Legendary"},
            "forest_guardian": {"name": "حارس الغابة الأبيض", "price": 15000, "animation": "white_stag_magic_aura", "rarity": "Legendary"},
            "enchanted_bridge": {"name": "ممر العوالم المضيئة", "price": 12000, "animation": "glowing_fungi_path", "rarity": "Epic"},
            "fairy_musician": {"name": "عازفة أوتار النجوم", "price": 10000, "animation": "starry_violin_melody", "rarity": "Epic"}
إضافات الملحمة الأسطورية
            "mafhdet_goddess": {"name": "مافديت: صائدة الفوضى", "price": 25000, "animation": "blue_electric_claw_slash", "rarity": "Mythic"},
            "dino_warrior": {"name": "فارس الحقبة المنقرضة", "price": 15000, "animation": "dino_warrior_charge", "rarity": "Legendary"}
# تأثير الدخول الأسطوري المجمع (كما وصفته بالفعل)
            "fairy_lotus_voyage": {
                "name": "رحلة الجنية وشراع اللوتس",
                "price": 30000,  # سعر أعلى لأنه تأثير دخول مجمع ومتحرك بالكامل
                "animation": "fairy_boat_movement_with_blooming_lotus_shara3",
                "rarity": "Mythic",
                "sound": "gentle_water_lapping_with_magical_chimes"
            }
# الهدية الأسطورية الكبرى: مملكة التنانين
            "dragon_dominance_entry": {
                "name": "سيادة تنين الظلام",
                "price": 100,000,  # السعر الأقصى لأنه تأثير ملكي
                "animation": "massive_dragon_summon_with_minions",
                "rarity": "God-Tier",
                "sound": "earth_shaking_dragon_roar"
            }
