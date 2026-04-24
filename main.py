import os
import time
import random
from colorama import Fore, Style, init

# استدعاء الأنظمة من ملفاتك التي رفعتها
from building_system import Building
from city_manager import City
from job_system import Engineering, CyberSecurity, Medical
from security import SecuritySystem
from economy import Bank
from population import PopulationManager
from utilities import PowerGrid
from save_system import SaveManager # الملف الجديد

# تفعيل الألوان
init(autoreset=True)
save_mgr = SaveManager()

def main_menu():
    # 1. إعداد الأنظمة الأساسية
    my_city = City("فلسطين الحرة")
    sec_sys = SecuritySystem()
    pop_sys = PopulationManager()
    power_sys = PowerGrid()
    
    # تحويل رصيد البداية (تحميل الحفظ إذا وجد)
    saved_data = save_mgr.load()
    if saved_data:
        my_bank = Bank(saved_data.get('balance', 35000))
        # ملاحظة: يمكن تطوير نظام السكان ليحفظ القائمة كاملة لاحقاً
    else:
        my_bank = Bank(35000)

    # 2. تعريف المختصين
    cyber = CyberSecurity("مدير حماية")
    eng = Engineering("مهندس معماري")

    while True:
        # تنظيف الشاشة لجعل الواجهة احترافية
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # --- محرك الحياة (Life Engine) ---
        has_food = any(b.b_type == "تجاري" for b in my_city.buildings)
        has_water = any(b.b_type == "خدمي" for b in my_city.buildings)
        has_hospital = any(b.b_type == "مستشفى" for b in my_city.buildings)
        
        # تحديث حالة السكان
        pop_sys.simulate_hour(has_food, has_water)
        
        # الضرائب: 50$ من كل ساكن كل ساعة
        total_pop = len(pop_sys.residents)
        if total_pop > 0:
            tax = total_pop * 50
            my_bank.deposit(tax)

        # --- واجهة المستخدم (UI) الملونة ---
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.GREEN}💰 الخزينة: {my_bank.balance} $ | {Fore.WHITE}👥 السكان: {total_pop}")
        print(f"{Fore.YELLOW}⚡ الطاقة: {'نشطة' if power_sys.is_online else 'منقطعة'} | {Fore.RED}🛡️ الأمن: مستوى {sec_sys.firewall_level}")
        print(f"{Fore.CYAN}{'='*60}")

        # عرض تنبيهات بسيطة
        if not has_food: print(f"{Fore.RED}⚠️ تحذير: لا توجد مطاعم! السكان جائعون.")
        if total_pop == 0: print(f"{Fore.RED}💀 المدينة مهجورة! اضغط 4 لجذب المهاجرين.")

        print(f"\n{Fore.WHITE}1. 🏗️ بناء منشأة (5000$)")
        print("2. 🛡️ تأمين النظام (2000$)")
        print("3. 📋 تقرير المدينة المفصل")
        print("4. 👣 جذب مهاجرين جُدد")
        print(f"{Fore.YELLOW}5. 💾 حفظ التقدم والخروج")
        print(f"{Fore.CYAN}{'='*60}")

        choice = input(f"{Fore.MAGENTA}🎮 قرارك يا مدير: ")

        if choice == '1':
            b_type = input("نوع المبنى (تجاري/خدمي/مستشفى/سكن): ")
            if my_bank.withdraw(5000):
                new_b = Building(b_type, 5000)
                my_city.add_building(new_b)
                print(f"{Fore.GREEN}✅ تم بناء {b_type} بنجاح!")
            else:
                print(f"{Fore.RED}❌ لا تملك مالاً كافياً!")
            time.sleep(1.5)

        elif choice == '2':
            if my_bank.withdraw(2000):
                sec_sys.upgrade_firewall()
                my_bank.deposit(1000) # مكافأة أمنية
                print(f"{Fore.BLUE}🛡️ تم تعزيز الحماية!")
            time.sleep(1)

        elif choice == '4':
            # إضافة 5 سكان جدد
            for _ in range(5):
                pop_sys.add_resident("مواطن جديد")
            print(f"{Fore.CYAN}👣 رحبوا بالمنضمين الجدد للمدينة!")
            time.sleep(1)

        elif choice == '5':
            # حفظ البيانات قبل الخروج
            data = {
                "balance": my_bank.balance,
                "pop_count": len(pop_sys.residents)
            }
            save_mgr.save(data)
            print(f"{Fore.GREEN}👋 تم الحفظ.. نراك لاحقاً في فلسطين الحرة!")
            break

if __name__ == "__main__":
    main_menu()
