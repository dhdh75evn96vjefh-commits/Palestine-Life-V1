"""
نظام الأحداث العشوائية - Palestine Life
يدير الأحداث المفاجئة التي تؤثر على المدينة
"""
import random
from colors import Colors

class EventManager:
    def __init__(self):
        self.events = [
            # ============ أحداث إيجابية ============
            {
                "name": "موجة حر",
                "message": "⚠️ موجة حر شديدة! استهلاك المياه والكهرباء تضاعف هذا الدور.",
                "type": "negative",
                "effect": "heat_wave",
                "chance": 0.12
            },
            {
                "name": "تبرعات دولية",
                "message": "💰 وصلت تبرعات دولية لدعم إعمار المدينة!",
                "type": "positive",
                "effect": "grant_money",
                "chance": 0.15,
                "money_bonus": (5000, 15000)  # نطاق عشوائي
            },
            {
                "name": "عطل فني",
                "message": "🔧 عطل في محطة الطاقة الرئيسية! الإنتاج انخفض بنسبة 50%.",
                "type": "negative",
                "effect": "power_failure",
                "chance": 0.08,
                "power_penalty": 0.5
            },
            {
                "name": "نمو سياحي",
                "message": "📸 وفد سياحي كبير يزور المدينة! زيادة في الرضا والدخل السياحي.",
                "type": "positive",
                "effect": "tourist_boom",
                "chance": 0.10,
                "tourist_multiplier": 3
            },
            
            # ============ أحداث جديدة ============
            {
                "name": "هطول أمطار غزيرة",
                "message": "🌧️ أمطار غزيرة! خزانات المياه امتلأت بشكل طبيعي، لكن بعض الطرق تضررت.",
                "type": "mixed",
                "effect": "heavy_rain",
                "chance": 0.10,
                "water_bonus": 30,
                "repair_cost": 2000
            },
            {
                "name": "مهرجان القدس",
                "message": "🎉 مهرجان القدس الثقافي يجذب الزوار! إيرادات مضاعفة من السياحة.",
                "type": "positive",
                "effect": "festival",
                "chance": 0.07,
                "revenue_multiplier": 2.5,
                "happiness_bonus": 15
            },
            {
                "name": "هجوم سيبراني",
                "message": "🛡️ محاولة اختراق للنظام البنكي! أنظمة الأمن تتصدى للهجوم.",
                "type": "negative",
                "effect": "cyber_attack",
                "chance": 0.06,
                "max_damage": 5000,
                "min_security_needed": 60
            },
            {
                "name": "افتتاح جامعة",
                "message": "🎓 مستثمرون يفتتحون جامعة جديدة! زيادة في عدد السكان المتعلمين.",
                "type": "positive",
                "effect": "university_opening",
                "chance": 0.08,
                "population_bonus": 20,
                "satisfaction_bonus": 10
            },
            {
                "name": "زلزال خفيف",
                "message": "🏚️ هزة أرضية خفيفة! بعض المباني تحتاج لصيانة عاجلة.",
                "type": "negative",
                "effect": "earthquake",
                "chance": 0.04,
                "damage_per_building": 500
            },
            {
                "name": "اكتشاف أثري",
                "message": "🏺 اكتشاف موقع أثري تاريخي! زيادة في السياحة والاهتمام الدولي.",
                "type": "positive",
                "effect": "archaeological_find",
                "chance": 0.05,
                "tourism_boost": 10,
                "reputation_bonus": 5
            },
            {
                "name": "ارتفاع الأسعار",
                "message": "📈 ارتفاع عالمي في أسعار مواد البناء! تكاليف البناء ×2 هذا الدور.",
                "type": "negative",
                "effect": "inflation",
                "chance": 0.09,
                "cost_multiplier": 2.0
            },
            {
                "name": "معرض تجاري",
                "message": "🏪 معرض فلسطين التجاري الدولي! فرصة لعقود تجارية مربحة.",
                "type": "positive",
                "effect": "trade_fair",
                "chance": 0.11,
                "income_bonus": 3000,
                "commercial_boost": True
            }
        ]
        
        self.event_history = []  # سجل الأحداث
        self.active_event = None
    
    def trigger_random_event(self, game_state):
        """
        تفعيل حدث عشوائي بناءً على الاحتمالات
        game_state: قاموس يحتوي على حالة اللعبة الحالية
        """
        # إعادة تعيين الحدث النشط
        self.active_event = None
        
        # محاولة تفعيل حدث (يتم تفعيل حدث واحد فقط في كل مرة)
        # نعطي فرصة 35% لحدوث أي حدث في هذا الدور
        if random.random() > 0.35:
            return None
        
        # ترتيب الأحداث حسب الأولوية
        available_events = []
        for event in self.events:
            if random.random() < event["chance"]:
                available_events.append(event)
        
        if not available_events:
            return None
        
        # اختيار حدث عشوائي من المتاحين
        self.active_event = random.choice(available_events)
        self.event_history.append(self.active_event)
        
        # عرض الحدث
        print(f"\n{Colors.MAGENTA}╔══════════════════════════════════════╗")
        print(f"║ ✨ حدث مفاجئ ✨                  ║")
        print(f"╚══════════════════════════════════════╝{Colors.RESET}")
        print(f"\n{Colors.YELLOW}[{self.active_event['name']}]{Colors.RESET}")
        print(f"{Colors.CYAN}{self.active_event['message']}{Colors.RESET}\n")
        
        return self.active_event
    
    def apply_event_effects(self, game_state, bank, population, energy, buildings, security):
        """
        تطبيق تأثيرات الحدث على أنظمة اللعبة المختلفة
        """
        if not self.active_event:
            return {}
        
        effect = self.active_event["effect"]
        results = {"message": self.active_event["message"]}
        
        # تطبيق التأثيرات حسب نوع الحدث
        if effect == "heat_wave":
            # استهلاك مضاعف للموارد
            old_food = population.food
            old_water = population.water
            population.food = max(0, population.food - 15)
            population.water = max(0, population.water - 20)
            population.satisfaction = max(0, population.satisfaction - 8)
            results["details"] = f"🍽️ الطعام: {old_food:.1f} → {population.food:.1f}\n💧 الماء: {old_water:.1f} → {population.water:.1f}"
        
        elif effect == "grant_money":
            bonus = random.randint(self.active_event.get("money_bonus", (5000, 15000))[0],
                                   self.active_event.get("money_bonus", (5000, 15000))[1])
            bank.add_funds(bonus)
            results["details"] = f"💰 تم إضافة ${bonus:,} إلى خزينة المدينة"
        
        elif effect == "power_failure":
            penalty = self.active_event.get("power_penalty", 0.5)
            energy.production *= penalty
            results["details"] = f"⚡ إنتاج الطاقة انخفض إلى {energy.production:.1f}"
        
        elif effect == "tourist_boom":
            multiplier = self.active_event.get("tourist_multiplier", 3)
            population.tourists *= multiplier
            # مكافأة مالية من السياحة
            bonus = population.tourists * 100
            bank.add_funds(bonus)
            results["details"] = f"🧳 عدد السياح: {population.tourists}\n💰 إيرادات السياحة: +${bonus:,}"
        
        elif effect == "heavy_rain":
            population.water += self.active_event.get("water_bonus", 30)
            repair_cost = self.active_event.get("repair_cost", 2000)
            if bank.deduct_funds(repair_cost):
                results["details"] = f"💧 الماء: +{self.active_event['water_bonus']}\n🔧 تكاليف الإصلاح: -${repair_cost:,}"
        
        elif effect == "festival":
            revenue_multiplier = self.active_event.get("revenue_multiplier", 2.5)
            happiness_bonus = self.active_event.get("happiness_bonus", 15)
            population.satisfaction = min(100, population.satisfaction + happiness_bonus)
            festival_income = population.tourists * 200 * revenue_multiplier
            bank.add_funds(festival_income)
            results["details"] = f"😊 الرضا: +{happiness_bonus}%\n💰 إيرادات المهرجان: +${festival_income:,.0f}"
        
        elif effect == "cyber_attack":
            min_security = self.active_event.get("min_security_needed", 60)
            max_damage = self.active_event.get("max_damage", 5000)
            
            if security.security_level >= min_security:
                # تم صد الهجوم
                security.threats_blocked += 1
                results["details"] = f"🛡️ تم صد الهجوم بنجاح! (الأمن: {security.security_level}%)"
            else:
                # الهجوم نجح
                damage = random.randint(1000, max_damage)
                bank.deduct_funds(damage)
                results["details"] = f"💔 تم اختراق النظام! الخسائر: -${damage:,}"
        
        elif effect == "university_opening":
            pop_bonus = self.active_event.get("population_bonus", 20)
            sat_bonus = self.active_event.get("satisfaction_bonus", 10)
            population.population += pop_bonus
            population.satisfaction = min(100, population.satisfaction + sat_bonus)
            results["details"] = f"👥 السكان: +{pop_bonus}\n😊 الرضا: +{sat_bonus}%"
        
        elif effect == "earthquake":
            damage_per_building = self.active_event.get("damage_per_building", 500)
            total_damage = len(buildings.buildings) * damage_per_building
            if total_damage > 0:
                bank.deduct_funds(total_damage)
                results["details"] = f"🏚️ عدد المباني المتضررة: {len(buildings.buildings)}\n💸 تكاليف الصيانة: -${total_damage:,}"
            else:
                results["details"] = "🏗️ لا توجد مباني للتضرر - محظوظ!"
        
        elif effect == "archaeological_find":
            tourism_boost = self.active_event.get("tourism_boost", 10)
            reputation = self.active_event.get("reputation_bonus", 5)
            population.tourists += tourism_boost
            population.satisfaction = min(100, population.satisfaction + reputation)
            donation = random.randint(3000, 8000)
            bank.add_funds(donation)
            results["details"] = f"🏺 السياح: +{tourism_boost}\n🌟 السمعة: +{reputation}\n💰 منحة بحثية: +${donation:,}"
        
        elif effect == "inflation":
            cost_multiplier = self.active_event.get("cost_multiplier", 2.0)
            # سيتم تطبيق المضاعف في نظام البناء
            results["details"] = f"📈 تضاعف تكاليف البناء هذا الدور (×{cost_multiplier})"
            results["inflation_active"] = True
        
        elif effect == "trade_fair":
            income_bonus = self.active_event.get("income_bonus", 3000)
            bank.add_funds(income_bonus)
            results["details"] = f"🤝 دخل إضافي من العقود التجارية: +${income_bonus:,}"
        
        return results
    
    def get_event_stats(self):
        """إحصائيات الأحداث"""
        positive = len([e for e in self.event_history if e["type"] == "positive"])
        negative = len([e for e in self.event_history if e["type"] == "negative"])
        mixed = len([e for e in self.event_history if e["type"] == "mixed"])
        
        return {
            "total": len(self.event_history),
            "positive": positive,
            "negative": negative,
            "mixed": mixed,
            "recent": self.event_history[-3:] if self.event_history else []
        }
    
    def display_history(self):
        """عرض سجل الأحداث"""
        print(f"\n{Colors.MAGENTA}═══ سجل الأحداث ═══")
        stats = self.get_event_stats()
        print(f"مجموع الأحداث: {stats['total']}")
        print(f"😊 إيجابية: {stats['positive']} | 😞 سلبية: {stats['negative']} | 😐 مختلطة: {stats['mixed']}")
        
        if stats["recent"]:
            print(f"\n{Colors.CYAN}آخر 3 أحداث:")
            for event in stats["recent"]:
                emoji = "✅" if event["type"] == "positive" else "❌" if event["type"] == "negative" else "⚠️"
                print(f"{emoji} {event['name']}")
        print(f"{Colors.MAGENTA}════════════════════\n")
