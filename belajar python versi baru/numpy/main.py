import numpy as np

# list biasa
list_a = [1, 2, 3, 4, 5]

# matrix atau array di numpy
vektor_a = np.array([1, 2, 3, 4, 5])

# tidak bisa dikuadratkan
print(f'list a = {list_a}')
# print(list_a**2) <- akan gagal

# vektor matrix bisa di kuadratkan
print(f'vektor a = {vektor_a}')
print(vektor_a**2)

# matrix bersarang
matrix_b = np.array([(1, 2, 3), (1, 2, 3)])
print(f'matrix b = \n{matrix_b}')
print(f'matrix b^2 = \n{matrix_b**2}')

# matrix zeros (nol semua)
zeros_c = np.zeros((3, 3))
print(f'zeros c = \n{zeros_c}')

# matrix ones (satu)
ones_d = np.ones((2, 3))
print(f'ones d = \n{ones_d}')

# melakukan penjumlahan matrix
jumlah = matrix_b + matrix_b**2 + ones_d
print(jumlah)
