import os
if not os.path.exists('my_chat.txt'):
    with open('my_chat.txt', 'w', encoding='utf-8') as my_chat_great:
        my_chat_great.write(f'=======Добро Пожаловать в чат=======\n')
try:
    while True:
        try:
            name = input('ВВедите свое имя: ').strip()
            if not name:
                raise ValueError('Ошибка, имя не может быть пустым')
            if not name.isalpha():
                raise ValueError('Ошибка , имя не может содержать цифры')
        except ValueError as e:
            print(e)
            continue
        print('1. Посмотреть текущий текст чата')
        print('2. Отправить сообщение (затем вводит сообщение).')
        print('3. Выйти с программы ')
        try :
            choice = input('Выберите действие (1/2/3):').strip()
            if choice == '1':
                with open('my_chat.txt', 'r', encoding='utf-8') as my_read_chat:
                    print(my_read_chat.read())
            elif choice == '2':
                with open('my_chat.txt', 'a', encoding='utf-8') as my_fail:
                    messege_chat = input('Введите сообщения: ').strip()
                    if messege_chat :
                        my_fail.write(f'{name} : {messege_chat}\n')
                        print('====Сообщение отправленно====')
                    else:
                        print('Сообщения не может быть пустым')
            elif choice == '3':
                print(f'Досвидание {name}')
                break
            else:
                raise FileNotFoundError('Ошибка вводите только 1 или 2')
        except FileNotFoundError as e:
            print(e)
except KeyboardInterrupt as x:
    print(x)
except Exception as x:
    print(f'Ошибка {x}')


