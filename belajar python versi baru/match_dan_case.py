import os

# syntax
# match nama_variabel:
#   case Nama_pilihan:
#       yang_dipilih

# match itu memilih pilihan 1 atau pilihan 2

# contoh
sistem = os.name

match sistem:
    case "nt":
        os.system("cls")
