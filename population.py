import random

class Resident:
    def __init__(self, name):
        self.name = name
        self.hunger = 0      # الجوع (0 شبعان - 100 ميت)
        self.thirst = 0      # العطش (0 مرتوِ - 100 ميت)
        self.energy = 100    # الطاقة والراحة
        self.is_alive = True
        self.status = "مستقر"

    def live_life(self, hour, has_food, has_water):
        if not self.is_alive:
            return

        # 1. استهلاك الموارد بناءً على الوقت (نظام اليوم والليلة)
        if 8 <= hour <= 16:  # وقت العمل (استهلاك عالٍ)
            self.energy -= 8
            self.hunger += 12
            self.thirst += 15
            self.status = "في العمل"
        elif 22 <= hour or hour <= 6:  # وقت النوم (استعادة طاقة)
            self.energy = min(100, self.energy + 15)
            self.hunger += 3
            self.thirst += 5
            self.status = "نائم"
        else:  # وقت الفراغ والتجول
            self.energy -= 2
            self.hunger += 6
            self.thirst += 8
            self.status = "متجول"

        # 2. تلبية الاحتياجات (إذا وفرت المدينة المنشآت)
        if has_food and self.hunger > 40:
            self.hunger = max(0, self.hunger - 60)
            self.status = "يأكل"
        
        if has_water and self.thirst > 40:
            self.thirst = max(0, self.thirst - 70)
            self.status = "يشرب"

class PopulationManager:
    def __init__(self):
        self.residents = []
        self.game_hour = 8

    def add_residents(self, count):
        for i in range(count):
            name = f"مواطن_{len(self.residents) + 1}"
            self.residents.append(Resident(name))

    def simulate_hour(self, has_food, has_water):
        # تقدم الوقت ساعة واحدة
        self.game_hour = (self.game_hour + 1) % 24
        
        # تحديث حالة كل ساكن وفحص الوفيات
        for r in self.residents[:]:
            r.live_life(self.game_hour, has_food, has_water)
            
            # فحص الوفاة بسبب الجوع أو العطش
            if r.hunger >= 100 or r.thirst >= 100:
                cause = "الجوع" if r.hunger >= 100 else "العطش"
                print(f"💀 كارثة! {r.name} توفي بسبب {cause}.")
                self.residents.remove(r)
            elif r.hunger > 80 or r.thirst > 80:
                print(f"⚠️ تحذير: {r.name} في حالة صحية حرجة!")
