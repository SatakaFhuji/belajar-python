# global dan local scope

nama_global = 'aldi'  # <- ini adalah variabel global


# akses variabel global dalam fungsi
def fungsi1():
    print(f'fungsi menampilkan nama {nama_global}')


fungsi1()

# akses variabel global dalam loop
for i in range(0, 4):
    print(f'loop ke {i} - {nama_global}')


# variabel local scope
def fungsi2():
    nama_local = 'suminah'  # <- ini adalah variabel local, di dalam fungsi


# Contoh 1: penggunaan akses variabel
def say_otong():
    print(f"Hello {nama}")


nama = "Otong"
say_otong()

# contoh 2: merubah variabel global
angka = 0
name = "Ucup"


def ubah(nilai_baru, nama_baru):
    global angka  # fungsi ini mendapat akses merubah angka
    global name
    angka = nilai_baru
    name = nama_baru


print(f"Sebelum {angka,name}")
ubah(10, "Otong")
print(f"Sesudah {angka,name}")

# contoh 3:
angka = 0

for i in range(0, 5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 5
    angka_dummy = 10

print(angka)
print(angka_dummy)
