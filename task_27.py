a_border = int(input('Введите левую границу: '))
b_border = int(input('Введите правую границу : '))


cube_border = [i ** 3 for i in range(a_border, b_border + 1 )]
square_border = [i ** 2 for i in range(a_border, b_border + 1 )]

print(f'Список кубов чисел в диапазоне от {a_border} до {b_border}: {cube_border}')
print(f'Список квадрат чисел в диапазоне от {a_border} до {b_border}:{square_border}')