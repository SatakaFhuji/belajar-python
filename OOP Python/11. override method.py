# belajar override method
# override artinya menimpa


class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print(f"name : {self.name} \nhealth : {self.health}\n")


class Hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

    # akan mengoverride yang sama
    # 👇 override dari show info class Hero
    def showInfo(self):
        print(f"name : {self.name} \ntipe : Intelligent \nhealth : {self.health}\n")


class Hero_strangth(Hero):
    def __init__(self, name):
        super().__init__(name, 100)


lina = Hero_intelligent("lina")
axe = Hero_strangth("exe")

lina.showInfo()
axe.showInfo()
