import pandas as pd

# класический список
s1 = pd.Series([1, 2, 3, 4, 5])
print(s1)

# тут создал метки по которым можно обращаться к списку (похоже на работу со словарем)
s2 = pd.Series([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'])
print(s2)


# можно использовать словарь для одновременного задания меток и значений
d = {'a': 1, 'b': 2, 'c': 3}
s3 = pd.Series(d)
print(s3)


# с использованием константы. Значения в ячейках структуры будут одинаковыми
a = 7
s4 = pd.Series(a, ['a', 'b', 'c'])
print(s4)


# можно обращаться по численному индексу / можно использовать метку
s5 = pd.Series([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'])
print(s5['b'])
# доступно получение slice
print(s5[1:5:2])