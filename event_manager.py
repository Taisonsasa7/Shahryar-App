# event_manager.py
from ai_engine import avatar, shop, gifts

def handle_user_event(user_name, event_type, data):
    """
    event_type: "purchase" أو "gift" أو "action"
    data: قاموس يحتوي على تفاصيل الحدث (مثل نوع الهدية، نوع المتجر)
    """
    if event_type == "gift":
        # 1. تغيير زي الأفاتار حسب نوع متجر الهدية
        avatar.execute_action(f"switch_to_{data['shop_type']}")
        
        # 2. إضافة الهدية للفاتورة
        invoice = gifts.add_gift(data['mic'], data['gift_name'], data['value'])
        
        # 3. إرجاع الرد للذكاء الاصطناعي ليعلنه للمستخدمين
        return f"حدث جديد: {user_name} أرسل {data['gift_name']}! {invoice}"

    elif event_type == "purchase":
        return shop.purchase_item(data['balance'], data['item_id'])
    
    return "Event processed."
# في event_manager.py
def present_final_bill(user_name):
    final_invoice = gifts.get_formatted_invoice(user_name)
    # الذكاء الاصطناعي هنا يقوم بدور "النادل أو مدير المطعم"
    announcement = f"AI Bot: يا {user_name} يا باشا، الشيك بتاعك جاهز! اتفضل الحساب مع رسوم الخدمة، يا رب تكون الخدمة عجبتك!"
    return f"{announcement}\n{final_invoice
