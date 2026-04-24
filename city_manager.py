from building_system import Building

class City:
    def __init__(self, city_name):
        self.city_name = city_name
        self.buildings_list = [] # قائمة لتخزين كل المباني

    def add_building(self, building_obj):
        """إضافة مبنى جديد للمدينة"""
        self.buildings_list.append(building_obj)
        print(f"تم إضافة {building_obj.name} إلى مخطط مدينة {self.city_name}.")

    def show_all_buildings(self):
        """عرض حالة كل المباني في المدينة"""
        print(f"\n--- خريطة مباني مدينة {self.city_name} ---")
        for b in self.buildings_list:
            print(b.get_info())

    def total_value(self):
        """حساب القيمة الإجمالية للعقارات في المدينة"""
        total = sum(b.price for b in self.buildings_list)
        return total

# --- تجربة إدارة المدينة ---
if __name__ == "__main__":
    my_city = City("فلسطين الحرة")

    # إنشاء مبانٍ مختلفة
    b1 = Building("مستشفى القدس", "صحي", 100000, 200)
    b2 = Building("مدرسة المتفوقين", "تعليمي", 45000, 500)
    b3 = Building("سوق المدينة", "تجاري", 75000, 1000)

    # إضافة المباني للمدينة
    my_city.add_building(b1)
    my_city.add_building(b2)
    my_city.add_building(b3)

    # عرض الإحصائيات
    my_city.show_all_buildings()
    print(f"\nإجمالي قيمة العقارات في المدينة: {my_city.total_value()} عملة.")

