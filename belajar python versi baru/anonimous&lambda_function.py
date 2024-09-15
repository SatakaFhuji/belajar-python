# lambda function -> bisa membuat program menjadi lebih simpel
# kegunaan lambda, kita bisa membuat fungsinya berbasis dari fungsi utama
# dan bisa mengubah parameter di dalamnya

# lambda
# cara penggunaan
# output = lambda argument: perintah


# anonimous function
# currying <- haskell curry

def pangkat(angka, n):
    hasil = angka ** n
    return hasil


data_hasil = pangkat(5, 2)

print(f'function biasa = {data_hasil}')


# dengan currying menjadi
def pangkat(n):
    return lambda angka: angka**n


pangkat2 = pangkat(2)
print(f'pangkat 2 = {pangkat2(5)}')
