# operasi logika atau boolean

# not, or, and, xor

# NOT
print('====NOT====')
a = True
c = not a
print('data a', a)
print('----------NOT')
print('data c =', c)

print()

# OR (jika salah satu True maka hasilnya akan True)
print('====OR====')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, ' =', c)
a = True
b = False
c = a or b
print(a, 'OR', b, ' =', c)
a = True
b = True
c = a or b
print(a, 'OR', b, '  =', c)

# AND (jika salah satu False maka hasilnya akan False)
print('====AND====')
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, ' =', c)
a = True
b = False
c = a and b
print(a, 'AND', b, ' =', c)
a = True
b = True
c = a and b
print(a, 'AND', b, '  =', c)

# XOR (jika salah satu True maka hasilnya True, dan jika sama maka akan menghasilkan false )
print('====XOR====')
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, ' =', c)
a = True
b = False
c = a ^ b
print(a, 'XOR', b, ' =', c)
a = True
b = True
c = a ^ b
print(a, 'XOR', b, '  =', c)
