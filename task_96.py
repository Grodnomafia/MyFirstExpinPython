from typing import Type, Callable, TypeVar,List

T = TypeVar('T')
R =TypeVar('R')


def  make_pair(first:T,two:R)->tuple[T,R]:
    newdata = tuple((first,two))
    return newdata
def get_first(data:tuple[T,R])->T:
    return data[0]

def get_two(data:tuple[T,R])->R:
    return data[1]
def change(data:tuple[T,R])->tuple[R,T]:
    return (data[1],data[0])
result = make_pair('artem',123)
result1 = get_first(result)
result2 = get_two(result)
result3 =change(result)
print(result3)
print(result1)
print(result2)
print(type(result2))
