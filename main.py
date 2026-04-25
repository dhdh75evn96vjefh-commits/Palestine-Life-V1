#!/usr/bin/env python3
import os
import time

# استيراد الأنظمة البرمجية (تأكد من وجود الملفات بنفس الأسماء في مجلدك)
try:
    from colors import Colors
    from config import INITIAL_BALANCE, INITIAL_POPULATION
    from bank import Bank
    from buildings import BuildingManager
    from population import Population
    from energy import EnergyGrid
    from market import EnergyMarket
    from security import SecuritySystem
    from quests import QuestManager
    from events import EventManager
    from disasters import DisasterManager
    from storage import SaveSystem  # تم توحيد الاسم هنا لحل مشكلة NameError
except ImportError as e:
    print(f"❌ خطأ: لم يتم العثور على ملف {e.name}. تأكد من وجوده في المجلد.")
    exit()

class PalestineLife:
    def __init__(self):
        # تهيئة الكائنات بناءً على ملفاتك في GitHub
        self.save_sys = SaveSystem()
        self.bank = Bank(INITIAL_BALANCE)
        self.buildings = BuildingManager()
        self.population = Population(INITIAL_POPULATION)
        self.energy = EnergyGrid()
        self.market = EnergyMarket()
        
        # إصلاح خطأ E1120: أضفنا قيمة البداية (100) لنظام الحماية
        self.security = SecuritySystem(100) 
        
        self.quests = QuestManager()
        self.events = EventManager()
        self.disasters = DisasterManager()

        self.turn = 1

    def clear_screen(self):
        os.system('clear' if os.name != 'nt' else 'cls')

    def display_status(self):
        # شريط الحالة العلوي
        print(f"{Colors.GREEN}#{"="*50}#")
        print(f"{Colors.WHITE} الدور: {self.turn} | المال: ${self.bank.balance} | السكان: {self.population.total}")
        print(f"{Colors.YELLOW} الطاقة: {self.energy.total_stored}MW | الحماية: {self.security.level}%")
        
        if self.disasters.active_disaster:
            print(f"{Colors.RED}🚨 كارثة نشطة: {self.disasters.active_disaster_name}")
        print(f"{Colors.GREEN}#{"="*50}#{Colors.WHITE}\n")

    def run(self):
        while True:
            self.clear_screen()
            self.display_status()
            
            print("1. إدارة المباني")
            print("2. البنك والاقتصاد")
            print("3. سوق الطاقة")
            print("4. المهمات")
            print("5. حفظ اللعبة")
            print("0. خروج")
            
            choice = input(f"\n{Colors.CYAN}اختر إجراءً: {Colors.WHITE}")
            
            if choice == '1':
                # تأكد أن BuildingManager يحتوي على هذه الوظيفة
                self.buildings.display_menu(self.bank)
            elif choice == '2':
                self.bank.display_menu()
            elif choice == '3':
                self.market.display_menu(self.energy, self.bank)
            elif choice == '4':
                self.quests.display_quests()
            elif choice == '5':
                self.save_sys.save_game(self)
                print(f"{Colors.GREEN}تم حفظ التقدم بنجاح!")
                time.sleep(1)
            elif choice == '0':
                break
            
            self.turn += 1

if __name__ == "__main__":
    game = PalestineLife()
    game.run()
