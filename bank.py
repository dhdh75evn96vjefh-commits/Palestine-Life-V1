from colors import Colors

class Bank:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.deposits = 0
        self.loans = 0
        self.interest_rate = 0.05
    
    def deposit(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.deposits += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.deposits:
            self.deposits -= amount
            self.balance += amount
            return True
        return False
    
    def add_funds(self, amount):
        self.balance += amount
        return True
    
    def deduct_funds(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def display(self):
        print(f"\n{Colors.YELLOW}═══════ الحساب البنكي ═══════")
        print(f"الرصيد الحالي: {Colors.GREEN}${self.balance:,.2f}")
        print(f"الودائع: {Colors.CYAN}${self.deposits:,.2f}")
        print(f"القروض: {Colors.RED}${self.loans:,.2f}")
        print(f"{Colors.YELLOW}════════════════════════════\n")
