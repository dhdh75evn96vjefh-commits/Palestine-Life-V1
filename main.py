import os
import time
import random
from colorama import Fore, Style, init

# استيراد كافة الأنظمة من ملفاتك على GitHub
from city_manager import City
from building_system import Building
from economy import Bank
from population import PopulationManager
from save_system import SaveManager
from utilities import PowerGrid
from market import Market  # السوق الجديد الذي أضفته

# تفعيل الألوان وتحميل الأنظمة
init(autoreset=True)
save_mgr = SaveManager()
market = Market()

def main_menu():
    # 1. تحميل البيانات السابقة أو بدء مدينة جديدة
    saved_data = save_mgr.load()
    my_city = City("فلسطين الحرة")
    pop_sys = PopulationManager()
    power_sys = PowerGrid()
    
    if saved_data:
        my_bank = Bank(saved_data.get('balance', 35000))
        for _ in range(saved_data.get('pop_count', 0)):
            pop_sys.add_resident("مواطن")
        print(Fore.GREEN + "✅ تم استعادة بيانات مدينتك!")
    else:
        my_bank = Bank(35000)

    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # --- محرك الأحداث العشوائية ---
        event_chance = random.random()
        event_msg = ""
        if event_chance < 0.1: # احتمال 10% لهجوم سيبراني
            loss = random.randint(500, 2000)
            my_bank.withdraw(loss)
            event_msg = f"{Fore.RED}⚠️ تنبيه: تعرضت المدينة لهجوم سيبراني! خسارة: {loss}$"

        # --- فحص حالة المدينة ---
        has_food = any(b.b_type == "تجاري" for b in my_city.buildings)
        has_water = any(b.b_type == "خدمي" for b in my_city.buildings)
        pop_sys.simulate_hour(has_food, has_water)

        # --- عرض الواجهة (UI) ---
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}💰 الخزينة: {my_bank.balance} $ | {Fore.WHITE}👥 السكان: {len(pop_sys.residents)}")
        print(f"{Fore.YELLOW}⚡ الطاقة: {power_sys.power_level} وحدة | {Fore.BLUE}🏠 المباني: {len(my_city.buildings)}")
        print(f"{Fore.CYAN}{'='*60}")
        
        if event_msg: print(event_msg)
        if not has_food: print(f"{Fore.RED}🍔 تنبيه: السكان جائعون! ابنِ منشأة تجارية.")

        print(f"\n{Fore.WHITE}1. 🏗️ بناء منشأة (5000$)")
        print("2. 👥 جذب سكان جُدد")
        print(f"{Fore.YELLOW}3. 💰 بيع فائض الطاقة (سوق التداول)")
        print(f"{Fore.GREEN}4. 📊 تقرير المدينة")
        print(f"{Fore.RED}5. 💾 حفظ وخروج")
        print(f"{Fore.CYAN}{'='*60}")

        choice = input(f"{Fore.MAGENTA}🎮 خيارك يا مدير: ")

        if choice == '1':
            b_type = input("نوع المبنى (تجاري/خدمي/سكن): ")
            if my_bank.withdraw(5000):
                new_b = Building(b_type, 5000)
                my_city.add_building(new_b)
                # زيادة إنتاج الطاقة عند بناء منشأة خدمية
                if b_type == "خدمي": power_sys.power_level += 20
                print(f"{Fore.GREEN}✅ تم بناء {b_type}!")
            else:
                print(f"{Fore.RED}❌ رصيدك غير كافٍ!")
            time.sleep(1)

        elif choice == '2':
            pop_sys.add_resident("مواطن جديد")
            print(f"{Fore.BLUE}👣 انضم ساكن جديد للمدينة.")
            time.sleep(0.5)

        elif choice == '3':
            # استخدام ملف market.py الذي أنشأته
            result = market.trade_power(power_sys, my_bank)
            print(f"{Fore.YELLOW}{result}")
            time.sleep(1.5)

        elif choice == '5':
            data = {"balance": my_bank.balance, "pop_count": len(pop_sys.residents)}
            save_mgr.save(data)
            print(f"{Fore.YELLOW}👋 تم حفظ التقدم.. إلى اللقاء!")
            break

if __name__ == "__main__":
    main_menu()
