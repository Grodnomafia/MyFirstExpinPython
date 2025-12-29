
from typing import Callable,Any
def decor(func:Callable)->Callable:
    """Декратор делает сохроняет кэш"""
    cache = dict()
    def wrapper(n:int)->Any:
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper
@decor
def fibanachi(n:int)->Any:
    """Вычесляем фибаначи, прибовляем от числа два его последних"""
    if n < 2:
        return n
    return fibanachi(n - 1) + fibanachi(n - 2)
print(fibanachi(10))
