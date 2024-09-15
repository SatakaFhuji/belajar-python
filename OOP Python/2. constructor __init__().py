import os

os.system("cls")


# self adalah hero1 dan parameter selanjutnya adalah yg ada di dalam kurung
# __init__ akan dieksekusi saat object di buat
# __init__ akan memberikan atribut kepada objectnya
class Hero:
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


# pembuatan object
hero1 = Hero("aldi", 100, 500, 50)
hero2 = Hero("riki", 200, 600, 65)
hero3 = Hero("Hawin", 500, 400, 1000)

print(hero1.name)
print(hero2.health)
print(hero3.armor)
print(hero3.__dict__)
print(hero3.__dict__)
print(hero3.__dict__)
