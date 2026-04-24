import json
import os

class SaveManager:
    def __init__(self, filename="city_save.json"):
        self.filename = filename

    def save(self, data):
        """يحفظ البيانات (الرصيد، السكان، إلخ) في ملف JSON"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"❌ خطأ أثناء الحفظ: {e}")
            return False

    def load(self):
        """يستعيد البيانات من الملف إذا كان موجوداً"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"❌ خطأ أثناء التحميل: {e}")
                return None
        return None
