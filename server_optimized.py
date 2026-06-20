
# استيراد الإعدادات من ملف config.py
from config import ADMIN_SHARE, AGENT_SHARE, HOST_SHARE
# استيراد وظيفة حفظ العمليات من ملف database.py
from database import save_transaction

def process_server_logic(amount, transaction_id):
    # حساب الأرباح بناءً على النسب
    distribution = {
        'admin': amount * ADMIN_SHARE,
        'agent': amount * AGENT_SHARE,
        'host': amount * HOST_SHARE
    }
    
    # حفظ العملية في قاعدة البيانات تلقائياً
    save_transaction(transaction_id, distribution)
    
    return distribution

print("Shahryar Core Engine Connected to Config and Database")\


