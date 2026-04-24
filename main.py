import os
import time
import random
from colorama import Fore, init

# استيراد الأنظمة من ملفاتك
from city_manager import City
from building_system import Building
from economy import Bank
from population import PopulationManager
from save_system import SaveManager
from utilities import PowerGrid
from market import Market
from quests import QuestManager

init(autoreset=True)
save_mgr = SaveManager()
market = Market()
quest_sys = QuestManager()

def main_menu():
    my_city = City("فلسطين الحرة")
    pop_sys = PopulationManager()
    power_sys = PowerGrid()
    
    # تحميل البيانات
    saved_data = save_mgr.load()
    if saved_data:
        my_bank = Bank(saved_data.get('balance', 35000))
        print(Fore.GREEN + "✅ تم تحميل مدينتك!")
    else:
        my_bank = Bank(35000)

    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # فحص المهام المضافة حديثاً
        notifications = quest_sys.check_quests(my_city, pop_sys, power_sys, my_bank)
        
        # عرض الواجهة الملونة
        print(f"{Fore.CYAN}{'='*50}")
        print(f"{Fore.GREEN}💰 الخزينة: {my_bank.balance}$ | {Fore.WHITE}👥 السكان: {len(pop_sys.residents)}")
        print(f"{Fore.YELLOW}⚡ الطاقة: {power_sys.power_level} | {Fore.BLUE}🏠 المباني: {len(my_city.buildings)}")
        print(f"{Fore.CYAN}{'='*50}")
        
        for note in notifications: print(f"{Fore.MAGENTA}{note}")
        
        print(f"\n1. 🏗️ بناء منشأة (5000$)")
        print("2. 👥 جذب سكان")
        print(f"3. 💹 سوق الطاقة")
        print(f"5. 💾 حفظ وخروج")

        choice = input(f"\n{Fore.MAGENTA}🎮 خيارك: ")

        if choice == '1':
            name = input("اسم المبنى: ")
            b_type = input("النوع (تجاري/خدمي): ")
            if my_bank.withdraw(5000):
                # استخدام الهيكل المطور لـ Building
                new_b = Building(name, b_type, 5000, 50)
                new_b.construct()
                my_city.add_building(new_b)
            time.sleep(1)

        elif choice == '3':
            # ربط ملف market.py
            print(market.trade_power(power_sys, my_bank))
            time.sleep(1.5)

        elif choice == '5':
            save_mgr.save({"balance": my_bank.balance, "pop_count": len(pop_sys.residents)})
            break

if __name__ == "__main__":
    main_menu()
