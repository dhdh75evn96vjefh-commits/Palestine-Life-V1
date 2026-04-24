#!/usr/bin/env python3
import os
import time

# استيراد الأنظمة البرمجية (تأكد من وجود الملفات بنفس الأسماء)
from colors import Colors
from config import INITIAL_BALANCE, INITIAL_POPULATION, INITIAL_ENERGY, INITIAL_SECURITY, BUILDING_COSTS
from bank import Bank
from buildings import BuildingManager
from population import Population
from energy import EnergyGrid
from market import EnergyMarket
from security import SecuritySystem
from quests import QuestManager
from events import EventManager
from disasters import DisasterManager

class PalestineLife:
    def __init__(self):
        # تهيئة الكائنات الأساسية
        self.bank = Bank(INITIAL_BALANCE)
        self.buildings = BuildingManager()
        self.population = Population(INITIAL_POPULATION)
        self.energy = EnergyGrid(INITIAL_ENERGY)
        self.market = EnergyMarket()
        self.security = SecuritySystem(INITIAL_SECURITY)
        self.quests = QuestManager()
        
        # تهيئة أنظمة التحديث الجديد
        self.events = EventManager()
        self.disasters = DisasterManager()
        
        self.turn = 1
        self.current_effects = {}

    def clear_screen(self):
        os.system('clear' if os.name != 'nt' else 'cls')

    def display_header(self):
        print(f"{Colors.GREEN}╔══════════════════════════════════════════════╗")
        print(f"║     🏙️  فلسطين لايف - PALESTINE LIFE V1.1    ║")
        print(f"╚══════════════════════════════════════════════╝{Colors.RESET}")

    def display_status_bar(self):
        # شريط المعلومات العلوي
        print(f"{Colors.CYAN} الدور: {self.turn} | {Colors.GREEN}الخزينة: ${self.bank.balance:,.0f} | {Colors.WHITE}السكان: {self.population.population}")
        print(f"{Colors.YELLOW} الطاقة: {self.energy.total_stored:.1f} | {Colors.RED}الأمن: {self.security.security_level}%")
        
        # عرض حالة الكارثة إذا كانت نشطة
        if self.disasters.active_disaster:
            print(f"{Colors.MAGENTA}🚨 كارثة نشطة: {self.disasters.active_disaster['name']} ({self.disasters.disaster_timer} أدوار متبقية)")
        print(f"{Colors.GREEN}══════════════════════════════════════════════{Colors.RESET}")

    def display_menu(self):
        print(f"{Colors.WHITE}1. 🏗️  بناء منشأة جديدة")
        print(f"{Colors.WHITE}2. ⬆️  ترقية المنشآت")
        print(f"{Colors.WHITE}3. 💹  سوق الطاقة (بيع)")
        print(f"{Colors.WHITE}4. 🏦  الحساب البنكي")
        print(f"{Colors.WHITE}5. 🛡️  الوضع الأمني والسكان")
        print(f"{Colors.WHITE}6. 📜  قائمة المهام")
        print(f"{Colors.RED if self.disasters.active_disaster else Colors.WHITE}7. 🆘 غرفة الطوارئ والتعافي")
        print(f"{Colors.CYAN}8. ⏭️  إنهاء الدور (Update)")
        print(f"{Colors.YELLOW}0. 🚪  خروج وحفظ")
        print(f"{Colors.GREEN}══════════════════════════════════════════════{Colors.RESET}")

    def process_turn_logic(self):
        """معالجة ما يحدث عند الانتقال لدور جديد"""
        self.turn += 1
        print(f"\n{Colors.YELLOW}⏳ جاري معالجة بيانات الدور الجديد...{Colors.RESET}")
        
        # 1. تحديث الموارد الأساسية
        self.energy.update(self.buildings.buildings, self.population.population)
        self.population.update(self.buildings.buildings)
        
        # 2. نظام الكوارث (فحص التحذيرات وتفعيل الكوارث)
        self.disasters.check_warning_signs()
        self.disasters.trigger_disaster(self.turn)
        
        if self.disasters.active_disaster:
            # تطبيق تأثير الكارثة
            self.disasters.apply_disaster_effects(None, self.bank, self.population, self.energy, self.buildings, self.security)
        else:
            # 3. نظام الأحداث العشوائية (يعمل فقط إذا لم تكن هناك كارثة)
            self.events.trigger_random_event(None)
            self.events.apply_event_effects(None, self.bank, self.population, self.energy, self.buildings, self.security)

        # 4. فحص المهام
        game_state = {"population": self.population.population, "security": self.security.security_level}
        self.quests.check_quests(game_state, self.bank)

        time.sleep(2)

    def run(self):
        while True:
            self.clear_screen()
            self.display_header()
            self.display_status_bar()
            self.display_menu()
            
            choice = input(f"{Colors.YELLOW}🕹️ اختر الأكشن: {Colors.RESET}").strip()
            
            if choice == "1":
                print("\nالأنواع: سكني, تجاري, مصنع, فندق, مستشفى, مركز_طاقة")
                b_type = input("النوع: ")
                name = input("الاسم: ")
                self.buildings.add_building(b_type, name, self.bank)
                time.sleep(1.5)
                
            elif choice == "2":
                self.buildings.display_buildings()
                try:
                    idx = int(input("رقم المبنى للترقية: ")) - 1
                    self.buildings.upgrade_building(idx, self.bank)
                except: print(Colors.error("مدخل غير صحيح"))
                time.sleep(1.5)

            elif choice == "3":
                self.market.display()
                self.market.sell_energy(self.energy, self.bank)
                time.sleep(2)

            elif choice == "4":
                self.bank.display()
                input("\nاضغط Enter للعودة...")

            elif choice == "5":
                self.security.display()
                self.population.display()
                input("\nاضغط Enter للعودة...")

            elif choice == "6":
                self.quests.display()
                input("\nاضغط Enter للعودة...")

            elif choice == "7":
                self.disasters.display_status()
                if self.disasters.active_disaster and not self.disasters.recovery_plan:
                    self.disasters.display_recovery_options()
                    try:
                        plan = int(input("اختر خطة (رقم): ")) - 1
                        self.disasters.choose_recovery_plan(plan, self.bank)
                    except: pass
                input("\nاضغط Enter للعودة...")

            elif choice == "8":
                self.process_turn_logic()
                
            elif choice == "0":
                print(f"{Colors.GREEN}🇵🇸 تم حفظ البيانات.. شكراً للقائد!{Colors.RESET}")
                break

if __name__ == "__main__":
    game = PalestineLife()
    game.run()
