# belajar method

# method di oop pyhton dibagi menjadi 3 yaitu :
# 1.method dengan argumen
# 2.method tanpa argumen
# 3.method dengan return


class Hero:
    # class variable
    jumlah_hero = 0

    # instace variable
    def __init__(self, inputNama, inputpower, inputArmor):
        self.nama = inputNama
        self.power = inputpower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # method tanpa argumen dan tanpa return atau void function
    def siapa(self):
        print(f"namaku adalah {self.nama}")

    # method dengan argumen
    def powerup(self, up):
        self.power += up

    # method dengan return
    def getpower(self):
        return self.power


hero1 = Hero("jett", 100, 50)
hero2 = Hero("sova", 200, 50)

hero1.siapa()
hero1.powerup(10)

print(hero1.getpower())
