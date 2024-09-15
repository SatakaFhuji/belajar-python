# class/static variabel adalah variabel yang ada di dalam class
# instance variable adalah variable yang nempel di object


class Hero:
    # class/static variable
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.nama = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print(f"membuat hero dengan nama = {self.nama}")


hero1 = Hero("riky", 100, 500, 200)
print(Hero.jumlah)
hero2 = Hero("aldi", 100, 300, 100)
print(Hero.jumlah)
