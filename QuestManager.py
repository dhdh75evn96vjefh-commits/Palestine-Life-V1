from Colors import Colors

class QuestManager:
    def __init__(self):
        self.quests = {
            "مدينة_ناشئة": {
                "title": "مدينة ناشئة",
                "description": "وصل عدد السكان إلى 100",
                "target": 100,
                "reward": 5000,
                "completed": False
            },
            "مركز_تجاري": {
                "title": "مركز تجاري",
                "description": "بناء 3 منشآت تجارية (تجاري أو فندق)",
                "target": 3,
                "reward": 8000,
                "completed": False
            },
            "حصن_رقمي": {
                "title": "حصن رقمي",
                "description": "رفع الأمن إلى 95",
                "target": 95,
                "reward": 10000,
                "completed": False
            }
        }
    
    def check_quests(self, game_state, bank):
        """فحص المهام ومنح المكافأة المالية فوراً"""
        new_completions = []
        
        # مهمة السكان
        if not self.quests["مدينة_ناشئة"]["completed"]:
            if game_state["population"] >= self.quests["مدينة_ناشئة"]["target"]:
                self.complete_quest("مدينة_ناشئة", bank, new_completions)
        
        # مهمة المباني التجارية
        if not self.quests["مركز_تجاري"]["completed"]:
            if game_state["commercial_count"] >= self.quests["مركز_تجاري"]["target"]:
                self.complete_quest("مركز_تجاري", bank, new_completions)
        
        # مهمة الأمن
        if not self.quests["حصن_رقمي"]["completed"]:
            if game_state["security"] >= self.quests["حصن_رقمي"]["target"]:
                self.complete_quest("حصن_رقمي", bank, new_completions)
        
        return new_completions

    def complete_quest(self, key, bank, completions_list):
        """دالة مساعدة لإتمام المهمة وإضافة المال"""
        self.quests[key]["completed"] = True
        reward = self.quests[key]["reward"]
        bank.add_funds(reward)
        completions_list.append(self.quests[key])
        print(f"\n{Colors.YELLOW}🌟 إنجاز جديد: {self.quests[key]['title']}")
        print(Colors.success(f"تم إضافة مكافأة ${reward:,} إلى خزنتك!"))

    def display(self):
        print(f"\n{Colors.CYAN}══════════════ قائمة المهام ══════════════")
        for quest in self.quests.values():
            status = Colors.success("✅ مكتملة") if quest["completed"] else Colors.warning("⏳ قيد التنفيذ")
            print(f"📌 {Colors.WHITE}{quest['title']}: {quest['description']}")
            print(f"   الحالة: {status} | المكافأة: {Colors.GREEN}${quest['reward']:,}")
        print(f"{Colors.CYAN}════════════════════════════════════════\n")

