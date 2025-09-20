
def main():

    my_list = dict()
    while True:
        print(f'Текущие контакты на телефоне:')
        if not my_list:
            print('<Пусто>')
        else:
            print(f'{my_list}')
        name = input('Введите имя: ')
        if name.lower() == 'стоп':
            print('Конец программы')
            break
        telephone = input('Введите номер телефона: ')
        if  telephone.lower() == 'стоп':
            print('Конец программы')
            break

        if name in my_list:
            print('Ошибка: такое имя уже существует.')
            continue
        my_list[name] = telephone

        print('Если хотите выйти с справочника напишите "Стоп"')









main()

