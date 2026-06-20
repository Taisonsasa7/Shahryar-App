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
 هدية الحصان المجنح (هدية البنات المميزة)
            "winged_unicorn_companion": {
                "name": "حصان الضياء السابح",
                "price": 25000, 
                "animation": "unicorn_walking_and_grazing_with_glow",
                "rarity": "Legendary",
                "sound": "magical_chimes_and_nature_sounds"
    # إضافات ملحمة العناصر (المشهد المجمع)
            "elements_saga_entry": {
                "name": "ملحمة العنقاء: صراع العناصر",
                "price": 45000,
                "animation": "phoenix_lion_transformation_sequence",
                "rarity": "Mythic",
                "sound": "epic_fire_and_water_clash_sound"
# الهدية الغامضة: مملكة الأرواح المفقودة
            "lost_spirits_gate": {
                "name": "بوابة الأرواح المفقودة",
                "price": 35000,
                "animation": "dimension_portal_with_ghostly_figures",
                "rarity": "Mythic",
                "sound": "mysterious_whispering_and_chimes"
# إضافات حضور ملكة الذئاب
            "wolf_queen_entry": {
                "name": "حضور ملكة الذئاب",
                "price": 38000,
                "animation": "wolf_queen_aura_pulse",
                "rarity": "Legendary",
                "sound": "wolf_howl_and_mystical_energy_surge"
     الهدية الرومانسية: لقاء الحمامة الملكي
            "royal_dove_romantic_entry": {
                "name": "لقاء الحمامة الملكي",
                "price": 40000,
                "animation": "romantic_dove_walk_and_castle_entry",
                "rarity": "Mythic",
                "sound": "gentle_harp_music_and_dove_cooing"
# الهدية الملكية: ملكة الصقور
            "falcon_queen_aura": {
                "name": "ملكة الصقور: الريش الذهبي",
                "price": 80000,
                "animation": "falcon_flight_with_golden_feathers_trail",
                "rarity": "God-Tier",
                "sound": "majestic_hawk_scream_and_glimmer_sparkle"
            }            }       }            }        }
# الهدية الرومانسية: رفيق الروح الأسطوري
            "soul_companion_romantic": {
                "name": "رفيق الروح الأسطوري",
                "price": 55000,
                "animation": "romantic_walk_with_mystical_companion",
                "rarity": "Mythic",
                "sound": "soft_piano_melody_and_footsteps"
 # الهدية التنافسية: إعلان التحدي الملكي
            "royal_challenge_entry": {
                "name": "إعلان التحدي الملكي",
                "price": 75000,
                "animation": "queen_challenge_gesture_with_aura",
                "rarity": "God-Tier",
                "sound": "cinematic_drums_and_royal_trumpet_flare"
# الهدية الأسطورية: تجلي الأثير السماوي
            "celestial_ether_manifest": {
                "name": "تجلي الأثير السماوي",
                "price": 95000,
                "animation": "celestial_portal_manifestation_aura",
                "rarity": "Divine",
                "sound": "ethereal_cosmic_chimes_and_light_shimmer"
# الهدية الملكية: هالة المحارب الملكي
            "royal_warrior_aura": {
                "name": "هالة المحارب الملكي",
                "price": 85000,
                "animation": "royal_warrior_stance_with_energy_shockwaves",
                "rarity": "Divine",
                "sound": "cinematic_power_surge_and_sharp_metallic_clash"
            }            }            }           }
# الهدية الملحمية: غضب ملكة الظلام
            "dark_queen_wrath": {
                "name": "غضب ملكة الظلام",
                "price": 99000,
                "animation": "dark_queen_transformation_with_red_aura",
                "rarity": "Supreme",
                "sound": "sinister_cackle_and_fire_crackle_magic"
# الهدية الملحمية: عملية الإنقاذ الأسطورية
            "legendary_rescue_operation": {
                "name": "إنقاذ إمبراطورية شهران",
                "price": 150000,
                "animation": "epic_rescue_battle_sequence_full",
                "rarity": "Ultimate",
                "sound": "cinematic_battle_score_and_magical_explosion"
            }
