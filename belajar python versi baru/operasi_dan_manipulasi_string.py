# operasi dan manipulasi string
# https://docs.python.org/3.9/library/stdtypes.html#string-methods

# 1. menyambung string (concatenate)

kalimat1 = 'makan'
kalimat2 = 'sana'

kalimat3 = kalimat1 + ' ' + kalimat2
print(kalimat3)

# 2. menghitung panjang string menggunakan lengt (len)
panjang = len(kalimat3)
print(panjang)

# 3. operator untuk string
makan = 'makan'
# <- untuk mengecek apakah ada komponen di dalam string menggunkan (in)
status = makan in kalimat1
print(status)

# 4. mengulang string
print('wk'*10)

# 5. indexing, mengambil data dari string
print('index ke-0 : ' + kalimat1[0])
# untuk mengambil jumlah index
print('index ke-[0:5] : ' + kalimat1[0:5])  # harus melebihi index

# 6. item paling kecil menggunakan (min)
print('paling kecil : ' + min(kalimat1))
# item paling besar menggunakan (max)
print('paling besar : ' + max(kalimat1))

# 7. operator dalam bentuk method
data = 'halo semuanya'
jumlah = data.count('a')
print('jumlah a pada ' + data + ' = ' + str(jumlah))

# merubah uppercase dan lowercase dari string
# upper
salam = 'bro!'
print('normal = ' + salam)
salam = 'bro!'
print('upper = ' + salam.upper())
# lower
alay = 'AKU KECE ABIS'
print('normal = ' + alay)
alay = 'AKU KECE ABIS'
print('normal = ' + alay.lower())

# 8. pengecekan dengan isX method
# contoh untuk pengecekan lower case
salam = 'sist'
apakah_lower = salam.islower()  # nanti akan menghasilkan boolean
print(salam + ' is lower = ' + str(apakah_lower))

# catatan
# isalpha() <-- untuk mengecek semua huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, new line(\n)
# istitle() <-- semua kata dimulai dengan huruf besar


# cek komponan startwith() dan endwith() <-- keren

cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start " + str(cek_start))
cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end " + str(cek_end))

# penggabungan komponen join() dan split() <-- buat orang males

pisah = ['aku', 'sayang', 'kamu']
gabungan = ' ehm '.join(pisah)
print(pisah)
print(gabungan)

gabungan = "naik vespa keliling kota"
pisah = gabungan.split()
print(gabungan)
print(pisah)

gabungan = "naikehmvespaehmkelilingehmkota"
pisah = gabungan.split("ehm")
print(gabungan)
print(pisah)

# alokasi karakter
print("'kiri      '")

kanan = "kanan".rjust(20)  # rata kanan dengan 20 karakter
print("'" + kanan + "'")

kiri = "kiri".ljust(20)  # rata kiri dengan 20 karakter
print("'" + kiri + "'")

tengah = "tengah".center(20)  # rata tengah dengan 20 karakter
print("'" + tengah + "'")

tengah = "tengah".center(20, '-')  # rata tengah dengan 20 karakter
print("'" + tengah + "'")

# kebalikan dari alokasi karakter
kanan = kanan.strip()
print("'" + kanan + "'")
tengah = tengah.strip('-')
print("'" + tengah + "'")
