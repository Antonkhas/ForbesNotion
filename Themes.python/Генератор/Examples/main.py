# (выражение for j in итерируемый объект if условие)
# Где for, in, if — ключевые слова, j — переменная.

# .close () — останавливает выполнение генератора;
# .throw () — генератор бросает исключение;
# .send () — позволяет отправлять значения генератору.


def f_gen(m):
    s = 1
    for n in range(1, m):
        yield n**2 + s
        s += 1


a = f_gen(5)
print(a)

for i in a:
    print(i)


print('--------- 2 example ----------')

def gen_fun():
    print('block 1')
    yield 1
    print('block 2')
    yield 2
    print('end')


for i in gen_fun():
    print(i)


print('--------- 3 example ----------')


def f_gen():
    n = 1
    while True:
        yield n**2
        n += 1


generator1 = f_gen()
generator2 = f_gen()

for i in generator1:
    print(i)
    if i > 10:
        generator1.close()


for i in generator2:
    print(i)
    if i > 10:
        generator2.throw(Exception("Плохо!"))





def generator(x):
    while True:
        x = yield x + 1


g = generator(5)
print(g.send(None))
print(g.send(10))