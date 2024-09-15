# Belajar Continue
# Continue digunakan untuk mengskip proses yg ada di dalam looping for dan while

# continue
for i in range(1, 101):
    if i % 2 == 1:
        continue  # akan membuat loop loncat ke step selanjutnya
    print(i)


# pass -> berfungsi sebagai dummy (tidak akan dieksekusi)
i = 0

while i < 5:
    i += 1
    if i == 3:
        pass  # (pass) ini tidak akan dieksekusi
    print(i)
