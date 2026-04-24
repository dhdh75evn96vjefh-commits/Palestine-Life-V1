import random
from Colors import Colors

class SecuritySystem:
    def __init__(self, initial_security):
        self.security_level = initial_security
        self.threats_blocked = 0
        self.total_damages = 0 # سجل إجمالي الخسائر
    
    def scan_threats(self, bank, buildings):
        """فحص التهديدات وخصم الضرر من البنك إذا نجح الهجوم"""
        
        # زيادة فرصة الهجوم إذا كان الرصيد مرتفعاً (الهجمات تستهدف الأغنياء!)
        base_chance = 0.2
        if bank.balance > 50000: base_chance = 0.4
        
        if random.random() < base_chance:
            # قوة الهجوم عشوائية
            threat_power = random.randint(10, 100)
            
            # إذا كان مستوى الأمان أقل من قوة التهديد، ينجح الهجوم
            if threat_power > self.security_level:
                damage = random.randint(1000, 5000)
                # خصم الضرر مباشرة من البنك
                bank.deduct_funds(damage)
                self.total_damages += damage
                
                print(f"\n{Colors.RED}🚨 [هجوم سيبراني ناجح!]")
                print(Colors.error(f"تم اختراق النظام البنكي وخصم: ${damage:,.2f}"))
                return damage
            else:
                self.threats_blocked += 1
                print(f"\n{Colors.GREEN}🛡️ [نظام الأمان]: تم صد محاولة اختراق بنجاح!")
                return 0
        return 0
    
    def update_security_level(self, buildings):
        """تحديث مستوى الأمان بناءً على وجود 'مركز_أمني'"""
        security_centers = [b for b in buildings if b.type == "مركز_أمني"]
        # كل مركز أمني يرفع المستوى الأساسي بـ 20 نقطة
        bonus = len(security_centers) * 20
        self.security_level = min(100, 40 + bonus) # 40 هو الأمان الأساسي

    def display(self):
        # تغيير اللون بناءً على خطورة المستوى
        status_color = Colors.GREEN if self.security_level > 70 else Colors.YELLOW if self.security_level > 40 else Colors.RED
        
        print(f"\n{Colors.RED}══════════ المركز الأمني ══════════")
        print(f"🛡️ مستوى الحماية: {status_color}{self.security_level}/100")
        print(f"⚔️ هجمات تم صدها: {Colors.CYAN}{self.threats_blocked}")
        if self.total_damages > 0:
            print(f"💸 إجمالي الخسائر: {Colors.RED}${self.total_damages:,.2f}")
        print(f"{Colors.RED}══════════════════════════════════\n")
