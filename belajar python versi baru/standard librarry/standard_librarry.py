import io
from collections import Counter
import datetime

data_waktu = datetime.datetime.now()
print(f"datetime now : {data_waktu}")
print(f"tahun : {data_waktu.year}")
print(f"hari : {data_waktu.strftime('%A')}")


data = ["a", "b", "c", "d", "a", "d", "a"]
data_count = Counter(data)

print(f"data count = {data_count}")
print(f"jumlah a = {data_count['a']}")
print(f"jumlah d = {data_count['d']}")


file = io.open("file_text.txt", mode='r')
print(file.read())
