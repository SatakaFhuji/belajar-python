# belajar looping list

# for
print("for loop")
peserta = [1, 2, 3, 4, 5, 6, 7, 8]

for data in peserta:
    print(f"data peserta : {data}")

# while
print("\nwhile loop")
angka = [
    1,
    2,
    3,
    5,
    4,
    6,
    1,
]

panjang = len(angka)
i = 0

while i < panjang:
    print(f"angka = {angka[i]}")
    i += 1

# list comprehension
print("\nlist comprehension")
data = ["simbol", 1, 2, 3, 4, 5, "kusi"]

[print(f"data = {i}") for i in data]

# enumerate, enumerate ini bisa mengambil indexnya dan datanya
print("\nenumerate")
data_list = ["ucup", 1, 2, 3, 4, 5, "gembul"]

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
