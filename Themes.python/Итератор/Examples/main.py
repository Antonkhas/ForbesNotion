# можно выводить каждый обьект по отдельности, указав спиосок iter
tumb = ["ножницы", "карандаш", "яблоко", "книга"]
itr = iter(tumb)
print(next(itr))
print(next(itr))


# проверяем является ли обьект итерируемым
print(iter(tumb))


# обозначаем, что нужно итерировать каждый обьект
for i in tumb:
    print(i)


# собственный итератор
class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration


s_iter2 = SimpleIterator(5)
for i in s_iter2:
    print(i)