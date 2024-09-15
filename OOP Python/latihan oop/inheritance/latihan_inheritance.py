class Hero:
    def __init__(self, name):
        self.health_pool = [0, 100, 200, 300, 400, 500]
        self.attPower_pool = [0, 10, 20, 30, 40, 50]
        self.armor_pool = [0, 1, 2, 3, 4, 5]
        self.__name = name
        self.__exp = 0
        self.__level = 0

    def show_info(self):
        print(
            f"name : {self.__name} \nlevel: {self.__level} \nhealth : {self.__health} \nattack Power : {self.__attPower} \narmor : {self.__armor}\n"
        )

    @property
    def health_pool(self):
        pass

    @property
    def attPower_pool(self):
        pass

    @property
    def armor_pool(self):
        pass

    @property
    def level_up(self):
        pass

    @property
    def gian_exp(self):
        pass

    @health_pool.setter
    def health_pool(self, input):
        self.__health_pool = input

    @attPower_pool.setter
    def attPower_pool(self, input):
        self.__attPower_pool = input

    @armor_pool.setter
    def armor_pool(self, input):
        self.__armor_pool = input

    @gian_exp.setter
    def gian_exp(self, input):
        self.__exp += input
        if self.__exp >= input:
            self.level_up = self.__exp // 100
            self.__exp %= 100

    @level_up.setter
    def level_up(self, input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__attPower = self.__attPower_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]


class HeroIntelligent(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.health_pool = [0, 50, 100, 150, 200, 250]
        self.attPower_pool = [0, 20, 40, 60, 80, 100]
        self.level_up = 1


class HeroStrangth(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.health_pool = [0, 200, 300, 400, 500, 600]
        self.attPower_pool = [1, 20, 40, 60, 80, 100]
        self.armor_pool = [0, 2, 4, 6, 8, 10]
        self.level_up = 1
