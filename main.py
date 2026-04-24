#!/usr/bin/env python3
import os
import time
# استيراد الألوان (تأكد أن اسم الملف Colors.py أو colors.py)
try:
    from colors import Colors
except ImportError:
    from Colors import Colors

# استيراد الأنظمة (تأكد أن أسماء الملفات مطابقة لما في المجلد)
from bank import Bank
from buildings import BuildingManager
from population import Population
from energy import EnergyGrid
from market import EnergyMarket
from security import SecuritySystem
from quests import QuestManager
from config import INITIAL_BALANCE, INITIAL_POPULATION, INITIAL_ENERGY, INITIAL_SECURITY, BUILDING_COSTS

class PalestineLife:
    def __init__(self):
        self.bank = Bank(INITIAL_BALANCE)
        self.buildings = BuildingManager()
        self.population = Population(INITIAL_POPULATION)
        self.energy = EnergyGrid(INITIAL_ENERGY)
        self.market = EnergyMarket()
        self.security = SecuritySystem(INITIAL_SECURITY)
        self.quests = QuestManager()
        self.turn = 1
    
    def clear_screen(self):
        os.system('clear' if os.name != 'nt' else 'cls')
    
    def display_header(self):
        print(f"{Colors.GREEN}======================================")
        print(f"{Colors.WHITE}   PALESTINE LIFE - فلسطين لايف V1.0  ")
        print(f"{Colors.GREEN}======================================")
    
    def display_status(self):
        # عرض الحالة بشكل مبسط لضمان القراءة في Termux
        print(f"{Colors.CYAN}[Turn: {self.turn}] | [Cash: ${self.bank.balance:,.0f}]")
        print(f"{Colors.YELLOW}[Pop: {self.population.population}] | [Energy: {self.energy.total_stored:.1f}]")
        print(f"{Colors.MAGENTA}--------------------------------------")

    def display_menu(self):
        # القائمة مرتبة لضمان ظهور رقم 4
        print(f"{Colors.WHITE}1. [Build] بناء منشأة جديدة")
        print(f"{Colors.WHITE}2. [Upgrade] ترقية منشأة")
        print(f"{Colors.WHITE}3. [Market] سوق الطاقة والبيع")
        print(f"{Colors.WHITE}4. [Bank] إدارة الحساب البنكي") # تم إضافة الرقم 4 هنا
        print(f"{Colors.WHITE}5. [Status] التقارير والأمن")
        print(f"{Colors.WHITE}6. [Quests] المهام والإنجازات")
        print(f"{Colors.CYAN}7. [Next Turn] إنهاء الدور")
        print(f"{Colors.RED}0. [Exit] خروج وحفظ")
        print(f"{Colors.MAGENTA}--------------------------------------")

    def run(self):
        while True:
            self.clear_screen()
            self.display_header()
            self.display_status()
            self.display_menu()
            
            choice = input(f"{Colors.YELLOW}🕹️ Choice/اختر: ").strip()
            
            if choice == "1":
                # منطق البناء
                print("\nTypes: سكني, تجاري, مصنع, فندق, مستشفى, مركز_طاقة")
                b_type = input("Type/النوع: ")
                name = input("Name/الاسم: ")
                self.buildings.add_building(b_type, name, self.bank)
                time.sleep(2)
                
            elif choice == "2":
                self.buildings.display_buildings()
                try:
                    idx = int(input("Number/الرقم: ")) - 1
                    self.buildings.upgrade_building(idx, self.bank)
                except: print("Error!")
                time.sleep(2)

            elif choice == "3":
                self.market.display()
                self.market.sell_energy(self.energy, self.bank)
                time.sleep(2)

            elif choice == "4": # تفعيل خيار البنك
                self.bank.display()
                input("Press Enter to return...")

            elif choice == "5":
                self.security.display()
                self.population.display()
                input("Press Enter to return...")

            elif choice == "6":
                self.quests.display()
                input("Press Enter to return...")

            elif choice == "7":
                self.turn += 1
                # تحديثات الدور
                self.energy.update(self.buildings.buildings, self.population.population)
                self.population.update(self.buildings.buildings)
                self.security.scan_threats(self.bank, self.buildings.buildings)
                print(f"{Colors.GREEN}Done! الدور التالي...")
                time.sleep(1.5)
                
            elif choice == "0":
                print("🇵🇸 شكراً للعب! فلسطين حرة")
                break

if __name__ == "__main__":
    game = PalestineLife()
    game.run()
