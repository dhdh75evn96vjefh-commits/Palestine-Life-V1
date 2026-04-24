from building_system import Building
from city_manager import City
from job_system import Engineering, CyberSecurity
from security import SecuritySystem

def main_menu():
    my_city = City("فلسطين الحرة")
    sec_sys = SecuritySystem()
    
    # --- نظام المال الجديد ---
    balance = 20000  # الميزانية الافتتاحية 20 ألف
    
    while True:
        print("\n" + "="*40)
        print(f"💰 ميزانية المدينة الحالية: {balance} شيكل")
        
        # فحص الأمن
        if sec_sys.scan_for_threats():
            print("⚠️  تنبيه أمني: محاولة اختراق!")
        else:
            print("🛡️  حالة النظام: آمن")
            
        print("-" * 10)
        print("1. بناء مبنى جديد (تكلفة: 5000)")
        print("2. عرض خريطة المدينة")
        print("3. العمل كخبير أمن (ربح: 1500)")
        print("4. خروج")
        print("="*40)
        
        choice = input("ماذا تريد أن تفعل؟ أدخل الرقم: ")

        if choice == "1":
            if balance >= 5000:
                name = input("اسم المبنى الجديد: ")
                new_b = Building(name, "عام", 5000, 100)
                my_city.add_building(new_b)
                new_b.construct()
                balance -= 5000 # خصم المبلغ
                print(f"✅ تم البناء. الرصيد المتبقي: {balance}")
            else:
                print("❌ عذراً، لا تملك مالاً كافياً للبناء!")
                
        elif choice == "2":
            my_city.show_all_buildings()
            
        elif choice == "3":
            # محاكاة عمل خبير الأمن
            print("🛡️ جاري تأمين السيرفرات...")
            balance += 1500 # إضافة الراتب
            print(f"💸 أحسنت! كسبت 1500 شيكل. الرصيد الجديد: {balance}")

        elif choice == "4":
            print("جاري إغلاق الأنظمة... وداعاً!")
            break
