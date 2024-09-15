# belajar copy list
# menduplikast list dengan copy

a = ['Riky', 'Hawin', 'aldi', 'iwan', 'ilbram']
b = a

# merubah data b
b[2] = 'novaldi'
print(f'data a : {a}')
print(f'data b : {b}')  # data a juga ikut berubah jika tidak menggunakan copy


# jika menggunakan copy (full duplikat)
c = a.copy()
c[2] = 'aldii'
print(f'data a : {a}')
print(f'data c : {c}')  # jika menggunakan copy, data a tidak akan berubah
