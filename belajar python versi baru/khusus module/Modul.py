# Belajar Modul
# modul bisa di gunakan di file lain

# mengimport file/modul lain, dengan memasukkan nama file/modulnya
import function

# kita juga bisa mengambil secara spesifik file atau modul tertentu
from function import say_hello
from function import total
from function import khusus

# hasil dari import function
hello = function.say_hello('aldi')
print(hello)

hasil = function.total(1, 2, 3, 4, 5)
print(hasil)


# hasil dari from function import say_hello dan total
hello = say_hello('aldi')
print(hello)

hasil = total(1, 2, 3, 4, 5)
print(hasil)
