# belajar Deep Copy di list

from copy import deepcopy

from numpy import insert

a = [['Riky', 'Hawin', 'aldi', 'iwan', 'ilbram']]
b = a

b[0][0] = 'iqbal'

print(f'data a : {a}')
print(f'data b : {b}')


# penggunaan deep copy di nested list, harus import dulu !
c = a
c = deepcopy(a)

c[0].insert(0, 'kikuk')  # menambahkan data di list nasted
print(f'data a : {a}')
print(f'data b : {b}')
print(f'data c : {c}')
