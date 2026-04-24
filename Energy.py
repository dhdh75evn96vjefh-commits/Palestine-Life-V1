from Colors import Colors

class EnergyGrid:
    def __init__(self, initial_energy):
        self.total_stored = initial_energy
        self.production = 0  # سيتم حسابه من المباني
        self.consumption = 0
        self.surplus = 0
    
    def update(self, buildings, population_count):
        """تحديث شبكة الطاقة بناءً على حالة المدينة الحالية"""
        
        # 1. حساب الإنتاج والاستهلاك من المباني
        # تذكر: مراكز الطاقة في Config لها قيمة سالبة، لذا سنفصلها
        self.production = sum(abs(b.energy_cost) for b in buildings if b.energy_cost < 0)
        building_consumption = sum(b.energy_cost for b in buildings if b.energy_cost > 0)
        
        # 2. حساب استهلاك السكان (من الإعدادات)
        # أضفنا 0.2 لكل شخص كما فعلت أنت
        pop_consumption = population_count * 0.2
        
        self.consumption = building_consumption + pop_consumption
        
        # 3. تحديث المخزون الكلي
        net_change = self.production - self.consumption
        self.total_stored = max(0, self.total_stored + net_change)
        
        # 4. حساب الفائض (ما زاد عن حاجة التشغيل الفورية)
        self.surplus = max(0, net_change)
        
        # 5. التحذيرات
        if self.total_stored <= 10:
            print(Colors.error("⚠️ انقطاع وشيك للتيار الكهربائي! ابنِ مركز طاقة فوراً."))

    def display(self):
        # تغيير لون الطاقة بناءً على المخزون
        energy_color = Colors.GREEN if self.total_stored > 50 else Colors.YELLOW if self.total_stored > 10 else Colors.RED
        
        print(f"\n{Colors.BLUE}══════════ شبكة الطاقة ══════════")
        print(f"🔋 المخزون الكلي: {energy_color}{self.total_stored:.1f} وحدة")
        print(f"🔌 الإنتاج الحالي: {Colors.GREEN}+{self.production:.1f}")
        print(f"📉 الاستهلاك الكلي: {Colors.RED}-{self.consumption:.1f}")
        print(f"⚖️ صافي الدخل: {Colors.CYAN}{self.surplus - (self.consumption if self.surplus == 0 else 0):.1f}")
        print(f"{Colors.BLUE}════════════════════════════════\n")
