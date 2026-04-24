import os
from colorama import Fore, Style, init
from save_system import SaveManager
from events import WorldEvents

init(autoreset=True) # تفعيل الألوان تلقائياً
save_mgr = SaveManager()
weather = WorldEvents()

# عند تشغيل اللعبة، حاول تحميل الحفظ
saved_data = save_mgr.load()
if saved_data:
    print(f"{Fore.GREEN}♻️ تم استعادة بيانات المدينة السابقة!")
    # هنا تضع منطق استرجاع الرصيد والسكان من saved_data

while True:
    os.system('clear') # تنظيف الشاشة لجعل الواجهة أجمل
    current_env = weather.update_event()
    
    print(f"{current_env['color']}{'='*40}")
    print(f"{current_env['color']}📍 حدث الآن: {current_env['msg']}")
    print(f"{current_env['color']}{'='*40}")
    
    print(f"{Fore.GREEN}💰 الخزينة: {my_bank.balance} $")
    print(f"{Fore.CYAN}👥 السكان: {len(pop_sys.residents)}")
    print(f"{Fore.YELLOW}⚡ الطاقة: {'مستقرة' if util.is_online else 'منقطعة'}")
    print("-" * 40)
    print(f"{Fore.WHITE}1. بناء | 2. تأمين | 3. تقرير | 4. هجرة | 5. حفظ وخروج")
    
    choice = input(f"{Fore.MAGENTA}🎮 اختر قرارك: ")
    
    if choice == '5':
        # منطق الحفظ قبل الخروج
        data_to_save = {"balance": my_bank.balance, "pop_count": len(pop_sys.residents)}
        save_mgr.save(data_to_save)
        break
import os
import random
import time
from building_system import Building
from city_manager import City
from job_system import Engineering, CyberSecurity, Medical
from security import SecuritySystem
from economy import Bank
from population import PopulationManager
from utilities import PowerGrid

def main_menu():
    # 1. إعداد الأنظمة الأساسية
    my_city = City("فلسطين الحرة")
    sec_sys = SecuritySystem()
    my_bank = Bank(35000) # رصيدك الحالي من الصور
    pop_sys = PopulationManager()
    power_sys = PowerGrid()
    
    # 2. تعريف المختصين
    cyber = CyberSecurity("مدير حماية")
    eng = Engineering("مهندس معماري")
    
    while True:
        # تنظيف الشاشة لجعل الواجهة احترافية
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # عرض شريط الحالة العلوي
        total_pop = len(pop_sys.residents)
        print("="*60)
        print(f"🏙️  المدينة: {my_city.name} | 💰 البنك: {my_bank.balance} $ | 👥 السكان: {total_pop}")
        print(f"⚡ الطاقة: {'متصلة' if power_sys.is_online else 'مقطوعة'} | 🛡️ الحماية: {sec_sys.firewall_level}")
        print("="*60)

        # محاكة الحياة (Life Engine)
        has_food = any(b.b_type == "تجاري" for b in my_city.buildings)
        has_water = any(b.b_type == "خدمي" for b in my_city.buildings)
        has_hospital = any(b.b_type == "مستشفى" for b in my_city.buildings)

        # تحديث حالة السكان (الجوع، العطش، الصحة)
        pop_sys.simulate_hour(has_food, has_water)

        # منطق الكهرباء وتأثيره على المستشفى
        if has_hospital and power_sys.is_online:
            for r in pop_sys.residents:
                r.energy = min(100, r.energy + 10)

        # تحصيل الضرائب ($50 لكل ساكن)
        if total_pop > 0:
            tax_income = total_pop * 50
            my_bank.deposit(tax_income)

        # عرض القائمة
        print("\n--- لوحة التحكم في المدينة ---")
        print("1. 🏗️ بناء منشأة (سكن، تجاري، خدمي، مستشفى)")
        print("2. 🛡️ تأمين النظام (رفع الحماية + مكافأة)")
        print("3. 📊 تقرير المدينة (حالة السكان والمباني)")
        print("4. 👨‍👩‍👧‍👦 جذب مهاجرين جُدد")
        print("5. ⚡ إدارة محطة الطاقة")
        print("6. 🚪 حفظ وخروج")
        
        choice = input("\n📥 اختر إجراءً: ")

        if choice == "1":
            b_type = input("نوع المبنى: ")
            cost = 5000
            # ميزة المهندس: تقليل التكلفة
            if any(isinstance(r, Engineering) for r in pop_sys.residents):
                cost = 4000
            
            if my_bank.balance >= cost:
                my_bank.balance -= cost
                my_city.add_building(Building(b_type))
                print(f"✅ تم بناء {b_type} بنجاح!")
            else:
                print("❌ لا يوجد رصيد كافٍ!")

        elif choice == "2":
            print(cyber.secure_system())
            sec_sys.firewall_level += 1
            my_bank.deposit(2000)

        elif choice == "3":
            my_city.show_all_buildings()
            if total_pop > 0:
                print(f"\n📊 حالة عينة من السكان: {pop_sys.residents[0].status}")
            input("\nاضغط Enter للعودة...")

        elif choice == "4":
            pop_sys.add_residents(5)
            print("🆕 رحب بـ 5 سكان جُدد في المدينة!")

        elif choice == "5":
            if my_bank.balance >= 10000:
                my_bank.balance -= 10000
                print(power_sys.build_power_plant())
            else:
                print("❌ بناء محطة الطاقة يحتاج 10,000 $")

        elif choice == "6":
            print("💾 جاري حفظ التقدم في فلسطين الحرة...")
            break
        
        time.sleep(1)

if __name__ == "__main__":
    main_menu()
