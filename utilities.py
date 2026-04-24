class PowerGrid:
    def __init__(self):
        self.power_level = 0
        self.is_online = False

    def build_power_plant(self):
        self.power_level += 100
        self.is_online = True
        return "⚡ تمت إنارة المدينة! جميع الخدمات تعمل الآن."

    def consume_power(self, amount):
        if self.power_level >= amount:
            self.power_level -= amount
            return True
        else:
            self.is_online = False
            return False

