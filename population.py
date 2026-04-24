import random

class Resident:
    def __init__(self, name):
        self.name = name
        self.hunger = 0      # الجوع (0 يعني شبعان)
        self.energy = 100    # الطاقة (100 يعني نشيط)
        self.is_home = True

    def live_life(self, hour, has_food_store):
        # في النهار يخرجون للعمل
        if 8 <= hour <= 16:
            self.is_home = False
            self.energy -= 10
            self.hunger += 15
        # في الليل يعودون للنوم
        else:
            self.is_home = True
            self.energy = min(100, self.energy + 20)
            
        # البحث عن الأكل
        if self.hunger > 50 and has_food_store:
            self.hunger = 0
            return "تم الأكل في المطعم"
        return "مستقر"

class PopulationManager:
    def __init__(self):
        self.residents = [] # قائمة السكان "الحقيقيين" في الكود
        self.game_hour = 8   # تبدأ اللعبة الساعة 8 صباحاً

    def add_residents(self, count):
        for i in range(count):
            self.residents.append(Resident(f"ساكن_{len(self.residents)}"))

    def simulate_hour(self, has_food_store):
        self.game_hour = (self.game_hour + 1) % 24
        for r in self.residents:
            r.live_life(self.game_hour, has_food_store)

