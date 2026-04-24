from building_system import Building
from city_manager import City
from job_system import Engineering, Medical

def main_menu():
    my_city = City("فلسطين الحرة")
    # إنشاء موظف افتراضي لتبدأ به
    engineer = Engineering("معماري")
    
    while True:
        print("\n" + "="*30)
        print(f" مرحباً بك في لوحة تحكم {my_city.city_name} ")
        print("="*30)
        print("1. إنشاء مبنى جديد")
        print("2. عرض خريطة المدينة")
        print("3. الاستعلام عن ميزانية المشروع")
        print("4. خروج")
        
        choice = input("اختر رقم العملية: ")

        if choice == "1":
            name = input("اسم المبنى: ")
            b_type = input("نوع المبنى (سكن/تجاري/صحي): ")
            price = int(input("تكلفة البناء: "))
            capacity = int(input("السعة: "))
            
            new_b = Building(name, b_type, price, capacity)
            my_city.add_building(new_b)
            
            confirm = input("هل تريد البدء بالبناء الآن؟ (نعم/لا): ")
            if confirm == "نعم":
                new_b.construct()
                
        elif choice == "2":
            my_city.show_all_buildings()
            
        elif choice == "3":
            print(f"إجمالي القيمة الاستثمارية للمباني: {my_city.total_value()}")
            print(f"راتب المهندس الحالي: {engineer.salary}")

        elif choice == "4":
            print("جاري حفظ البيانات والخروج... وداعاً!")
            break
        else:
            print("اختيار غير صحيح، حاول مرة أخرى.")

if __name__ == "__main__":
    main_menu()


