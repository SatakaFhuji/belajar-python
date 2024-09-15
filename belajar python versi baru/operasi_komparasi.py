# operasi kompparasi/perbandingan
# setiap hasil dari operasi komparasi adalah boolean
# jika kedua nilainya sama dan kamu ingin menghasilkan True maka gunakan <= atau >=
# >, <, >=, <=, ==, !=, is, is not

a = 2
b = 3
# lebih besar dari (>)
print('==========================Lebih Besar Dari (>)=======================')
hasil = b > a
print(hasil)
hasil = a > b
print(hasil)
hasil = b > 3
print(hasil)
print('')
print('')


# lebih kecil dari (<)
print('==========================Lebih Kecil Dari (<)=======================')
hasil = b < a
print(hasil)
hasil = a < b
print(hasil)
hasil = b < 3
print(hasil)
print('')
print('')

# lebih dari sama dengan (>=)
print('==========================Lebih besar sama dengan (>=)=======================')
hasil = b >= a
print(hasil)
hasil = a >= b
print(hasil)
hasil = b >= 3
print(hasil)
print('')
print('')

# kurang dari sama dengan (<=)
print('==========================kurang dari sama dengan (<=)=======================')
hasil = b <= a
print(hasil)
hasil = a <= b
print(hasil)
hasil = b <= 3
print(hasil)
print('')
print('')

# sama dengan (==)
print('==========================sama dengan/absolut (==)=======================')
hasil = a == 2
print(hasil)
hasil = b == 2
print(hasil)
print()
print()

# tidak sama dengan (!=)
print('==========================tidak sama dengan (!=)=======================')
hasil = a != 2
print(hasil)
hasil = b != 3
print(hasil)
hasil = a != 3
print(hasil)
print()
print()

# (is) sebagai komparasi object identity
print('==========================object identity (is dan is not)=======================')
x = 5  # ini adalah assigment membuat objek
y = 5
print('nilai x =', x, 'id = ', hex(id(x)))
print('nilai y =', y, 'id = ', hex(id(y)))
hasil = x is y
print('x is y =', hasil)


x = 5  # ini adalah assigment membuat objek
y = 6
print('nilai x =', x, 'id = ', hex(id(x)))
print('nilai y =', y, 'id = ', hex(id(y)))
hasil = x is not 5
print('x is y =', hasil)
