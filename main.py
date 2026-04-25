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
    from storage import SaveSystem # حل مشكلة التعريف
except ImportError as e:
    print(f"❌ خطأ: لم يتم العثور على ملف {e.name}. تأكد من وجوده في المجلد.")

class PalestineLife:
    def __init__(self):
        # تهيئة الكائنات بناءً على ملفاتك في GitHub
        self.save_sys = SaveSystem()
        self.bank = Bank(INITIAL_BALANCE)
        self.buildings = BuildingManager()
        self.population = Population(INITIAL_POPULATION)
        self.energy = EnergyGrid()
        self.market = EnergyMarket()
        self.security = SecuritySystem(100)
        self.quests = QuestManager()
        self.events = EventManager()
        self.disasters = DisasterManager()
        
        self.turn = 1

    def clear_screen(self):
        os.system('clear' if os.name != 'nt' else 'cls')

    def display_status(self):
        # شريط الحالة العلوي
        print(f"{Colors.GREEN}══════════════════════════════════════════")
        print(f"{Colors.WHITE} الدور: {self.turn} | المال: ${self.bank.balance:,.0f} | السكان: {self.population.population}")
        print(f"{Colors.YELLOW} الطاقة: {self.energy.total_stored:.1f} | الأمن: {self.security.security_level}%")
        
        if self.disasters.active_disaster:
            print(f"{Colors.RED}🚨 كارثة نشطة: {self.disasters.active_disaster['name']}")
        print(f"{Colors.GREEN}══════════════════════════════════════════{Colors.RESET}")

    def display_menu(self):
        # تنسيق جديد لضمان ظهور الرقم 4 بوضوح في Termux
        print(f"{Colors.CYAN} [1] {Colors.WHITE}🏗️  بناء/ترقية المنشآت")
        print(f"{Colors.CYAN} [2] {Colors.WHITE}💹  سوق الطاقة")
        print(f"{Colors.CYAN} [3] {Colors.WHITE}🏦  إدارة البنك")
        print(f"{Colors.CYAN} [4] {Colors.WHITE}🛡️  الأمن والسكان") # لن يختفي الآن
        print(f"{Colors.CYAN} [5] {Colors.WHITE}📜  المهام والجوائز")
        print(f"{Colors.CYAN} [6] {Colors.WHITE}🆘  غرفة الطوارئ (الكوارث)")
        print(f"{Colors.CYAN} [7] {Colors.WHITE}⏭️  إنهاء الدور (Update)")
        print(f"{Colors.RED} [0] {Colors.WHITE}💾  حفظ وخروج")

    def run(self):
        while True:
            self.clear_screen()
            print(f"{Colors.GREEN}🇵🇸 مدينة فلسطين - الإصدار المتكامل V1{Colors.RESET}")
            self.display_status()
            self.display_menu()
            
            choice = input(f"\n{Colors.YELLOW}🕹️ اختر أمر: {Colors.RESET}").strip()
            
            if choice == "1":
                self.buildings.add_building_menu(self.bank)
            elif choice == "2":
                self.market.sell_energy(self.energy, self.bank)
            elif choice == "3":
                self.bank.display_bank_menu()
            elif choice == "4":
                self.security.display_security_status()
                self.population.display_pop_info()
            elif choice == "5":
                self.quests.display_quests()
            elif choice == "6":
                self.disasters.display_status()
                if self.disasters.active_disaster and not self.disasters.recovery_plan:
                    self.disasters.display_recovery_options()
                    try:
                        plan_idx = int(input("اختر خطة (رقم): ")) - 1
                        self.disasters.choose_recovery_plan(plan_idx, self.bank)
                    except: pass
            elif choice == "7":
                self.process_turn()
            elif choice == "0":
                # استخدام نظام الحفظ storage.py
                save_data = {
                    "balance": self.bank.balance,
                    "population": self.population.population,
                    "turn": self.turn
                }
                self.save_sys.save_game(save_data)
                break
            input(f"\n{Colors.WHITE}اضغط Enter للمتابعة...")

    def process_turn(self):
        self.turn += 1
        print(f"\n{Colors.YELLOW}⏳ جاري تحديث بيانات الدور {self.turn}...{Colors.RESET}")
        
        # تحديث الموارد
        self.energy.update(self.buildings.buildings, self.population.population)
        self.population.update(self.buildings.buildings)
        
        # فحص الكوارث والأحداث العشوائية
        self.disasters.check_warning_signs()
        self.disasters.trigger_disaster(self.turn)
        
        if self.disasters.active_disaster:
            self.disasters.apply_disaster_effects(None, self.bank, self.population, self.energy, self.buildings, self.security)
        else:
            self.events.trigger_random_event(None)
            
        time.sleep(1.5)

if __name__ == "__main__":
    game = PalestineLife()
    game.run()
