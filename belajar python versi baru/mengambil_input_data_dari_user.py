#input user

#string : data yang di masukkan user, pasti menghasilkan string
data = input('masukkan data : ')

print('data = ',data,',type = ',type(data))

#jika kita ingin mengambil integer dan float
angka = int(input('masukkan angka : '))
print('angka = ',angka,',type = ',type(angka))

angka_float = float(input('masukkan angka float : '))
print('angka float = ',angka_float,',type = ',type(angka_float))


#jika ingin mengambil boolean
biner = bool(int(input('masukkan nilai bolean : ')))
print('angka bolean = ',biner,',type = ',type(biner))