class Bank:
    def __init__(self, initial_balance=10000):
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("❌ عذراً! رصيدك غير كافٍ لإتمام هذه العملية.")
            return False

    def deposit(self, amount):
        self.balance += amount
        print(f"💰 تم إضافة {amount} إلى رصيدك. الرصيد الحالي: {self.balance}")

    def get_balance(self):
        return self.balance
