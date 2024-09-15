# belajar OOP (inheritance)
# inheritance -> penurunan sifat/mengambil, dari super class ke sub class


class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health


# class turunan dari Hero
class Hero_intelligent(Hero):
    pass


class Hero_strength(Hero):
    pass


lina = Hero("hero", 100)
sakura = Hero_intelligent("sakura", 10)
naruto = Hero_strength("naruto", 1000)

print(lina.name)
print(sakura.name)
print(naruto.name)
