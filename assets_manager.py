import json
import os

class AssetsManager:
    def _init_(self):
        self.data = {"gifts": {}}
        self.load_assets()

    def load_assets(self):
        """تحميل الـ 300 رابط من ملف البيانات الخارجية"""
        file_path = 'assets_data.json'
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
            except Exception as e:
                print(f"خطأ في قراءة ملف JSON: {e}")
        else:
            print("تنبيه: ملف assets_data.json غير موجود.")

    def get_asset(self, item_id):
        """جلب بيانات أي عنصر"""
        return self.data.get('gifts', {}).get(item_id)

    def can_swap(self, item_a, item_b):
        """التأكد من التكافؤ قبل أي عملية تبديل"""
        asset_a = self.get_asset(item_a)
        asset_b = self.get_asset(item_b)
        
        if asset_a and asset_b:
            return asset_a.get("rarity") == asset_b.get("rarity")
        return False
