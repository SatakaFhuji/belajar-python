# kwargs mengambil data dalam bentuk dictionary
"""**kwargs"""


from optparse import Option


def fungsi(nama, tinggi, berat):
    """fungsi biasa"""
    print(f"{nama} punya tinggi {tinggi} dan beratnya {berat} kilo")


fungsi("aldi", 170, 49)


def fungsi(**kwargs):
    """fungsi kwargs"""
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan beratnya {berat} kilo")


fungsi(nama="aldi", tinggi=170, berat=49)


# studi kasus


def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        for angka in args:
            output *= angka
    else:
        print("tidak ada oprasi")
    return output


hasil = math(1, 2, 3, 4, 5, 6, 7, 8, 9, option="tambah")
print(f"hasil jumlah {hasil}")
hasil = math(1, 2, 3, 4, 5, 6, 7, 8, 9, option="kali")
print(f"hasil kali {hasil}")
