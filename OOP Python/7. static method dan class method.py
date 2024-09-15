# belajar python oop (static method dan class method)


class Bunga:

    # private class variabel
    __jumlah = 0

    def __init__(self, warna):
        self.__warna = warna
        Bunga.__jumlah += 1

    # method ini hanya berlaku untuk object
    def getjumlah(self):
        return Bunga.__jumlah

    # method ini tidak berlaku untuk object tapi berlaku untuk class
    def getjumlah1():
        return Bunga.__jumlah

    # method static (decorator), dia akan nempel di object dan classnya
    @staticmethod  # <- dikasih tanda @staticmethod
    def getjumlah2():
        return Bunga.__jumlah

    # method class, dia juga akan nempel di object dan classnya tetapi memakai argument
    @classmethod
    def getjumlah3(cls):  # <- argument cls
        return cls.__jumlah


dahlia = Bunga("dahlia")
print(dahlia.getjumlah())  # <- output dari getjumlah()
print(Bunga.getjumlah1())  # <- output dari getjumlah1()
kamboja = Bunga("kamboja")
print(kamboja.getjumlah2())  # <- output dari getjumlah2()
sepatu = Bunga("sepatu")
print(Bunga.getjumlah3())  # <- output dari getjumlah3()
