import json
import os

class DataStore:
    def _init_(self, filename="shahryar_db.json"):
        self.filename = filename
        # إنشاء الملف إذا لم يكن موجوداً
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump({"users": {}, "rooms": {}, "support_tickets": []}, f)

    def save_data(self, key, value):
        with open(self.filename, 'r+') as f:
            data = json.load(f)
            data[key] = value
            f.seek(0)
            json.dump(data, f, indent=4)

    def get_data(self):
        with open(self.filename, 'r') as f:
            return json.load(f)

