# multi keys dan nasting (distionary di dalam dictionary)

import os
import datetime


os.system('cls')

# multi keys, bisa bernilai str, int, bool, library
mahasiswa1 = {
    'nama': 'iwan',
    'nim': '19533131',
    'gender': 'laki - laki',
    'sks': 4,
    'beasiswa': False,
    'lahir': datetime.datetime(2000, 5, 23)
}

mahasiswa2 = {
    'nama': 'ibram',
    'nim': '19533931',
    'gender': 'laki - laki',
    'sks': 4,
    'beasiswa': False,
    'lahir': datetime.datetime(2000, 3, 13)
}

mahasiswa3 = {
    'nama': 'fakih',
    'nim': '19533531',
    'gender': 'laki - laki',
    'sks': 4,
    'beasiswa': False,
    'lahir': datetime.datetime(2000, 4, 3)
}

# nasting
data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3
}

# dibuat seperti data base
print(f"{'Key':<6} {'Nama':<17} {'Nim':^8} {'gender':^11} {'Sks':^10} {'beasiswa':^15} {'Tanggal Lahir':<10}")
print('-'*87)

for mahasiswa in data_mahasiswa.keys():
    key = mahasiswa

    nama = data_mahasiswa[key]['nama']
    nim = data_mahasiswa[key]['nim']
    gender = data_mahasiswa[key]['gender']
    sks = data_mahasiswa[key]['sks']
    beasiswa = data_mahasiswa[key]['beasiswa']
    tanggal_lahir = data_mahasiswa[key]['lahir'].strftime('%x')

    print(f"{key:<6} {nama:<17} {nim:^8} {gender:<11} {sks:^10} {beasiswa:^15} {tanggal_lahir:^10}")
