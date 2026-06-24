import gspread
from google.oauth2.service_account import Credentials

# 1. إعداد الاتصال بجدول البيانات (قاعدة البيانات المركزية)
def connect_to_sheet():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = Credentials.from_service_account_file('credentials.json', scopes=scope)
    client = gspread.authorize(creds)
    # هذا هو الرابط الذي قمت بإنشائه وتسميته Shahryar_Data
    sheet = client.open("Shahryar_Data").sheet1
    return sheet

# 2. نظام المحاسبة (نموذج 60/40)
def calculate_and_update(room_id, total_sales):
    management_share = total_sales * 0.60
    host_agent_share = total_sales * 0.40
    agent_commission = total_sales * 0.05
    
    # تحديث البيانات في الجدول
    sheet = connect_to_sheet()
    # البحث عن الغرفة وتحديث المبيعات والنسب
    # (هذا الكود سيتصل بالجدول الذي أنشأته ويحدث الأعمدة)
    print(f"تمت المحاسبة لغرفة {room_id}: الإدارة {management_share}، المضيف {host_agent_share}")
    return True

# 3. دمج بوابة دفع Pi Network (هيكلية أولية)
def process_pi_payment(amount, wallet_address):
    # هنا سيتم الربط بـ Pi SDK لاحقاً لإتمام التحويل
    print(f"جاري تحويل {amount} عملة Pi إلى المحفظة {wallet_address}")
    return "Success"

# تشغيل النظام
if _name_ == "_main_":
    print("نظام شهريار يعمل الآن...")
# دالة لجلب قائمة كل الوكالات
def get_all_agencies():
    sheet = connect_to_sheet()
    agency_sheet = sheet.worksheet("Agencies")
    return agency_sheet.get_all_records()

# دالة لجلب بيانات محفظة وكالة معينة
def get_wallet_by_agency(agency_id):
    sheet = connect_to_sheet()
    wallet_sheet = sheet.worksheet("Wallets")
    records = wallet_sheet.get_all_records()
    for row in records:
        if str(row['agency_id']) == str(agency_id):
            return row
    return None

# دالة لتحديث رصيد المحفظة
def update_wallet_balance(agency_id, new_balance):
    sheet = connect_to_sheet()
    wallet_sheet = sheet.worksheet("Wallets")
    records = wallet_sheet.get_all_records()
    
    # البحث عن الصف وتحديثه
    for i, row in enumerate(records):
        if str(row['agency_id']) == str(agency_id):
            # i + 2 لأن الصف الأول هو العناوين، والترقيم يبدأ من 1
            wallet_sheet.update_cell(i + 2, 3, new_balance) 
            return True
    return False                                                                                                                                                                                                      
