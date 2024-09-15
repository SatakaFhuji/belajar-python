# belajar set
# set harus unix(tidak boleh sama) jika sama akan di hapus
# set tidak mendukung pengambilan data menggunakan index, contoh : [0]
# dalam set posisi urutan index bisa berubah setiap waktu

# list -> []
# tuple -> ()
# set -> {}

nama = {"aldi", "eko", "aldi", "eko", "iwan"}

# menambah data di set menggunakan variabel.add()
nama.add("ucup")

# menghapus data di set menggunakan variabel.remove()
nama.remove("ucup")

print(nama)

# set hanya mendukung pengambilan data menggunakan looping for
for i in nama:
    print(i)


# union hanya bisa digunakan oleh set
# union akan menjadikan satu, nama jika ada yang sama
# jika nama dalam set tersebut sama maka akan dijadikan satu atau ditimpa

x = {"jagung", "apel", "jambu", "alpukat"}
y = {"jambu", "belimbing", "anggur", "apel"}

z = x.union(y)

print(z)
