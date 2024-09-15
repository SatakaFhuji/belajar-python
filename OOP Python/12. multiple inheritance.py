# belajar OOP Python (multiple inheritance)
"""
multiple inheritance adalah suatu class
yang bisa mendapatkan inheritance dari banyak class

"""
# contoh 👇
class A:
    def method_A(self):
        print("ini adalah method A")


class B:
    def method_B(self):
        print("ini adalah method B")


""" 
jadi si class C 👇 akan mengambil/menginherit dari 2 buah class di atas👆
(class A dan B)
kegunaan : bisa mengambil berbagai class

"""


class C(A, B):
    pass


objek = C()

objek.method_A()
objek.method_B()
