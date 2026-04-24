class QuestManager:
    def __init__(self):
        self.active_quests = [
            {"goal": "إيواء 50 ساكن", "reward": 10000, "completed": False},
            {"goal": "بناء 3 منشآت تجارية", "reward": 15000, "completed": False}
        ]

    def check_progress(self, city, bank):
        for q in self.active_quests:
            if not q["completed"]:
                # منطق التحقق (مثال: عدد المباني)
                if len(city.buildings) >= 3:
                    q["completed"] = True
                    bank.deposit(q["reward"])
                    print(f"🎊 مبروك! أنجزت مهمة: {q['goal']} وحصلت على {q['reward']}$")

