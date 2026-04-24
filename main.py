from building_system import Building
from city_manager import City
from job_system import Engineering, Medical

def start_simulation():
    print("--- مرحباً بك في مشروع معدن فلسطين (النسخة الأولى) ---")
    
    # 1. إنشاء المدينة
    my_city = City("فلسطين الحرة")

    # 2. إنشاء شخصية مهندس معماري
    engineer_job = Engineering("معماري")
    print(f"تم تعيين مهندس معماري براتب: {engineer_job.salary}")

    # 3. إنشاء مبنى جديد كمخطط
    new_hospital = Building("مستشفى الشفاء", "صحي", 120000, 300)
    
    # 4. إضافة المبنى للمدينة
    my_city.add_building(new_hospital)

    # 5. استخدام صلاحيات المهندس للبناء
    print(engineer_job.get_permit())
    new_hospital.construct()

    # 6. عرض حالة المدينة النهائية
    my_city.show_all_buildings()

if __name__ == "__main__":
    start_simulation()

