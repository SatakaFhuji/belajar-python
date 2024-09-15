# exception akan terjadi saat programmengalami error saat runtime

# contoh sederhana untuk menangkap exception


from math import nan

# contoh sederhana
#input_user = int(input('masukkan angka : '))
#hasil = nan
#
# try:
#    hasil = 10 / input_user
#
# jika runtime error except akan dijalankan
# except:
#    print('input tidak boleh 0')
#
#print(f'hasil = {hasil}')


# contoh di aplikasi

while (True):
    angka = int(input('masukkan angka pembagi : '))
    try:
        hasil = 10 / angka
        print(f'hasil = {hasil}')
        is_done = input('lanjutkan (y/n) ?')
        if is_done == 'n':
            break
    except:
        print('pembagi nol, silahkan masukkan input lagi')

print('akhir dari program 1')

# contoh aplikasi untuk membuat file data.txt
try:
    with open('try.txt', mode='r', encoding='utf-8') as file:
        print(file.read())
except:
    print('file try.txt tidak ditemukan, membuat file baru')
    with open('try.txt', mode='w', encoding='utf-8') as file:
        file.write('file baru')

print('akhir dari program 2')
