# gifts_system/gifts_manager.py
from gifts_db import gifts

class GiftsManager:
    def send_gift(self, gift_id, user_balance):
        gift = gifts.get(gift_id)
        if not gift:
            return {"status": "error", "message": "الهدية غير موجودة"}
        
        if user_balance >= gift["price"]:
            new_balance = user_balance - gift["price"]
            return {
                "status": "success", 
                "remaining_balance": new_balance, 
                "animation": gift["animation"]
            }
        else:
            return {"status": "error", "message": "رصيدك غير كافٍ"
