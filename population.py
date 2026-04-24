import random
from Colors import Colors
from Config import CONSUMPTION_RATES, TOURISM_BASE_RATE, TOURISM_MULTIPLIER

class Population:
    def __init__(self, initial_pop):
        self.population = initial_pop
        self.tourists = 0
        self.food = 100
        self.water = 100
        self.satisfaction = 80
    
    def update(self, buildings):
        """تحديث حالة السكان في كل دورة"""
        # 1. استهلاك الموارد بناءً على الإعدادات
        food_needed = (self.population + self.tourists) * CONSUMPTION_RATES["food_per_person"]
        water_needed = (self.population + self.tourists) * CONSUMPTION_RATES["water_per_person"]
        
        self.food = max(0, self.food - food_needed)
        self.water = max(0, self.water - water_needed)
        
        # 2. منطق السياح المطور
        hotels = [b for b in buildings if b.type == "فندق"]
        commercial = [b for b in buildings if b.type == "تجاري"]
        
        if hotels:
            # السياح يأتون بناءً على الفنادق والرضا العام
            new_tourists = int(len(hotels) * TOURISM_BASE_RATE * (self.satisfaction / 100))
            # إضافة لمسة عشوائية
            self.tourists = new_tourists + random.randint(0, 2)
        else:
            self.tourists = max(0, self.tourists - 2) # رحيل السياح إذا لم توجد فنادق
        
        # 3. نمو السكان المرتبط بالسعة (Capacity)
        total_capacity = sum(b.capacity for b in buildings)
        if self.population < total_capacity and self.satisfaction > 60:
            growth = random.randint(1, 3)
            self.population += growth
        elif self.population > total_capacity:
            self.satisfaction -= 5 # استياء بسبب الازدحام
        
        # 4. تحديث الرضا بناءً على الموارد
        if self.food <= 0 or self.water <= 0:
            self.satisfaction = max(0, self.satisfaction - 15)
            self.population = max(1, self.population - 2) # هجرة أو تناقص بسبب الجوع
        elif self.food > 50 and self.water > 50:
            self.satisfaction = min(100, self.satisfaction + 2)

    def display(self):
        # تحديد لون الرضا بناءً على قيمته
        sat_color = Colors.GREEN if self.satisfaction > 70 else Colors.YELLOW if self.satisfaction > 40 else Colors.RED
        
        print(f"\n{Colors.MAGENTA}══════════ حالة السكان ══════════")
        print(f"👥 السكان: {Colors.WHITE}{self.population} | 📸 السياح: {Colors.CYAN}{self.tourists}")
        print(f"🍎 الطعام: {Colors.YELLOW}{self.food:.1f} | 💧 الماء: {Colors.BLUE}{self.water:.1f}")
        print(f"😊 مستوى الرضا: {sat_color}{self.satisfaction}%")
        print(f"{Colors.MAGENTA}════════════════════════════════\n")
