quantity = int(input('Введите количество сотрудников : '))
my_list = []
for i in range(quantity):
    salary = int(input(f'Введите зарплату сотрудника {i + 1}: '))
    my_list.append(salary)

    if salary == 0:
        my_list.remove(salary)
count = len(my_list)

print(f'Осталась сотрудников {count}')
print(f'Зарплаты: {my_list}')
print(f'Максимальная зарплата сотрудника {max(my_list)}')
print(f'Минимальная зарплата сотрудника {min(my_list)}')