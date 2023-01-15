# К неизменяемым относятся целые числа (int),числа с плавающей запятой (float),
# булевы значения (bool), строки (str), кортежи (tuple).


# int
x = 10
print(x, type(x), id(x))

x = 12
print(x, type(x), id(x))


# Кортежи (tuple)
tuple1 = (1, 2, 3, 4)
print(tuple1, id(tuple1))

tuple1 = (2, 3, 3, 4)
print(tuple1, id(tuple1))



# К изменяемым — списки (list), множества (set), и словари (dict).

# Списки (list)
x = ['Яблоко', 'Груша', 'Слива']
x[1] = 'Ананас'
x.append(' И Персик')
print(x)


# Словари (dict)
dict = {'Name': 'Антон', 'Age': 23, 'Job': 'Middle Developer'}
print(dict)
dict['Name'] = 'Антон Хасанов'
print(dict)

