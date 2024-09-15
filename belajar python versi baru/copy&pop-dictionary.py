teman_teman = {
    'nama': 'aldi',
    'umur': 22,
    'semester': 7,
    'Hobi': 'ngoding'
}

# jika kita menggunakan copy() maka yg variabel teman-teman tidak ikut merubah
teman = teman_teman.copy()

print(f'teman-teman : {teman_teman}')
print(f'teman : {teman}')

teman.update({'gender': 'laki - laki'})
print(f'{teman}\n')

# pop (mentranfer) dictionary, mengeluarkan values dari dictionary sebelumnya
gender = teman.pop('gender')  # berdasarkan key
print(f'data yang diambil dengan key : gender, value : {gender}')
print(f'teman : {teman}\n')

# popitem dictionary (data yang diambil adalah data paling akhir)
terakhir = teman.popitem()
print(f'data yang di ambil adalah data yang paling akhir {terakhir}')
print(f'teman {teman}')
