# stuck = menumupuk dan mengambil yg paling atas. atau keluar di akhir

tumpukan = [1, 2, 3, 4, 5, 6]
print(tumpukan)

# memasukkan data baru
tumpukan.append(7)
print("data masuk : ", 7)
print("data sekarang : ", tumpukan)
tumpukan.append(8)
print("data masuk : ", 8)
print("data sekarang : ", tumpukan)

out = tumpukan.pop()
print("data keluar : ", out)
print("data sekarang : ", tumpukan)
