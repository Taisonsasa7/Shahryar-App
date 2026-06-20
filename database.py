# نظام حفظ العمليات لـ Shahryar App
import json

def save_transaction(transaction_id, details):
    # حفظ تفاصيل العملية في ملف نصي
    filename = "transactions.json"
    try:
        with open(filename, 'a') as f:
            json.dump({transaction_id: details}, f)
            f.write('\n')
        print(f"Transaction {transaction_id} saved successfully.")
    except Exception as e:
        print(f"Error saving transaction: {e}")
