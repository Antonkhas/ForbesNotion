import pandas as pd


# Создание DataFrame из словаря
d = {"price":pd.Series([1, 2, 3], index=['v1', 'v2', 'v3']),
     "count": pd.Series([10, 12, 7], index=['v1', 'v2', 'v3']),
     "activ": pd.Series([11, 13, 8], index=['v1', 'v2', 'v3'])}
df1 = pd.DataFrame(d)

print(df1)  # можно так же вывести index/columns + все теже методы как у Series


