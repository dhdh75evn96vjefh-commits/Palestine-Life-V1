#!/usr/bin/env python3
import os
import time

# استيراد الألوان والملفات التي ظهرت في صورتك على جيت هاب
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
    from storage import SaveSystem
except ImportError as e:
    print(f"❌ خطأ: لم يتم العثور على ملف {e.name}. تأكد من وجوده في نفس المجلد.")

class PalestineLife:
    def __init__(self):
        # تهيئة كل الأنظمة التي أظهرتها في صورة الملفات
        self.save_sys = SaveSystem()
        self.bank = Bank(INITIAL_BALANCE)
        self.buildings = BuildingManager()
        self.population = Population(INITIAL_POPULATION)
        self.energy = EnergyGrid()
        self.market = EnergyMarket()
        self.security = SecuritySystem()
        self.quests = QuestManager()
        self.events = EventManager()
        self.disasters = DisasterManager()
        
        self.turn = 1

    def clear_screen(self):
        os.system('clear' if os.name != 'nt' else 'cls')

    def display_status(self):
        print(f"{Colors.GREEN}══════════════════════════════════════════")
        print(f"{Colors.WHITE} الدور: {self.turn} | المال: ${self.bank.balance:,.0f} | السكان: {self.population.population}")
        print(f"{Colors.YELLOW} الطاقة: {self.energy.total_stored:.1f} | الأمن: {self.security.security_level}%")
        if self.disasters.active_disaster:
            print(f"{Colors.RED}🚨 كارثة نشطة: {self.disasters.active_disaster['name']}")
        print(f"{Colors.GREEN}══════════════════════════════════════════{Colors.RESET}")

    def display_menu(self):
        print(f"{Colors.CYAN}1. {Colors.WHITE}🏗️  بناء/ترقية المنشآت")
        print(f"{Colors.CYAN}2. {Colors.WHITE}💹  سوق الطاقة")
        print(f"{Colors.CYAN}3. {Colors.WHITE}🏦  إدارة البنك")
        print(f"{Colors.CYAN}4. {Colors.WHITE}🛡️  الأمن والسكان")
        print(f"{Colors.CYAN}5. {Colors.WHITE}📜  المهام والجوائز")
        print(f"{Colors.CYAN}6. {Colors.WHITE}🆘  غرفة الطوارئ (الكوارث)")
        print(f"{Colors.CYAN}7. {Colors.WHITE}⏭️  إنهاء الدور (Update)")
        print(f"{Colors.RED}0. {Colors.WHITE}💾  حفظ وخروج")

    def run(self):
        while True:
            self.clear_screen()
            print(f"{Colors.GREEN}🇵🇸 مدينة فلسطين - الإصدار المطور V1{Colors.RESET}")
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
                self.disasters.display_recovery_options()
            elif choice == "7":
                self.next_turn()
            elif choice == "0":
                # استخدام ملف storage.py الذي صنعته
                self.save_sys.save_game(self)
                break
            input(f"\n{Colors.WHITE}اضغط Enter للمتابعة...")

    def next_turn(self):
        self.turn += 1
        # تحديث الموارد
        self.energy.update(self.buildings)
        self.population.grow()
        # فحص الكوارث والأحداث
        self.disasters.check_for_disaster(self.turn)
        self.events.trigger_random_event(self)
        print(f"{Colors.GREEN}✅ تم الانتقال للدور {self.turn}")

if __name__ == "__main__":
    game = PalestineLife()
    game.run()
