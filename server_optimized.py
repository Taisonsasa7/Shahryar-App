# Shahryar Global System - Core Engine
# المحرك المالي الموحد للتطبيق

def process_server_logic(amount):
    # توزيع الأرباح (60% إدارة / 10% وكلاء / 30% مضيفين)
    distribution = {
        'admin': amount * 0.60,
        'agent': amount * 0.10,
        'host': amount * 0.30
    }
    return distribution

print("Shahryar Core Engine Active"
