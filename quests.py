class QuestManager:
    def __init__(self):
        self.active_quests = [
            {"goal": "إيواء 5 سكان جُدد", "target": 5, "reward": 5000, "completed": False}
        ]

    # تأكد أن الاسم هنا 'check_quests' بالضبط
    def check_quests(self, city, pop_sys, power_sys, bank):
        status_updates = []
        for q in self.active_quests:
            if not q["completed"]:
                # مثال للتحقق من عدد السكان
                if len(pop_sys.residents) >= q["target"]:
                    q["completed"] = True
                    bank.deposit(q["reward"])
                    status_updates.append(f"🎊 إنجاز! {q['goal']} | المكافأة: {q['reward']}$")
        return status_updates
