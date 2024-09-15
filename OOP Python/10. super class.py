# belajar OOP (super)
# mengambil method yang ada didalam class super yaitu Hero


class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print(f"{self.name} dengan health {self.health}")


class Hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)  # <- mengambil __init__ yg ada di Hero
        super().showInfo()


class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)
        super().showInfo()


sakura = Hero_intelligent("sakura")
sasuke = Hero_strength("sasuke")
