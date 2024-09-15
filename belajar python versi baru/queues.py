# queues = seperti antrian di restoran,
# jika restoran menerima antrian duluan maka yang akandapat pesanan pertama adalah
# yang pertama memesan itu. jadi queues itu yang di depan

# deque harus mengimport terlebih dahulu
from collections import deque

# fungsi deque bisa menambah dan mengurangi di depan
antrian = deque([1, 2, 3, 4, 5, 6])

print("data sekarang : ", antrian)

# menambah data
antrian.append(7)
print("data masuk", 7)
print("data sekarang : ", antrian)

# mengurangi data
out = antrian.popleft()
print("data keluar : ", out)
print("data sekarang : ", antrian)
