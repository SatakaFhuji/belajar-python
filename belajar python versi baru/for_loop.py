# Belajar for loop
# for digunakan untuk mengakses/melakukan perulagan semua data yang ada di dalam list

# for kondisi:
#   aksi

pelanggan = ['aldi', 'novaldi', 'purnomo', 'jeki']

pelanggan.append('ucup')
pelanggan.remove('jeki')

# mengakses semua nama pelanggan
for nama in pelanggan:
    print(f'nama pelanggannya siapa saja : {nama}')
