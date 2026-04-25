 import json
import os

class SaveSystem: # تم تغيير الاسم ليتوافق مع main.py
    def __init__(self, filename="city_save.json"):
        self.filename = filename

    def save_game(self, game_obj): # تم تغيير الاسم ليتوافق مع استدعاء اللعبة
        """يحفظ بيانات اللعبة (الرصيد، السكان، إلخ)"""
        data = {
            "money": game_obj.bank.balance,
            "population": game_obj.population.total,
            "turn": game_obj.turn
        }
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"❌ عطل أثناء الحفظ: {e}")
            return False
