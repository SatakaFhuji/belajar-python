# belajar argument list

# dengan menambahkan tanda bintang di depan parameternya,
# otomatis parameter tersebut akan menjadi argument list,
# yg artinya bisa kita masukkan datanya lebih dari 1
# jika ingin menambahkan parameter lain, argument listnya
# harus di taruh paling belakang
def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f'Total {list_angka} = {total}')


jumlahkan(10, 10, 10, 10)
