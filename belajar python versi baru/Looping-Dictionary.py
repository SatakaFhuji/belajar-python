# belajar looping di dictionary

teman_teman = {
    'nama': 'aldi',
    'umur': 22,
    'semester': 7,
    'Hobi': 'ngoding'
}


# looping pertama
print('='*5, 'for biasa', '='*5)
for teman in teman_teman:  # yg muncul key nya saja
    print(teman)


# operator atau method untuk mengambil item / iterables
# Keys
print('='*5, 'keys', '='*5)
for key in teman_teman.keys():
    print(key)

# Values
print('='*5, 'values', '='*5)
for values in teman_teman.values():
    print(values)

# item
print('='*5, 'item', '='*5)
for item in teman_teman.items():
    print(item)

for key, value in teman_teman.items():
    print(f'key = {key}, value = {value} ')
