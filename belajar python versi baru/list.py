# Belajar list
# list adalah tipe data untuk kumpulan data
# menambah data menggunakan appand() contoh : nama_variabel.appand()
# menghapus data menggunakan remove() contoh : nama_variabel.remove()
# perlu diingat jika menghapus/remove data indexnya akan berubah


# membuat list menggunakan kurung siku []
nama = ['sumbul', 'ratna', 'aldi']
nama2 = ['kholid', 'gembul']

# menambahkan data sesui posisi, nama_variabel.insert(posisi yg akan di tambah, nama yg akan di tambahkan)
nama.insert(0, 'kanabawi')
print(nama)

# menambahkan data di akhir list nama_variabel.appand(),
nama.append('purnomo')

# menghapus data nama_variabel.remove()
nama.remove('ratna')

# menambahkan list dengan list
nama.extend(nama2)
print(nama)

# mengakses list
print(nama[0])

# untuk mengetahui jumlah data, kita menggunakan len()
print(len(nama))

# merubah data di list
print(nama)
nama[1] = 'novaldi'
print(nama)
