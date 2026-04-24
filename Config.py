import os
from colorama import Fore, Style, init
from Config import BUILDING_COSTS, INITIAL_BALANCE, INITIAL_ENERGY
# استيراد الأنظمة الأخرى
from building_system import BuildingManager
from population import PopulationManager

init(autoreset=True)

class Game:
    def __init__(self):
        self.balance = INITIAL_BALANCE
        self.energy = INITIAL_ENERGY
        self.buildings = []
        self.pop_manager = PopulationManager()
        self.building_manager = BuildingManager()

    def show_menu(self):
        os.system('clear')
        print(Fore.GREEN + "==== مدينة فلسطين الحرة ====")
        print(f"💰 الخزينة: {self.balance}$ | ⚡ الطاقة: {self.energy}")
        print(f"🏠 المباني: {len(self.buildings)} | 👥 السكان: {len(self.pop_manager.residents)}")
        print("============================")
        print("1. 🏗️ بناء منشأة جديدة")
        print("2. 👥 جذب سكان/سياح")
        print("3. 💾 حفظ وخروج")
        
    def build(self):
        print("\nالمباني المتاحة:")
        for b_type, info in BUILDING_COSTS.items():
            print(f"- {b_type}: {info['base']}$")
        
        choice = input("ماذا تريد أن تبني؟ ")
        if choice in BUILDING_COSTS:
            cost = BUILDING_COSTS[choice]['base']
            if self.balance >= cost:
                self.balance -= cost
                self.buildings.append(choice)
                self.energy -= BUILDING_COSTS[choice]['energy_cost']
                print(Fore.YELLOW + f"🎉 تم بناء {choice} بنجاح!")
            else:
                print(Fore.RED + "❌ الرصيد غير كافٍ!")

    def run(self):
        while True:
            # تحديث السياح تلقائياً في كل دورة بناءً على Config
            news = self.pop_manager.update_population(self.buildings)
            self.show_menu()
            if news: print(Fore.CYAN + news)
            
            action = input("\n🎮 اختر رقم الأكشن: ")
            if action == "1": self.build()
            elif action == "3": break

if __name__ == "__main__":
    game = Game()
    game.run()
