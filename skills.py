# skills.py
class Skill:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 0

    def add_experience(self, amount):
        self.experience += amount
        if self.experience >= self.level * 10:  # Простейшая формула повышения уровня
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        print(f"{self.name} улучшен до уровня {self.level}!")

class SkillsManager:
    def __init__(self):
        self.skills = {
            "digging": Skill("Digging"),
            "crafting": Skill("Crafting"),
            "combat": Skill("Combat")
        }

    def add_experience(self, skill_name, amount):
        if skill_name in self.skills:
            self.skills[skill_name].add_experience(amount)
