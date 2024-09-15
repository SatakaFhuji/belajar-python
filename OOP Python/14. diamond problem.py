# belajar OOp Python (diamond Problem 💎🚫)
# salah satu maslah 💀 yang muncul ketika menggunakan multiple inheritance yaitu diamond problem
# cara penyelesaian masalah diamond problem tergantung urutan. note : --kalau tidak salah--


class A:
    def show(self):
        print("ini adalah show A")


class B(A):
    def show(self):
        print("ini adlah show B")


class C(A):
    def show(self):
        print("ini adlah show C")


class D(B, C):
    pass


objek = D()
objek.show()
