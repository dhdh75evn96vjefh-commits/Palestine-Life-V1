import os
import time
from colorama import Fore, Style, init

# استيراد ملفاتك
from city_manager import City
from economy import Bank
from population import PopulationManager
from save_system import SaveManager
from building_system import Building

init(autoreset=True)
save_mgr = SaveManager()

def main_menu():
    # تحميل البيانات أو بدء مدينة جديدة
    saved_data = save_mgr.load()
    
    my_city = City("فلسطين الحرة")
    pop_sys = PopulationManager()
    
    if saved_data:
        my_bank = Bank(saved_data.get('balance', 35000))
        # إضافة سكان وهميين بناءً على العدد المحفوظ
        for _ in range(saved_data.get('pop_count', 0)):
            pop_sys.add_resident("مواطن")
        print(Fore.GREEN + "✅ تم تحميل مدينتك بنجاح!")
    else:
        my_bank = Bank(35000)

    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # فحص الموارد (حل خطأ buildings)
        has_food = any(b.b_type == "تجاري" for b in my_city.buildings)
        has_water = any(b.b_type == "خدمي" for b in my_city.buildings)
        
        pop_sys.simulate_hour(has_food, has_water)
        
        # واجهة المستخدم الملونة
        print(f"{Fore.CYAN}{'='*45}")
        print(f"{Fore.GREEN}💰 الخزينة: {my_bank.balance} $ | {Fore.WHITE}👥 السكان: {len(pop_sys.residents)}")
        print(f"{Fore.CYAN}{'='*45}")
        
        print("\n1. 🏗️ بناء منشأة (5000$)")
        print("2. 👥 جذب مهاجرين")
        print("3. 📊 تقرير الحالة")
        print(Fore.YELLOW + "5. 💾 حفظ وخروج")
        
        choice = input(f"\n{Fore.MAGENTA}🎮 قرارك يا مدير: ")

        if choice == '1':
            b_type = input("النوع (تجاري/خدمي/سكن): ")
            if my_bank.withdraw(5000):
                new_b = Building(b_type, 5000)
                my_city.add_building(new_b)
                print(Fore.GREEN + "✅ تم البناء!")
            time.sleep(1)

        elif choice == '2':
            pop_sys.add_resident("مهاجر")
            print(Fore.BLUE + "👣 وصل ساكن جديد!")
            time.sleep(1)

        elif choice == '5':
            data = {
                "balance": my_bank.balance,
                "pop_count": len(pop_sys.residents)
            }
            save_mgr.save(data)
            print(Fore.YELLOW + "وداعاً!")
            break

if __name__ == "__main__":
    main_menu()
