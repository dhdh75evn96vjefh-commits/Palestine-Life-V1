from building_system import Building
from city_manager import City
from job_system import Engineering, CyberSecurity # تم إضافة الأمن هنا
from security import SecuritySystem # تأكد أنك أنشأت ملف security.py

def main_menu():
    my_city = City("فلسطين الحرة")
    sec_sys = SecuritySystem()
    
    # تعيين خبير أمن افتراضي لإدارة النظام
    cyber_expert = CyberSecurity("مدير حماية")
    
    while True:
        print("\n" + "="*30)
        # فحص أمني تلقائي عند كل دورة في البرنامج
        if sec_sys.scan_for_threats():
            print("⚠️ تنبيه أمني خطير: محاولة اختراق للنظام الاقتصادي!")
            print(f"درع الحماية الحالي: المستوى {sec_sys.firewall_level}")
        else:
            print("🛡️ حالة النظام: آمن ومستقر")
            
        print(f"--- لوحة تحكم {my_city.city_name} ---")
        print("1. إنشاء مبنى جديد")
        print("2. عرض خريطة المدينة")
        print("3. تفعيل بروتوكولات الحماية (خاص بخبير الأمن)")
        print("4. خروج")
        
        choice = input("اختر رقم العملية: ")

        if choice == "1":
            name = input("اسم المبنى: ")
            b_type = input("النوع (سكن/صحي/تجاري): ")
            price = int(input("التكلفة: "))
            cap = int(input("السعة: "))
            
            new_b = Building(name, b_type, price, cap)
            my_city.add_building(new_b)
            new_b.construct()
                
        elif choice == "2":
            my_city.show_all_buildings()
            
        elif choice == "3":
            # هنا يستخدم خبير الأمن مهاراته لرفع الحماية
            print(cyber_expert.secure_system())
            sec_sys.firewall_level += 1
            print(f"🛡️ تم تعزيز الجدار الناري بنجاح. المستوى الجديد: {sec_sys.firewall_level}")

        elif choice == "4":
            print("جاري حفظ البيانات والخروج... إلى اللقاء!")
            break
