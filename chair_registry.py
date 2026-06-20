# chair_registry.py - المحدث
ELEMENTAL_THRONES = {
    "dragon_fire": {
        "name": "عرش التنين الناري",
        "entity_type": "dragon",
        "gift_effect": "golden_fire_cloud",
        "sound_effect": "dragon_fire_roar.mp3",
        "movement_speed": 1.2
    },
    "elephant_throne": {
        "name": "عرش الفيل العظيم",
        "entity_type": "elephant",
        "gift_effect": "water_splash_gift",
        "sound_effect": "elephant_trumpet.mp3",
        "movement_speed": 0.5
    },
    "peacock_throne": {
        "name": "عرش الطاووس الملكي",
        "entity_type": "peacock",
        "gift_effect": "feather_dance_gift",
        "sound_effect": "peacock_cry.mp3",
        "movement_speed": 0.7
    }
}

def get_throne_data(chair_id):
    return ELEMENTAL_THRONES.get(chair_id, None)
