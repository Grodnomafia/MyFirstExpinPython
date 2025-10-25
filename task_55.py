def temperary(n):
    if not n:
        return [],[],[]

    support = n[-1]
    min,medium,max = [], [], []
    for i in n:
        if support > i:
            min.append(i)
        elif support == i:
            medium.append(i)
        elif support < i:
            max.append(i)
    return min,medium,max,support
def foo(x):
    if len(x) <= 1:
        return x


    min,medium,max,supp = temperary(x)
    min_new =foo(min)
    max_new = foo(max)
    return min_new + medium + max_new




def main():
    my_list = [4, 9, 2, 7, 5]
    min_list,medium_list,max_list,support_num = temperary(my_list)
    print(f'Принятые данные {my_list}')
    print(f'Опорное число {support_num}\nМеньше опорного {min_list}\nРавные опорному{medium_list}\nБольше опорного{max_list}')
    result = foo(my_list)
    print('Результат =',result)

main()