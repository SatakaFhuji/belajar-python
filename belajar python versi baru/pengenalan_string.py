# cara membuat string di python

# 1. menggunkan single quote ('') dan doble quote ("")
nama = 'aldi'  # <- ini single quote atau kutip satu
print(nama)

nama = "gembul"  # <- ini doble quote atau kutip dua
print(nama)

# 2. menggunakan back slash (\)
# <- bisa digunakan apabila terdapat seperti contoh tersebut
contoh = 'ini adalah hari jum\'at'
print(contoh)

# 3. menggunakan raw string
print(r'c:\new folder')  # <- setelah raw tersebut akan dianggap string

# 4. multiline literal string
print("""
nama        : novaldi
semester    : 7 Teknik Informatika 
pekerjaan   : programer
""")  # <- akan menghasilkan sama seperti apa yg di tulis di multiline
