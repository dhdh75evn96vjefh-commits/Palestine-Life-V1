class Building:
    def __init__(self, name, b_type, price, capacity):
        """
        إعداد كائن المبنى:
        name: اسم المبنى (مثل: مستشفى القدس)
        b_type: نوع المبنى (تجاري، خدمي، سكن) ليتعرف عليه المحرك الرئيسي
        price: سعر بناء المنشأة (يُخصم من البنك)
        capacity: السعة السكانية التي يوفرها المبنى
        """
        self.name = name
        self.b_type = b_type
        self.price = price
        self.capacity = capacity
        self.is_constructed = False  # الحالة الافتراضية: مخطط فقط
        self.level = 1               # مستوى تطوير المبنى

    def construct(self):
        """تغيير حالة المبنى من مخطط إلى بناء قائم"""
        if not self.is_constructed:
            print(f"🏗️ جاري العمل على بناء {self.name}...")
            self.is_constructed = True
            print(f"✨ اكتمل بناء {self.name} بنجاح!")
        else:
            print(f"⚠️ تنبيه: المبنى '{self.name}' قائم بالفعل ولا يحتاج لبناء.")

    def upgrade(self):
        """تطوير مستوى المبنى لزيادة السعة أو الكفاءة"""
        self.level += 1
        # زيادة السعة بنسبة 20% عند كل تطوير
        self.capacity = int(self.capacity * 1.2)
        print(f"🆙 تم تطوير {self.name} إلى المستوى {self.level}!")
        print(f"👥 السعة الجديدة: {self.capacity}")

    def get_info(self):
        """إرجاع بطاقة المعلومات الخاصة بالمبنى"""
        status = "مكتمل" if self.is_constructed else "تحت الإنشاء"
        return (f"🏢 المنشأة: {self.name}\n"
                f"🏷️ النوع: {self.b_type}\n"
                f"💰 القيمة: {self.price}$\n"
                f"📊 المستوى: {self.level}\n"
                f"🛠️ الحالة: {status}")

# --- جزء لاختبار الكود (اختياري) ---
if __name__ == "__main__":
    # إنشاء تجريبي لمبنى
    test_b = Building("مركز التجارة", "تجاري", 50000, 100)
    print(test_b.get_info())
    test_b.construct()
    test_b.upgrade()
    print(test_b.get_info())
