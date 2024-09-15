# belajar python oop (encapsulasi)
# aturan encapsulasi :
# 1. buat semua variable private
# 2.getter(mengambil variabel) dan setter(mengsetting variabel)

# ininya encapsulasi adalah untuk menjaga private variabel tidak dirubah


class Hero:
    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower

    # getter
    def getname(self):
        return self.__name

    def gethealth(self):
        return self.__health

    # setter
    def diserang(self, serangPower):
        self.__health -= serangPower

    def setAttPower(self, nilaiBaru):
        self.__attackPower = nilaiBaru


# awal game
banjing = Hero("banjing", 50, 100)

print(banjing.__dict__)

# game berjalan
# print(banjing.__name) <- tidak bisa
print(banjing.getname())
banjing.diserang(10)
print(banjing.gethealth())
