 # --- استدعاء الأنظمة (بدون تكرار) ---
from building_system import Building
from city_manager import City
from job_system import Engineering, CyberSecurity, Medical
from security import SecuritySystem
from economy import Bank

def main_menu():
    # 1. إعداد المدينة والأنظمة المالية والأمنية
    my_city = City("فلسطين الحرة")
    sec_sys = SecuritySystem()
    my_bank = Bank(20000)  # رصيد البداية لدعم تطوير المدينة
    
    # 2. تجهيز الطاقم المهني
    eng = Engineering("معماري")
    cyber = CyberSecurity("مدير حماية")
    doc = Medical("جراح")

    while True:
        print("\n" + "═"*50)
        # عرض شريط الحالة العلوي
        current_balance = my_bank.get_balance()
        print(f"💰 الميزانية: {current_balance} $ | 🛡️ مستوى الحماية: {sec_sys.firewall_level}")
        
        # محرك الفحص الأمني التلقائي
        if sec_sys.scan_for_threats():
            print("⚠️  [تنبيه أمني]: رصد محاولة اختراق نشطة!")
        else:
            print("✅ [النظام]: الحالة مستقرة")
            
        print("-" * 20)
        print(f"--- لوحة تحكم: {my_city.city_name} ---")
        print("1. 🏗️  بناء منشأة جديدة (التكلفة: 5000 $)")
        print("2. 🗺️  عرض خريطة المدينة والمباني")
        print("3. 🛡️  تأمين الأنظمة (مهمة الأمن - ربح 2000 $)")
        print("4. 🏥  فحص القطاع الصحي (مهمة الطبيب)")
        print("5. 🚪  خروج وحفظ التقدم")
        print("═"*50)
        
        choice = input("ما هو إجراءك القادم؟ : ")

        if choice == "1":
            if my_bank.withdraw(5000):
                name = input("اسم المبنى: ")
                b_type = input("النوع (سكن/تجاري/حكومي): ")
                new_b = Building(name, b_type, 5000, 100)
                my_city.add_building(new_b)
                new_b.construct()
                print(f"✨ تم بناء {name} وإضافته للمخطط.")
            
        elif choice == "2":
            my_city.show_all_buildings()
            
        elif choice == "3":
            # تفعيل مهارات الأمن السيبراني
            print(cyber.secure_system())
            sec_sys.firewall_level += 1
            my_bank.deposit(2000) # راتب مقابل الحماية
            print("💰 تم إيداع مكافأة الحماية في رصيدك.")

        elif choice == "4":
            # تفعيل مهارات الطبيب
            print(doc.heal())
            print("👨‍⚕️ التقرير الطبي: المدينة آمنة صحياً.")

        elif choice == "5":
            print("💾 جاري حفظ البيانات... نراك لاحقاً في فلسطين الحرة!")
            break
        else:
            print("❌ خيار غير صحيح، حاول مرة أخرى.")

if __name__ == "__main__":
    main_menu()
