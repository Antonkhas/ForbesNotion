def get_list():
    for x in [1, 2, 3, 4]:
        yield x


a = get_list()
for x in a:
    print(x)


print('--------- 2 example---------')
num1 = 10
num2 = 20


def itog():
    yield num1 + num2
    yield num1 * num2
    yield num1 / num2


for i in itog():
    print(i)


print('--------- 3 example---------')

mylist = [10, 15, 20, 30, 35]

def mod(mylist):
    for i in mylist:
        if (i % 10 == 0):
            yield i


for i in mod(mylist):
    print(i)

