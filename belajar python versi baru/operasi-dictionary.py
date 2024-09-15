# Belajar operator dictionary

from turtle import update


dict = {
    'nama': 'aldi',
    'umur': 22,
    'kota asal': 'ponorogo'
}

# panjang dictionary
len = len(dict)
print(f'panjang dictionary : {len}')

# mengakses value (read) dengan get
print(dict.get('nama'))
print(dict.get('aldi', 'key tidak ditemukan'))  # cek key dengan massage

# mengupdate dengan data
dict['nama'] = 'Novaldi'
print(f'update data key nama : aldi menjadi Novaldi {dict}')

# menambah data
dict['semester'] = 7
print(f'menambah data {dict}')

# mengupdate dengan lebih simpel gunakan update()
dict.update({'nama': 'Mohammad Novaldi Purnomo'})
print(f'mengupdate lebih simpel {dict}')

# menambah data dengan lebih simple
# jika tidak ada data didalam dict, di add otomatis
dict.update({'hobi': 'coding'})
print(f'menambahkan data dengan lebih simple {dict}')

# menghapus data di dictionary
del dict['hobi']
print(f'menghapus data hobi di dict {dict}')
