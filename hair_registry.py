# chair_registry.py

# تعريف العروش الأسطورية (The Legendary Elemental Thrones)
ELEMENTAL_THRONES = {
    "dragon_fire": {
        "name": "عرش التنين الناري",
        "element": "fire",
        "colors": ["#FF4500", "#FFD700"],  # أحمر وذهبي
        "gift_effect": "golden_fire_cloud",
        "sound_effect": "dragon_fire_roar.mp3",
        "movement_speed": 1.2
    },
    "dragon_ice": {
        "name": "عرش التنين التلجي",
        "element": "ice",
        "colors": ["#00CED1", "#F0F8FF"],  # أزرق سماوي وأبيض
        "gift_effect": "ice_crystals_burst",
        "sound_effect": "dragon_ice_shatter.mp3",
        "movement_speed": 1.0
    },
    "dragon_volcanic": {
        "name": "عرش التنين البركاني",
        "element": "volcanic",
        "colors": ["#8B0000", "#36454F"],  # أحمر داكن ورمادي صخري
        "gift_effect": "lava_sphere_drop",
        "sound_effect": "dragon_lava_bubble.mp3",
        "movement_speed": 0.8
    },
    "dragon_wrath": {
        "name": "عرش تنين الغضب",
        "element": "wrath",
        "colors": ["#4B0082", "#FFD700"],  # بنفسجي وذهبي
        "gift_effect": "purple_lightning_strike",
        "sound_effect": "dragon_thunder_roar.mp3",
        "movement_speed": 1.5
    }
}

def get_throne_data(chair_id):
    """استرجاع بيانات أي كرسي بناءً على معرفه"""
    return ELEMENTAL_THRONES.get(chair_id, None)

def list_available_thrones():
    """عرض قائمة العروش المتاحة للإدارة أو المتجر"""
    return {k: v['name'] for k, v in ELEMENTAL_THRONES.items()}
