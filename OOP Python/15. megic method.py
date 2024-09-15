# belajar OOP Python (magic method) untuk pembuatan class
# magic method mempunyai tanda underscore2x (__nama method__)
# kelakuan __init__ akan dipanggil saat  membuat class
# jadi jika kita menggunakan keduanya (__repr__ dan __str__) maka yang akan di eksekusi
# yang __str__ nya


# contoh 👇
class mangga:

    # magic method 1
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    # magic method 2
    """method ini menghasilkan output str
    kapan waktu yang tepat saat memakai method ini : yaitu pada saat debugging"""

    def __repr__(self) -> str:
        return f"debug = mangga : {self.nama} \njumlah : {self.jumlah}"

    # magic method 3
    """kelakuan method ini sama persis dengan repr akan 
    tetapi berbeda waktu penggunaan, waktu yang tepat untuk memakai method ini
    adalah saat program sudah jadi"""

    def __str__(self) -> str:
        return f"\nstr = mangga : {self.nama} \njumlah : {self.jumlah}"

    # magic method 4
    """berguna untuk aritmatika
    cara penggunaanya harus memasukkan input"""

    def __add__(self, objek):
        return self.jumlah + objek.jumlah


mangga1 = mangga("mangga madu", 10)
mangga2 = mangga("lonjong", 20)
# cara penggunaan repr
print(repr(mangga1))

# cara penggunaan str
print(mangga1)

# penggunaan add
print(mangga1 + mangga2)
