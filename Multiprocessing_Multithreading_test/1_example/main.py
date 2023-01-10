import time
import threading

# запускаю поток с промежутком 1 сек
def test():
    while True:
        print('test')
        time.sleep(1)

# указываю что этот поток должен запускаться только через 5 секунд
thr = threading.Timer(5, test)
thr.start()

# здесь укажу, что этот поток будет работать 3 секунды
for _ in range(3):
    print('111')
    time.sleep(1)

thr.cancel()
print('finish')