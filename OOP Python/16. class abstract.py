# belajar OOp Python (class abstract)
# cara menggunakan class abstract yaitu:
# harus import dulu modul abc.
# abc = abstract base class

"""class abstract mempunyai intance class,
jadi class abstract menjadi blue printnya class dibawahnya.
perbedaan class biasa dengan class abstract :
class abstract akan memaksa class untuk mengimplementasikan methodnya"""

from abc import ABC, abstractmethod  # 👈 decorator


class Button(ABC):
    def __init__(self, set_link):
        self.link = set_link  # type: ignore

    @abstractmethod  # 👈 decorator
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass


class PushButton(Button):

    # 👇 ini dipaksa untuk menjalankan def click yg di abstract
    def click(self):
        print(f"Go to : {self.link}")

    @Button.link.setter
    def link(self, input):
        self.__link = input

    @link.getter
    def link(self):
        return self.__link


tombol1 = PushButton("www.kelasterbuka.id")

tombol1.click()


"""PEMBELAJARAN PYTHON TELAH SELESAI SECARA SYNTAX, JIKA INGIN MELANJUTKAN 
LANJUT SAJA KE OBJECT ORIENTED DESIGN"""
