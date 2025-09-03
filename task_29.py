import random

one_squad = [random.randint(50 , 80) for _ in range(10)]
two_squad = [random.randint(30, 60 )for _ in range(10)]
three_squad = [('Погиб' if one_squad[count] + two_squad[count] > 100 else 'Выжил' ) for count in range(10)]
print(f'Первый отряд {one_squad}')
print(f'Второй отряд {two_squad}')
print(f'Третий отряд{three_squad}')