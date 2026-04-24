class Job:
    """الفئة الأم لكل المهن"""
    def __init__(self, category, salary):
        self.category = category
        self.salary = salary

# --- فرع الهندسة والبناء ---
class Engineering(Job):
    def __init__(self, specialty):
        # تخصصات الهندسة ورواتبها
        specialties = {
            "معماري": 6000,
            "مدني": 5500,
            "كهرباء": 5000
        }
        self.specialty = specialty
        super().__init__("الهندسة", specialties.get(specialty, 4000))

    def get_permit(self):
        return f"صلاحية: إصدار تصاريح بناء لفرع {self.specialty}"

# --- فرع الطب والخدمات الصحية ---
class Medical(Job):
    def __init__(self, specialty):
        # تخصصات الطب ورواتبها
        specialties = {
            "جراح": 12000,
            "ممرض": 4000,
            "صيدلي": 7000
        }
        self.specialty = specialty
        super().__init__("الطب", specialties.get(specialty, 5000))

    def heal(self):
        return f"صلاحية: علاج المرضى في قسم {self.specialty}"

# --- فرع الأمن والشرطة ---
class Security(Job):
    def __init__(self, rank):
        # الرتب العسكرية ورواتبها
        ranks = {
            "ضابط": 8000,
            "شرطي": 3500
        }
        self.rank = rank
        super().__init__("الأمن", ranks.get(rank, 3000))

# --- تجربة النظام الفراعي ---
if __name__ == "__main__":
    employee1 = Engineering("معماري")
    employee2 = Medical("جراح")

    print(f"الموظف الأول تخصص: {employee1.specialty} براتب {employee1.salary}")
    print(employee1.get_permit())
    
    print(f"الموظف الثاني تخصص: {employee2.specialty} براتب {employee2.salary}")
# --- فرع الأمن السيبراني ---
class CyberSecurity(Job):
    def __init__(self, specialty):
        # تخصصات الأمن السيبراني
        specialties = {
            "مختبر اختراق": 9000,
            "محلل بيانات": 7500,
            "مدير حماية": 11000
        }
        self.specialty = specialty
        super().__init__("الأمن السيبراني", specialties.get(specialty, 6000))

    def secure_system(self):
        return f"🛡️ تم تفعيل بروتوكولات الحماية لفرع {self.specialty}."


