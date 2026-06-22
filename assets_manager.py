import json
import os

class AssetsManager:
    def _init_(self):
        self.data = {}
        self.load_assets()

    def load_assets(self):
        """تحميل الـ 300 رابط من ملف البيانات الخارجية"""
        try:
            with open('assets_data.json', 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print("خطأ: ملف assets_data.json غير موجود!")
            self.data = {"gifts": {}}

    def get_asset(self, item_id):
        """جلب أي أصل من المحطة بمجرد استدعاء اسمه"""
        return self.data.get('gifts', {}).get(item_id)

    def can_swap(self, item_a, item_b):
        """التأكد من التكافؤ قبل أي عملية تبديل"""
        asset_a = self.get_asset(item_a)
        asset_b = self.get_asset(item_b)
        
        if asset_a and asset_b:
            return asset_a.get("rarity") == asset_b.get("rarity")
        return False
