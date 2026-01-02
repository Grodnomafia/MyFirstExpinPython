from abc import ABC,abstractmethod

class Auto_park(ABC):
    def __init__(self,color,speed):
        self.color = color
        self.speed = speed
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def signal(self):
        pass

    def __str__(self):
        return (f'{self.speed} - {self.color}')
class Primes:
    def music(self,name):
        print(f'Тут играет какая та музыка{name}')


class Car(Auto_park):
    def move(self):
        print(f'Транспорт {self.color} двигается  со скоростью {self.speed} по земле')

    def signal(self):
         print(f'Бииип-Биппп')
    def operate(self):
        print('Ездит только по земле')
class Amfib(Auto_park,Primes):
    def __init__(self,color:str = 'Red', speed: int = 0,mode:bool = True):
        super().__init__(color,speed)
        self.mode = mode
    def move(self):
        if self.mode :
            print(f'Транспорт двигается со скоростью {self.speed} по земле')
        else:
            print(f'Транспорт двигается со скоростью {self.speed} по воде')
    def switch(self):
        self.mode = not self.mode
        print(f'Переключили режим теперь ')

    def signal(self):
         print(f'Бииип-Биппп')
    def operate(self):
        print('Ездит только по земле и по воде')

class Boats(Auto_park):
    def move(self):
        print(f'Транспорт {self.color} двигается со скоростью {self.speed}')

    def signal(self):
        print(f'Бииип-Биппп')

    def operate(self):
        print('Плывут только по воде')


test2 = Amfib('Blue', 20)
print(test2)
test2.music('Лондан')
test2.signal()
test2.move()
test2.switch()
test2.move()

# У нас есть парк транспорта. У каждого транспорта есть цвет и скорость, и каждый умеет двигаться и подавать сигнал. В парке транспорта стоят:
# ● Автомобили. Они могут ездить только по земле.
# ● Лодки. Ездят только по воде.
# ● Амфибии. Могут перемещаться и по земле, и по воде.
# Напишите код, который реализует соответствующие классы и методы. Класс «Транспорт» должен быть абстрактным и содержать абстрактные методы.
# Также добавьте класс-примесь, в котором реализован функционал проигрывания музыки. «Замешайте» этот класс в «Амфибию»