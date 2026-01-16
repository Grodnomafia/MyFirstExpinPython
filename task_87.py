import functools
from datetime import datetime
def logging(cls):
    for name_method in dir(cls):
        if not name_method.startswith('__'):
            method = getattr(cls,name_method)
            if callable(method):
                def the_wrapper(name = name_method,method = method):
                    @functools.wraps(method)
                    def wrapper(*args,**kwargs):
                        great_time = datetime.now()
                        print(f'Метод названия {name}')
                        print(f'Создания метода {great_time}')
                        print(f'Документация метода {method.__doc__}')
                        method_args = f'Аргументы метода: {args[1:] if args else args}'
                        print(method_args)
                        print(f'Кваргц метода {kwargs}')
                        result = method(*args,**kwargs)
                        print(f'Результат : {result}')
                        log_entry = f'''
                        Метод названия {name}
                        Создания метода {great_time}
                        Документация метода {method.__doc__}
                        Аргументы метода: {method_args}
                        Кваргц метода {kwargs}
                        Результат : {result}
                        {'=' * 40}
                        '''
                        with open('Inform.txt', 'a', encoding='utf-8') as x:
                            x.write(log_entry)

                        return result
                    return wrapper
                setattr(cls,name_method,the_wrapper(name_method,method))

    return cls

@logging
class Myclass:
    def method(self,*args,**kwargs):
        """АНАТАЦИЯ МЕТОД 1"""
        new = 1
        result = sum(args) ** 20
        return result
    def method_2(self,num):
        """АНАТАЦИЯ МЕТОД 2"""
        new = 2
        result = num // 20
        return result
    def method_3(self,*args,**kwargs):
        """АНАТАЦИЯ МЕТОД 3"""
        new = 3
        result = dict()
        for key,vallues in kwargs.items():
            if isinstance(vallues,(float,int)):
                result[key] = vallues % 10
        return result


test = Myclass()
print(test.method(2,3,4,5))
print(test.method_2(2))
print(test.method_3(num = 3,long= 4))
