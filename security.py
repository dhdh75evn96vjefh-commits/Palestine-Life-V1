import random

class SecuritySystem:
    def __init__(self):
        self.firewall_level = 1

    def scan_for_threats(self):
        # احتمال 30% لوجود هجمة عند كل فحص
        if random.random() < 0.3:
            return True
        return False
