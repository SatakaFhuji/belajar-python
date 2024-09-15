# belajar OOP Python (method resolution order)
# jika nama object sama, maka akan diambil yang berdasarkan urutan

"""
gunakan help(nama_object) untuk melihat object mana dulu,
yang akan ditampilkan ketika nama objectnya sama

jadi : method resolution order yang di inherit ke sebuah class,
itu tergantung dari urutannya
"""


class A:
    def show(self):
        print("ini adalah show A")


class B:
    def show(self):
        print("ini adalah show B")


# contoh seperti di bawah 👇 pasti yang akan di ambil yg A
class C(A, B):
    pass


objek = C()
objek.show()
objek.show()
# help(objek)
