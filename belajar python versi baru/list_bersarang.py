# belajar Nested List atau Lis Bersrang (list di dalam list)

# list biasa
nama = ['aldi', 'sumbul']

# list bersarang atau nested list
list_bersarang = [nama]
print(f'ini adalah list bersarang {list_bersarang}')

# contoh penggunaan
peserta = ['hawin', 23, 'male']
peserta1 = ['riky', 23, 'male']
peserta2 = ['aldi', 22, 'male']
peserta3 = ['iwan', 22, 'male']
peserta4 = ['ilbram', 22, 'male']

nama_peserta = [peserta, peserta1, peserta2, peserta3, peserta4]
print(f'ini adalah list bersarang {nama_peserta}')

for member in nama_peserta:
    print(f'nama : {member[0]} berumur {member[1]} jenis kelamin {member[2]}')
