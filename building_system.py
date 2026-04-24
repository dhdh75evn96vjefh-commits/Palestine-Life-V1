class Building:
    def __init__(self, name, b_type, price, capacity):
        self.name = name          # اسم المبنى (مثل: برج القدس)
        self.b_type = b_type      # نوعه (سكن، تجاري، مستشفى)
        self.price = price        # سعره بالعملة الافتراضية
        self.capacity = capacity  # كم شخص يتسع
        self.is_constructed = False # هل تم بناؤه أم لا يزال مخططاً

    def construct(self):
        """وظيفة لبدء عملية البناء"""
        if not self.is_constructed:
            print(f"جاري بناء {self.name}...")
            self.is_constructed = True
            print(f"تم الانتهاء من بناء {self.name} بنجاح!")
        else:
            print(f"المبنى {self.name} قائم بالفعل.")

    def get_info(self):
        """عرض معلومات المبنى"""
        status = "مكتمل" if self.is_constructed else "تحت الإنشاء"
        return f"المبنى: {self.name} | النوع: {self.b_type} | الحالة: {status}"

# --- تجربة الكود ---
if __name__ == "__main__":
    # إنشاء أول مبنى في مشروعنا
    my_building = Building("مركز التجارة", "تجاري", 50000, 100)
    print(my_building.get_info())
    
    # تنفيذ عملية البناء
    my_building.construct()
    print(my_building.get_info())
