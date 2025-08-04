

words = list(input('Введите строку: '))
number = int(input('введите номер символа: ')) - 1

if words[number]  == words[number - 1] and words[number + 1] == words[number]:
    print(f'Символ слево {words[number-1]}\nСимвол справа {words[number+1]}')

    print(f'\nСимволы с обеих сторон {words[number]} ')
elif words[number] == words[number-1]:
    print(f'Символ слево {words[number-1]}\nСимвол справа {words[number+1]}')
    print('\nесть ровно один такой же символ.')
elif words[number] == words[number + 1]:
    print(f'Символ слево {words[number - 1]}\nСимвол справа {words[number + 1]}')
    print('\nесть ровно один такой же символ.')
else :
    print('Таких же символов нету')
