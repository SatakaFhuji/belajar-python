# belajar opp (variabel private)
# __variable privat bisa dipakai juga di dalam class


class Hero:
    # class variable
    jumlah = 0
    __privatejumlah = 0

    def __init__(self, nama, darah):
        self.nama = nama
        self.darah = darah

        # variable instance private
        # jika ingin membuat variabel prifat harus di awali undescor 2x (contoh :__nama-variabel)
        self.__private = "private"

        # variabel instance protected
        # jika ingin membuat variabel protected harus di awali undescor 1x (contoh :_nama-variabel)
        # tidak merubah apa-apa, perlakuannya sama dengan variabel instance global
        # hanya di pakai di dalam class saja dan jangan dirubah
        self._protected = "protected"


lina = Hero("lina", 100)

print(lina.__dict__)
print(Hero.__dict__)
print(Hero.__privatejumlah)
