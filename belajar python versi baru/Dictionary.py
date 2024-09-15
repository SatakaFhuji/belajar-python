# Belajar Tipe Data Dictionary
# mirip seperti list, tuple, dan set
# dengan dictionary kita bisa mengganti indexnya menjadi string
# untuk membuat dictionary sama seperti membuat set, yaitu dengan menggunakan {}
# perbedaan Dictionary dengan list, tuple, dan set adalah,
# dictionary itu menggunakan key:value contoh ('nama':'aldi')

# pembuatan dictionary
customer = {"Nama": "aldi", "age": 22, "address": "ponorogo"}

# untuk mengakses data ambil keynya
name = customer["Nama"]
age = customer["age"]
address = customer["address"]

# menambah dan mengubah data baru di Dictionary
customer["company"] = "star up"
customer["Nama"] = "Mohammad Novaldi Purnomo"

# untuk menghapus data di Dictionary dunakan kata kunci del
del customer["address"]


# Dictionary bisa menampilkan data dalam bentuk for loop
# dictionary mempunyai method yang namanya items
# item itu merupakan data Dictionary atau list berupa tuple
for key, value in customer.items():
    print(f"{key}:{value}")
