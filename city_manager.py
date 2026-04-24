from building_system import Building

class City:
    def __init__(self, city_name):
        self.city_name = city_name
        # غيرنا الاسم من buildings_list إلى buildings ليتطابق مع main.py
        self.buildings = [] 

    def add_building(self, building_obj):
        """إضافة مبنى جديد للمدينة"""
        self.buildings.append(building_obj)
        print(f"تم إضافة {building_obj.b_type} إلى مدينة {self.city_name}")

    def show_all_buildings(self):
        """عرض حالة كل المباني"""
        print(f"--- خريطة مباني مدينة {self.city_name} ---")
        for b in self.buildings:
            print(b.get_info())
