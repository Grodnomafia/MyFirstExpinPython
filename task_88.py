from functools import wraps
import time
import datetime
from typing import Any,Callable

def log_methods(data_format:str)->Callable:
    def cls_method(cls:type)->type:
        for name in dir(cls):
            if name.startswith('__'):
                continue
            method = getattr(cls,name)
            if callable(method):
                def the_wrapper(name:str,method:Callable)->Callable:
                    @wraps(method)
                    def wrapper(*args:Any,**kwargs:Any)->Any:
                        great_method = datetime.datetime.now()
                        new_format = great_method.strftime(data_format)
                        print(f'Запускается {cls.__name__}.{name} .Дата и время запуска:{new_format}')
                        print(f'{cls.__doc__} {method.__doc__}')
                        start_work_time = time.time()
                        result = method(*args,**kwargs)
                        print(f'Завершение "{cls.__name__}.{name}", время работы = {round(time.time()-start_work_time,3)}')
                        print(f'результат = {result}')
                        return result
                    return wrapper
                setattr(cls,name,the_wrapper(name,method))
        return cls
    return cls_method

@log_methods("%b %d %Y — %H:%M:%S")
class A:
    """АНАТАЦИЯ КЛАССА А"""
    def test_sum_1(self)-> int:
        """АНАТАЦИЯ МЕТОДА TEST_SUM_1"""
        print('тут метод test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result

@log_methods("%b %d %Y — %H:%M:%S")
class B(A):
    """АНАТАЦИЯ КЛАССА Б"""
    def test_sum_1(self)->int:
        """АНАТАЦИЯ МЕТОДА TEST_SUM_1"""
        result = super().test_sum_1()
        print('Тут метод у наследника test_sum_1')
        return result


    def test_sum_2(self)->int:
        """АНАТАЦИЯ МЕТОДА TEST_SUM_2"""
        print(" тут метод  у наследника test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
# Результат:
# Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 — 21:50:37. 
# Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 — 21:50:37. 
# Тут метод test_sum_1.
# Завершение 'A.test_sum_1', время работы = 0,187 s. 
# Тут метод test_sum_1 у наследника.
# Завершение 'B.test_sum_1', время работы = 0,187 s. 
# Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 — 21:50:37. 
# Тут метод test_sum_2 у наследника.
# Завершение 'B.test_sum_2', время работы = 0,370 s.