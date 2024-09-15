# belajar python oop (getter dan setter)
# decorator @property merubah sebuah method menjadi seperti variabel


class Hero:
    def __init__(self, nama, darah, armor):
        self.__nama = nama
        self.__darah = darah
        self.__armor = armor
        self.__info = "nama : {} \n\tdarah : {}".format(self.__nama, self.__darah)

    @property  # <- method ini dianggap variabel
    def info(self):
        return self.__info

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter  # <- untuk menghapus
    def armor(self):
        print("armor di delete")
        self.__armor = None


gusen = Hero("gusen", 100, 50)

print(gusen.info)

print("getter dan setter untuk __armor :")
print(gusen.armor)
print(gusen.__dict__)
gusen.armor = 60
print(gusen.armor)
print(gusen.__dict__)

print("delete armor")
del gusen.armor
print(gusen.__dict__)
