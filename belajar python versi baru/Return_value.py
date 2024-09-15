# belajar Method Return Value
# jika ingin return, tinggal menambahkan return di akhir program

''' fungsi dengan kembalian'''

# templet fungsi dengan kembalian
# def nama_function(argumen atau parameter):
#     badan fungsi
#     return output


def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    return total


# menambahkan variabel untuk menampung return total
total = jumlahkan(10, 10, 10, 10)

# memanggil return
print(total)
