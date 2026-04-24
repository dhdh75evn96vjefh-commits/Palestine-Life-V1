#!/usr/bin/env python3
import os
import time
from Colors import Colors
from Config import INITIAL_BALANCE, INITIAL_POPULATION, INITIAL_ENERGY, INITIAL_SECURITY, BUILDING_COSTS
from Bank import Bank
from Buildings import BuildingManager
from Population import Population
from Energy import EnergyGrid
from Market import EnergyMarket
from Security import SecuritySystem
from QuestManager import QuestManager

class PalestineLife:
    def __init__(self):
        # تهيئة جميع الأنظمة بناءً على ملفاتك
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
        print(f"""
{Colors.GREEN}╔══════════════════════════════════════════════╗
║        🏙️  فلسطين لايف - Palestine Life       ║
║           نسخة المبرمج المحترف V1.0           ║
╚══════════════════════════════════════════════╝{Colors.RESET}""")
    
    def display_status_bar(self):
        # شريط حالة سريع يظهر في كل دورة
        print(f"{Colors.YELLOW}الدور: {self.turn} | {Colors.GREEN}الخزينة: ${self.bank.balance:,.0f} | {Colors.CYAN}السكان: {self.population.population}")
        print(f"{Colors.BLUE}الطاقة: {self.energy.total_stored:.1f} | {Colors.RED}الأمن: {self.security.security_level}%")
        print(f"{Colors.MAGENTA}══════════════════════════════════════════════")

    def run_turn_updates(self):
        """تحديث المحاكاة عند الانتقال للدور التالي"""
        self.turn += 1
        print(f"\n{Colors.YELLOW}⏳ جاري معالجة بيانات الدور الجديد...")
        
        # 1. تحديث الأمن وفحص الهجمات
        self.security.update_security_level(self.buildings.buildings)
        self.security.scan_threats(self.bank, self.buildings.buildings)
        
        # 2. تحديث الطاقة والسكان
        self.energy.update(self.buildings.buildings, self.population.population)
        self.population.update(self.buildings.buildings)
        
        # 3. تحديث سوق الطاقة
        self.market.update_market()
        
        # 4. فحص المهام ومنح المكافآت
        game_state = {
            "population": self.population.population,
            "commercial_count": len([b for b in self.buildings.buildings if b.type in ["تجاري", "فندق"]]),
            "security": self.security.security_level
        }
        self.quests.check_quests(game_state, self.bank)
        
        time.sleep(1.5)

    def run(self):
        while True:
            self.clear_screen()
            self.display_header()
            self.display_status_bar()
            
            print(f"{Colors.WHITE}1. 🏗️  بناء منشأة جديدة")
            print(f"{Colors.WHITE}2. ⬆️  ترقية منشأة موجودة")
            print(f"{Colors.WHITE}3. 🏦  إدارة البنك والودائع")
            print(f"{Colors.WHITE}4. 💹  سوق الطاقة (بيع الفائض)")
            print(f"{Colors.WHITE}5. 🛡️  المركز الأمني والتقارير")
            print(f"{Colors.WHITE}6. 📜  المهام والإنجازات")
            print(f"{Colors.CYAN}7. ⏭️  إنهاء الدور (تحديث الحالة)")
            print(f"{Colors.RED}0. 🚪  خروج وحفظ")
            
            choice = input(f"\n{Colors.YELLOW}🕹️  اختر الأكشن: ").strip()
            
            if choice == "1":
                print(f"\n{Colors.CYAN}قائمة التكاليف:")
                for b, info in BUILDING_COSTS.items():
                    print(f"- {b}: ${info['base']:,}")
                b_type = input("\nاكتب نوع المبنى: ")
                name = input("اعطِ اسماً للمبنى: ")
                self.buildings.add_building(b_type, name, self.bank)
                time.sleep(2)
                
            elif choice == "2":
                self.buildings.display_buildings()
                try:
                    idx = int(input("رقم المبنى للترقية: ")) - 1
                    self.buildings.upgrade_building(idx, self.bank)
                except: print(Colors.error("مدخل غير صحيح"))
                time.sleep(2)

            elif choice == "3":
                self.bank.display()
                print("1. إيداع | 2. سحب")
                action = input("اختر: ")
                try:
                    amt = float(input("المبلغ: $"))
                    if action == "1": self.bank.deposit(amt)
                    else: self.bank.withdraw(amt)
                except: print(Colors.error("خطأ في المبلغ"))
                time.sleep(2)

            elif choice == "4":
                self.market.display()
                confirm = input("هل تريد بيع كل الفائض؟ (نعم/لا): ")
                if confirm.lower() in ['نعم', 'y']:
                    self.market.sell_energy(self.energy, self.bank)
                time.sleep(2)

            elif choice == "5":
                self.security.display()
                self.population.display()
                input("\nاضغط Enter للعودة...")

            elif choice == "6":
                self.quests.display()
                input("\nاضغط Enter للعودة...")

            elif choice == "7":
                self.run_turn_updates()
                
            elif choice == "0":
                print(f"{Colors.GREEN}تم حفظ تقدمك في مدينة فلسطين الحرة. إلى اللقاء! 🇵🇸")
                break

if __name__ == "__main__":
    game = PalestineLife()
    game.run()
