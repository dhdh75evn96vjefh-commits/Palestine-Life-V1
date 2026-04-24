from building_system import Building
# --- استدعاء كافة الأنظمة الخارجية ---
from building_system import Building
from city_manager import City
from job_system import Engineering, CyberSecurity, Medical
from security import SecuritySystem
from economy import Bank

def main_menu():
    # إعداد الكائنات الأساسية
    my_city = City("فلسطين الحرة")
    sec_sys = SecuritySystem()
    my_bank = Bank(15000) # رصيد البداية (هدية للمطور)
    
    # إعداد المهن
    eng = Engineering("معماري")
    cyber = CyberSecurity("مدير حماية")
    doc = Medical("جراح")

    while True:
        print("\n" + "═"*45)
        print(f" 🏦 الرصيد: {my_bank.get_balance()} $ | 🛡️ الحماية: {sec_sys.firewall_level}")
        
        # محرك التنبيهات الأمنية (عشوائي)
        if sec_sys.scan_for_threats():
            print("⚠️  تنبيه: محاولة اختراق سيبراني مرصودة!")
        else:
            print("✅ حالة الأنظمة: مستقرة وآمنة")

        print(f"--- لوحة إدارة: {my_city.city_name} ---")
        print("1. 🏗️  بناء منشأة (تكلفة 5000)")
        print("2. 🗺️  عرض خريطة المدينة")
        print("3. 🛡️  تفعيل بروتوكول الحماية (ربح 2000)")
        print("4. 🏥  فحص القطاع الصحي")
        print("5. 🚪  خروج وحفظ")
        print("═"*45)

        choice = input("ما هو إجراءك القادم؟ : ")

        if choice == "1":
            if my_bank.withdraw(5000):
                name = input("اسم المبنى: ")
                b_type = input("النوع (سكن/مستشفى/برج): ")
                new_b = Building(name, b_type, 5000, 100)
                my_city.add_building(new_b)
                new_b.construct()
            
        elif choice == "2":
            my_city.show_all_buildings()
            
        elif choice == "3":
            print(cyber.secure_system())
            sec_sys.firewall_level += 1
            my_bank.deposit(2000)
            print("💰 تمت إضافة مكافأة الأمان لرصيدك.")

        elif choice == "4":
            print(doc.heal())
            print("👨‍⚕️ حالة السكان: ممتازة.")

        elif choice == "5":
            print("💾 جاري الحفظ... نراك قريباً في فلسطين الحرة!")
            break
        else:
            print("❌ خيار غير صحيح!")

if __name__ == "__main__":
    main_menu()
