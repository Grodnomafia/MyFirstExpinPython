first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')


if len(first_str) != len(second_str):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
else:

    found = False
    for shift in range(len(second_str)):

        shifted_str = second_str[shift:] + second_str[:shift]

        if shifted_str == first_str:
            print(f'Первая строка получается из второй со сдвигом {shift}.')
            found = True
            break

    if not found:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')