# استيراد الإعدادات من ملف config.py
from config import ADMIN_SHARE, AGENT_SHARE, HOST_SHARE

def process_server_logic(amount):
    # استخدام النسب المحددة في ملف الإعدادات
    distribution = {
        'admin': amount * ADMIN_SHARE,
        'agent': amount * AGENT_SHARE,
        'host': amount * HOST_SHARE
    }
    return distribution

print("Shahryar Core Engine Connected to Config")
