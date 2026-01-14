import datetime
import functools
from datetime import datetime
import time

def createtime(cls):
    @functools.wraps(cls)
    def wrapper(*args,**kwargs):
        instance = cls(*args,**kwargs)
        print(f'Время создания {datetime.now()}')
        return instance
    return wrapper

def decorat(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        print(f'{func.__name__} выполнен: {round(time.time()- start_time, 4)}')
        return result
    return wrapper
def all_methods(decorat):
    @functools.wraps(decorat)
    def decorate(cls):
        for i in dir(cls):
            if not i.startswith('__'):
                new_method = getattr(cls,i)
                decorat_method = decorat(new_method)
                setattr(cls,i,decorat_method)
        return cls
    return decorate
@createtime
@all_methods(decorat)
class Functions:
    def __init__(self,max_num:int)->None:
        self.max_num = max_num

    def squares_sum(self)-> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(self.max_num)])
        return result

    def cubes_sum(self,number:int)-> int:
        result = 0
        for _ in range(number):
            result += sum([i_num ** 3 for i_num in range(self.max_num)])
        return result


mu_func_1 = Functions(max_num = 4)
print(mu_func_1.cubes_sum(number = 2000))
mu_func_1.squares_sum()