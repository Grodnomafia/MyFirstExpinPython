from abc import ABC,abstractmethod
class Figura(ABC):
    def __init__(self,x,y,long,width):
        self.y= y
        self.x = x
        self.width = width
        self.long = long

    def changeCordinate(self, new_x, new_y):
        self.y = new_y
        self.x = new_x


    def __str__(self):
        return f'Кардинаты х = {self.x} у = {self.y}\nВысота = {self.width} Длинна = {self.long}'
class Primes:
    def changesize(self,new_width,new_long):
        self.width = new_width
        self.long  = new_long


class Rectangle(Figura,Primes):
    pass


class Square(Figura,Primes):
    def __init__(self,x,y,width):
        super().__init__(x,y,width,width)




test = Rectangle(1,2,20,30)
test.changeCordinate(50,100)
test2 = Square(3,4,30)
test2.changeCordinate(7,8)
test.changesize(4,4)
print(test)



for i in [test,test2]:
    new = i.width * 2
    new1 = i.long * 2
    i.changesize(new,new1)
print(test)
print(test2)