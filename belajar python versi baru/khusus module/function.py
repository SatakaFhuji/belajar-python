def say_hello(nama):
    return f'hallo {nama}'


def total(*list_angka):
    hasil = 0
    for data in list_angka:
        hasil = hasil + data
    return hasil
