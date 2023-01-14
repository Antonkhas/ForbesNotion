# создаем функцию с одним параметром func - она будет ссылкой на некую функцию
def func_dec(func):
    def wrapper():
        print('----- что-то делает перед вызовом функции -----')
        func()
        print('----- что-то делает после вызова функции -----')

    return wrapper


def some_func():
    print('Вызов функции some_func')


some_func = func_dec(some_func)
some_func()


print('///// 2 EXAMPLE /////')