from Colors import Colors

class Bank:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.deposits = 0
        self.loans = 0
        self.interest_rate = 0.05 # فائدة 5%
    
    def deposit(self, amount):
        """تحويل المال من الكاش إلى الوديعة"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.deposits += amount
            return True, Colors.success(f"تم إيداع ${amount:,.2f} في حسابك.")
        return False, Colors.error("المبلغ غير متوفر في رصيدك الحالي!")
    
    def withdraw(self, amount):
        """سحب المال من الوديعة إلى الكاش"""
        if amount > 0 and amount <= self.deposits:
            self.deposits -= amount
            self.balance += amount
            return True, Colors.success(f"تم سحب ${amount:,.2f} إلى محفظتك.")
        return False, Colors.error("لا تملك هذا المبلغ في ودائعك!")
    
    def apply_interest(self):
        """إضافة أرباح على الودائع (تُستدعى في كل دورة زمنية)"""
        if self.deposits > 0:
            profit = self.deposits * self.interest_rate
            self.deposits += profit
            return f"📈 أرباح بنكية: تم إضافة ${profit:,.2f} لودائعك."
        return None

    def display(self):
        print(f"\n{Colors.YELLOW}═══════ الحساب البنكي ═══════")
        print(f"💰 الكاش (في الجيب): {Colors.GREEN}${self.balance:,.2f}")
        print(f"🏦 الودائع (في البنك): {Colors.CYAN}${self.deposits:,.2f}")
        print(f"📉 القروض المطلوبة: {Colors.RED}${self.loans:,.2f}")
        print(f"{Colors.YELLOW}════════════════════════════\n")
