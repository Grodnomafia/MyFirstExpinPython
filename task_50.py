
my_contact = dict()

while True:

    print('\tПрограмма контакты')
    if my_contact:
        print(f'Текуший список контактов {my_contact}')

    print('1.Добавить контакт.\n2.Найти человека.\n3.Конец программы.')
    you_request = input(f'Введите номер действия:').strip()
    if you_request == '1':
        name = tuple(input('Введите имя и фамилию нового контакта(через пробел): ').split())
        if len(name) != 2:
            print('Ошибка, Введите имя, фамилию через пробел.')
            continue
        if name in my_contact:
            print('Такой человек уже есть в контактах.')
            continue
        telefon = input('Введите номер телефона: ').strip()
        my_contact[name] = telefon


    elif you_request == '2':
        search = input('Введите фамилию для поиска: ').strip()
        test = False
        for i in my_contact.keys():
            if search in i[1]:
                print(f'{' '.join(i)} {my_contact[i]}')
                test = True
        if  not test:
            print('Контакт не найден')





    elif you_request == '3':
        print('Конец программы ')
        break
    else :
        print('Ошибка ввода , ввод должен быть 1,2,3')
        continue




