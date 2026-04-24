import json
import os
from colors import Colors

class SaveSystem:
    def __init__(self, filename="save_data.json"):
        self.filename = filename

    def save_game(self, game_state):
        """حفظ حالة اللعبة في ملف JSON"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(game_state, f, ensure_ascii=False, indent=4)
            print(f"{Colors.GREEN}✅ تم حفظ تقدمك في مدينة فلسطين بنجاح!{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.RED}❌ خطأ في الحفظ: {e}{Colors.RESET}")

    def load_game(self):
        """تحميل حالة اللعبة إذا كانت موجودة"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return None
        return None

