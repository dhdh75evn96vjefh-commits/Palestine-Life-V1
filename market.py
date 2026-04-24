class Market:
    def __init__(self):
        self.power_price = 150 # سعر وحدة الكهرباء

    def trade_power(self, power_grid, bank):
        if power_grid.power_level > 20: # إذا كان هناك فائض
            profit = 10 * self.power_price
            bank.deposit(profit)
            power_grid.power_level -= 10
            return f"💰 تم بيع فائض طاقة! الربح: {profit}$"
        return "❌ لا يوجد طاقة كافية للبيع حالياً."
