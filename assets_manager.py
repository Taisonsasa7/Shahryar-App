import os
from supabase import create_client, Client

class AssetsManager:
    def _init_(self):
        self.data = {"gifts": {}}
        # قم بوضع الرابط والمفتاح الخاصين بمشروعك هنا
  self.url = "https://dpyavcpuhsnwozgayixx.supabase.co"
self.key = "sb_publishable_nzVEMDJq8JgAvbhL2L1NzA_LLd5hN1z"
        self.supabase = create_client(self.url, self.key)
        self.load_assets()

    def load_assets(self):
        """تحميل الهدايا من قاعدة بيانات Supabase"""
        try:
            # جلب البيانات من جدول gifts_catalog
            response = self.supabase.table("gifts_catalog").select("*").execute()
            
            # ترتيب البيانات لتناسب هيكلية تطبيقك
            if response.data:
                self.data["gifts"] = {item['name']: item for item in response.data}
                print("تم تحميل الهدايا بنجاح من قاعدة البيانات!")
            else:
                print("الجدول فارغ.")
        except Exception as e:
            print(f"خطأ في الاتصال بقاعدة البيانات: {e}")

    def get_asset(self, item_id):
        """جلب أي عنصر"""
        return self.data.get("gifts", {}).get(item_id)
 
