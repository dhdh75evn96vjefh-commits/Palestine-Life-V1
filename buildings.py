from colors import Colors
from config import BUILDING_COSTS

class Building:
    def __init__(self, name, building_type):
        self.name = name
        self.type = building_type
        self.level = 1
        self.capacity = BUILDING_COSTS[building_type]["capacity"]
        self.energy_cost = BUILDING_COSTS[building_type]["energy_cost"]
    
    def upgrade(self):
        self.level += 1
        self.capacity += 5
        self.energy_cost += 2
        return self.level * BUILDING_COSTS[self.type]["base"]
    
    def __str__(self):
        return f"{self.name} (Lv.{self.level})"

class BuildingManager:
    def __init__(self):
        self.buildings = []
    
    def add_building(self, building_type, name, bank):
        if building_type in BUILDING_COSTS:
            cost = BUILDING_COSTS[building_type]["base"]
            if bank.deduct_funds(cost):
                building = Building(name, building_type)
                self.buildings.append(building)
                print(Colors.success(f"تم بناء {name} بنجاح!"))
                return True
            else:
                print(Colors.error("الرصيد غير كافٍ!"))
                return False
        return False
    
    def upgrade_building(self, index, bank):
        if 0 <= index < len(self.buildings):
            cost = self.buildings[index].upgrade()
            if bank.deduct_funds(cost):
                print(Colors.success(f"تم ترقية {self.buildings[index].name}!"))
                return True
        print(Colors.error("فشل الترقية!"))
        return False
    
    def display_buildings(self):
        print(f"\n{Colors.CYAN}═══════ المباني ═══════")
        for i, building in enumerate(self.buildings):
            print(f"{i+1}. {building} | سعة: {building.capacity} | طاقة: {building.energy_cost}")
        if not self.buildings:
            print("لا توجد مباني حالياً")
        print(f"{Colors.CYAN}══════════════════════\n")
    
    def get_total_energy_consumption(self):
        return sum(b.energy_cost for b in self.buildings)
