class Hero:

    # private class variabel
    __jumlah = 0

    def __init__(self, name, health, attpower, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attpower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return f"{self.__name} level {self.__level} : \n\thealt = {self.__health}/{self.__healthMax} \n\tattack = {self.__attPower} \n\tarmor = {self.__armor}"

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if self.__exp >= 100:
            print(self.__name, "level up")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def attack(self, musuh):
        self.gainExp = 50


kamenRider = Hero("kamen Rider", 100, 5, 10)
axe = Hero("axe", 100, 5, 10)
print(kamenRider.info)

kamenRider.attack(axe)
kamenRider.attack(axe)
kamenRider.attack(axe)

print(kamenRider.info)
