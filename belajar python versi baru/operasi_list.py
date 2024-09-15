# belajar operasi di list

angka = [1, 2, 3, 4, 5, 6, 7, 4, 8, 8, 8, 9, 0]


# menghitung data di list menggunakan count
jumlah = angka.count(8)
print(f'jumlah angka 8 ada {jumlah}')

# mengambil posisi ke berapa di dalam list
data = ['zulkifli', 'iwan', 'aldi', 'ibram', 'naufal']
data_ibram = data.index('ibram')
print(f'index ilbram ke : {data_ibram}')

# mengurutkan list (sort)
print(f'data sebelum diurutkan {angka}')

angka.sort()
print(f'data sesudah diurutkan dengan sort {angka}')

# mengurutkan data list berdasarkan alfabet (sort)
print(f'data string sebelum di urutkan {data}')

data.sort()  # diurutkan berdasarkan alfabet
print(f'data string sesudah diurutkan dengan sort {data}')

# membalik list, dari besar ke kecil reverse
angka.reverse()
data.reverse()

print(f'sesudah di reverse {angka}\n{data}')
