# belajar default argument
# jika kita mau ada default valuenya, usahakan yg ada default valuenya itu di belakang

# def nama_fuction(argument = nilai defaultnya):
#    badan fungsi

def nama_panggilan(nama1='novaldi', nama2=''):
    print(f'hallo {nama1}-{nama2}')


nama_panggilan()
nama_panggilan(nama2='purnomo')


# contoh 1
def say_hello(nama="Ganteng"):
    '''fungsi dengan default argument'''
    print(f"Hallo {nama}")


say_hello("Ucup")
say_hello()

# contoh 2


def sapa_dia(nama, pesan="Apa kabar?"):
    '''fungsi dengan satu input biasa, dan satu default argument'''
    print(f"hai {nama}, {pesan}")


sapa_dia("Dudung", "Hai Ganteeeng")
sapa_dia("Otong")

# contoh 3


def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil


print(hitung_pangkat(2, 4))

hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)

# contoh 4


def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil


print(fungsi())
print(fungsi(input3=10))
