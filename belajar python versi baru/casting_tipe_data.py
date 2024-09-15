#casting (merubah 1 tipe ke tipe lain)
#tipe data = int, float, str, bool

#INTEGER
print('===========================INTEGER=================================')
data_int = 5
print('data = ', data_int, ',type=', type(data_int))

data_float = float(data_int)
print('data = ', data_float, ',type=', type(data_float))

data_str = str(data_int)
print('data = ', data_str, ',type=', type(data_str))

data_bool = bool(data_int) #akan false jika nilai int = 0
print('data = ', data_bool, ',type=', type(data_bool))


print('')


#FLOAT
print('===========================FLOAT=================================')
data_float = 5.7
print('data = ', data_float, ',type=', type(data_float))

data_int = int(data_float) #akan dibulatkan ke bawah
print('data = ', data_int, ',type=', type(data_int))

data_str = str(data_float)
print('data = ', data_str, ',type=', type(data_str))

data_bool = bool(data_float) #akan false jika nilai float = 0
print('data = ', data_bool, ',type=', type(data_bool))


print('')


#BOOLEAN
print('===========================BOOLEAN=================================')
data_bool = False
print('data = ', data_bool, ',type=', type(data_bool))

data_int = int(data_bool) #akan dibulatkan ke bawah
print('data = ', data_int, ',type=', type(data_int))

data_str = str(data_bool)
print('data = ', data_str, ',type=', type(data_str))

data_float = float(data_bool) #akan false jika nilai float = 0
print('data = ', data_float, ',type=', type(data_float))


print('')


#STRING
print('===========================STRING=================================')
data_str = 'dena'
print('data = ', data_str, ',type=', type(data_str))

data_int = int(data_str) #string harus angka
print('data = ', data_int, ',type=', type(data_int))

data_bool = bool(data_str) #false jika string kosong
print('data = ', data_bool, ',type=', type(data_bool))

data_float = float(data_str) #string harus angka
print('data = ', data_float, ',type=', type(data_float))