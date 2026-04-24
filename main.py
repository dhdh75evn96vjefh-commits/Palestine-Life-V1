# --- استدعاء كافة الأنظمة ---
try:
    from building_system import Building
    from city_manager import City
    from job_system import Engineering, CyberSecurity, Medical
    from security import SecuritySystem
    from economy import Bank
    from population import PopulationManager
except ImportError as e:
    print(f"❌ خطأ: تأكد من وجود جميع الملفات في المجلد! ({e})")

def main_menu():
    # 1. إعداد الأنظمة الأساسية
    my_city = City("فلسطين الحرة")
    sec_sys = SecuritySystem()
    my_bank = Bank(25000)  # ميزانية البداية
    pop_sys = PopulationManager()
    
    # 2. تعريف المختصين (الوظائف)
    cyber = CyberSecurity("مدير حماية")
    eng = Engineering("مهندس معماري")

    while True:
        # --- محرك الحياة (Life Engine) ---
        # فحص توفر المطاعم (تجاري) ومحطات المياه (خدمي)
        has_food = any(b.b_type == "تجاري" for b in my_city.buildings)
        has_water = any(b.b_type == "خدمي" for b in my_city.buildings)
        
        # محاكاة الساعة وتأثيرها على السكان
        pop_sys.simulate_hour(has_food, has_water)
        
        # تحصيل ضرائب تلقائية (50$ من كل ساكن كل ساعة لتمويل المدينة)
        if len(pop_sys.residents) > 0:
            tax = len(pop_sys.residents) * 50
            my_bank.deposit(tax)

        # 3. واجهة المستخدم (UI)
        print("\n" + "═"*60)
        total_pop = len(pop_sys.residents)
        avg_energy = sum(r.energy for r in pop_sys.residents) / total_pop if total_pop > 0 else 0
        
        print(f"🕒 الساعة: {pop_sys.game_hour}:00 | 💰 الخزينة: {my_bank.get_balance()} $")
        print(f"👥 السكان: {total_pop} | 🔋 الطاقة: {avg_energy:.1f}% | 🛡️ الأمن: {sec_sys.firewall_level}")
        
        # نظام التنبيهات الأمنية
        if sec_sys.scan_for_threats():
            print("⚠️ [تنبيه]: رصد محاولة اختراق للأنظمة المالية!")
        else:
            print("✅ [النظام]: الحالة الأمنية مستقرة")
            
        print("-" * 30)
        print("1. 🏗️  بناء منشأة (5000$) - [سكن/تجاري/خدمي/مستشفى]")
        print("2. 🛡️  تفعيل بروتوكول حماية (+2000$ مكافأة أمنية)")
        print("3. 📊  تقرير السكان والمدينة (مراقبة الجوع والعطش)")
        print("4. 👥  جذب مهاجرين جدد (إضافة سكان يدوياً)")
        print("5. 🚪  خروج وحفظ التقدم")
        print("═"*60)
        
        choice = input("اختر الإجراء القادم: ")

        if choice == "1":
            if my_bank.withdraw(5000):
                name = input("اسم المبنى: ")
                print("أنواع المباني: (سكن: يجذب ناس | تجاري: يوفر أكل | خدمي: يوفر ماء)")
                b_type = input("النوع: ")
                new_b = Building(name, b_type, 5000, 100)
                my_city.add_building(new_b)
                new_b.construct()
                
                if b_type == "سكن":
                    pop_sys.add_residents(10)
                    print("🏠 انتقل 10 سكان جدد للعيش في مدينتك!")
            
        elif choice == "2":
            print(cyber.secure_system())
            sec_sys.firewall_level += 1
            my_bank.deposit(2000)
            print("💰 تم إيداع مكافأة الحماية في الخزينة.")

        elif choice == "3":
            my_city.show_all_buildings()
            if total_pop > 0:
                print(f"\n📊 حالة عينة من السكان ({pop_sys.residents[0].name}):")
                print(f"   الحالة: {pop_sys.residents[0].status}")
                print(f"   الجوع: {pop_sys.residents[0].hunger}/100 | العطش: {pop_sys.residents[0].thirst}/100")
            else:
                print("\n⚠️ لا يوجد سكان في المدينة حالياً.")

        elif choice == "4":
            pop_sys.add_residents(5)
            print("👨‍👩‍👧‍👦 رحب بـ 5 سكان جدد في المدينة.")

        elif choice == "5":
            print("💾 جاري الحفظ.. نراك لاحقاً في فلسطين الحرة!")
            break
        else:
            print("❌ اختيار غير صحيح!")

if __name__ == "__main__":
    main_menu()
# --- داخل حلقة المحاكاة في main.py ---

# فحص إذا كان هناك مستشفى في المدينة
has_hospital = any(b.b_type == "مستشفى" for b in my_city.buildings)

# محاكاة حدث عشوائي (ظهور مرض)
if random.random() < 0.05: # احتمالية 5% ظهور مرض كل ساعة
    print("🚨 تنبيه صحي: انتشرت عدوى موسمية في المدينة!")
    for r in pop_sys.residents:
        r.energy -= 20 # المرض ينهك الطاقة

# إذا وجد مستشفى، يتم علاج السكان تلقائياً
if has_hospital:
    for r in pop_sys.residents:
        r.energy = min(100, r.energy + 10)
