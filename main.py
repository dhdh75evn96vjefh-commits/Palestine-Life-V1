from building_system import Building
from city_manager import City
from job_system import Engineering, CyberSecurity, Medical
from security import SecuritySystem
from economy import Bank
from population import PopulationManager

def main_menu():
    my_city = City("فلسطين الحرة")
    sec_sys = SecuritySystem()
    my_bank = Bank(20000)
    pop_sys = PopulationManager()
    
    # تعريف المختصين
    cyber = CyberSecurity("مدير حماية")
    doc = Medical("جراح")

    while True:
        # محاكاة مرور الوقت وتأثيره على السكان
        # نتحقق إذا كان هناك "مبنى تجاري" (مطعم) لتغذية السكان
        has_food = any(b.b_type == "تجاري" for b in my_city.buildings)
        pop_sys.simulate_hour(has_food)
        
        # حساب إحصائيات السكان
        total_pop = len(pop_sys.residents)
        avg_energy = sum(r.energy for r in pop_sys.residents) / total_pop if total_pop > 0 else 0
        
        print("\n" + "═"*55)
        print(f"🕒 الساعة: {pop_sys.game_hour}:00 | 💰 الرصيد: {my_bank.get_balance()} $")
        print(f"👥 السكان: {total_pop} | 🔋 طاقة الشعب: {avg_energy:.1f}% | 🛡️ الأمن: {sec_sys.firewall_level}")
        
        if sec_sys.scan_for_threats():
            print("⚠️  تنبيه أمني: هجوم سيبراني مرصود!")
            
        print("-" * 25)
        print("1. 🏗️  بناء منشأة (التكلفة 5000 $)")
        print("2. 👥  إضافة سكان (هجرة للمدينة)")
        print("3. 🛡️  تأمين النظام (ربح 2000 $)")
        print("4. 📊  عرض تقرير المدينة المفصل")
        print("5. 🚪  خروج وحفظ")
        print("═"*55)

        choice = input("ما هو قرارك القادم؟ : ")

        if choice == "1":
            if my_bank.withdraw(5000):
                name = input("اسم المبنى: ")
                # تأكد من كتابة "تجاري" لكي يأكل السكان
                b_type = input("النوع (سكن/تجاري/مستشفى): ")
                new_b = Building(name, b_type, 5000, 100)
                my_city.add_building(new_b)
                new_b.construct()
                if b_type == "سكن":
                    pop_sys.add_residents(10)
                    print("🏠 انتقل 10 سكان جدد للعيش في المدينة!")
            
        elif choice == "2":
            pop_sys.add_residents(5)
            print("👨‍👩‍👧‍👦 رحب بـ 5 سكان جدد في مدينتك.")

        elif choice == "3":
            print(cyber.secure_system())
            sec_sys.firewall_level += 1
            my_bank.deposit(2000)

        elif choice == "4":
            my_city.show_all_buildings()
            if total_pop > 0:
                print(f"\n📊 حالة أول ساكن ({pop_sys.residents[0].name}):")
                print(f"   الجوع: {pop_sys.residents[0].hunger} | الطاقة: {pop_sys.residents[0].energy}")
            else:
                print("\n⚠️ لا يوجد سكان حالياً، ابنِ 'سكن' لجذبهم!")

        elif choice == "5":
            print("💾 جاري الحفظ.. نراك في النسخة القادمة!")
            break

if __name__ == "__main__":
    main_menu()
