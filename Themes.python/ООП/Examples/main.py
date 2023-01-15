from abc import ABC, abstractmethod

# Абстрактный класс можно определить с помощью класса abc.ABC, а абстрактный метод определить с помощью abc.abstractmethod


# Можно определить некоторые общие вещи в абстрактном методе и использовать функцию super() для вызова его в подклассах.
class Animal(ABC):
    @abstractmethod
    def move(self):
        print('Animal moves')


class Cat(Animal):
    def move(self):
        super().move()
        print('Cat moves')


c = Cat()
c.move()

# Совместно с @abstractmethod можно использовать дескриптор класса  -@property,
# метод класса - @classmethod и статический метод класса - @staticmethod.