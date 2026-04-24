import os
import time
import random
from colorama import Fore, Style, init

# استيراد الأنظمة من ملفاتك التي رفعتها على GitHub
from city_manager import City
from building_system import Building
from economy import Bank
from population import PopulationManager
from save_system import SaveManager
from utilities import PowerGrid
from market import Market
from quests import QuestManager

# تفعيل الألوان وتحميل الأنظمة
init(autoreset=True)
save_mgr = SaveManager()
market = Market()
quest_sys = QuestManager()

def main_menu():
    # 1. إعداد المدينة والأنظمة
    my_city = City("فلسطين الحرة")
    pop_sys = PopulationManager()
    power_sys = PowerGrid()
    
    # تحميل البيانات المحفوظة إن وجدت
    saved_data = save_mgr.load()
    if saved_data:
        my_bank = Bank(saved_data.get('balance', 35000))
        for _ in range(saved_data.get('pop_count', 0)):
            pop_sys.add_resident("مواطن")
        print(Fore.GREEN + "✅ تم استعادة بيانات مدينتك بنجاح!")
    else:
        my_bank = Bank(35000)

    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # --- فحص المهام (Quests) ---
        # يقوم بفحص التقدم ومنح المكافآت تلقائياً
        notifications = quest_sys.check_quests(my_city, pop_sys, power_sys, my_bank)
        
        # --- محرك الأحداث العشوائية ---
        event_msg = ""
        if random.random() < 0.1: # احتمال 10% لهجوم سيبراني
            loss = random.randint(500, 2000)
            my_bank.withdraw(loss)
            event_msg = f"{Fore.RED}⚠️ تنبيه أمني: تعرضت المدينة لهجوم سيبراني! خسارة: {loss}$"

        # --- فحص حالة السكان ---
        # التأكد من وجود مبانٍ توفر الخدمات
        has_food = any(b.b_type == "تجاري" for b in my_city.buildings)
        has_water = any(b.b_type == "خدمي" for b in my_city.buildings)
        pop_sys.simulate_hour(has_food, has_water)

        # --- عرض واجهة المستخدم (UI) ---
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}💰 الخزينة: {my_bank.balance} $ | {Fore.WHITE}👥 السكان: {len(pop_sys.residents)}")
        print(f"{Fore.YELLOW}⚡ الطاقة: {power_sys.power_level} | {Fore.BLUE}🏠 المباني: {len(my_city.buildings)}")
        print(f"{Fore.CYAN}{'='*60}")
        
        if event_msg: print(event_msg)
        for note in notifications: print(f"{Fore.MAGENTA}{note}")
        
        print(f"\n{Fore.WHITE}1. 🏗️ بناء منشأة جديدة (5000$)")
        print("2. 👥 جذب سكان للمدينة")
        print(f"{Fore.YELLOW}3. 💹 سوق التداول (بيع الطاقة)")
        print(f"{Fore.BLUE}4. 📊 عرض تقرير المباني")
        print(f"{Fore.RED}5. 💾 حفظ التقدم والخروج")
        print(f"{Fore.CYAN}{'='*60}")

        choice = input(f"{Fore.MAGENTA}🎮 خيارك يا مدير: ")

        if choice == '1':
            name = input("أدخل اسم المبنى: ")
            b_type = input("النوع (تجاري/خدمي/سكن): ")
            if my_bank.withdraw(5000):
                # إنشاء الكائن بناءً على هيكل building_system.py المطور
                new_b = Building(name, b_type, 5000, 50)
                new_b.construct()
                my_city.add_building(new_b)
                if b_type == "خدمي": power_sys.power_level += 25
            else:
                print(f"{Fore.RED}❌ رصيدك غير كافٍ للبناء!")
            time.sleep(1.5)

        elif choice == '2':
            pop_sys.add_resident("مواطن جديد")
            print(f"{Fore.BLUE}👤 انضم ساكن جديد لمدينتك.")
            time.sleep(0.5)

        elif choice == '3':
            # استخدام نظام السوق من ملف market.py
            result = market.trade_power(power_sys, my_bank)
            print(f"{Fore.YELLOW}{result}")
            time.sleep(1.5)

        elif choice == '4':
            print(f"\n{Fore.WHITE}--- قائمة المنشآت الحالية ---")
            for b in my_city.buildings:
                print(b.get_info())
            input("\nاضغط Enter للعودة...")

        elif choice == '5':
            data = {
                "balance": my_bank.balance, 
                "pop_count": len(pop_sys.residents),
                "city_name": my_city.name
            }
            save_mgr.save(data)
            print(f"{Fore.YELLOW}👋 تم حفظ بيانات 'Palestine-Life-V1'. نراك لاحقاً!")
            break

if __name__ == "__main__":
    main_menu()
