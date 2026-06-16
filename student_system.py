class Student:
    def __init__(self, name, attack, defense, skill):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.skill = skill

class Team:
    def __init__(self):
        self.members = []
    
    def add_student(self, student):
        if len(self.members) < 6:
            self.members.append(student)
            return True
        return False

# 示例使用
arina = Student("阿露", 1500, 800, "精准射击")
team = Team()
team.add_student(arina)