

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


def check(list, name ):
        return name in list

while True:


    print(f'Сейчас на вечеринке {len(guests)} : человек {guests}')

    message = input('Гость пришёл или ушёл? ')
    if message.capitalize() == 'Пора спать':
            print('Вечеринка закончилась, все пошли спать')
            break
    if message.capitalize() == 'Пришел':
            in_people = input('Имя гостя:').capitalize()
            if not check(guests , in_people):
                if len(guests) < 6:
                        guests.append(in_people)
                        print(f'Привет, {in_people}')
                else :
                    print(f'Прости, {in_people} но мест нет.')

    elif message.capitalize() == 'Ушел':
            in_people = input('Имя гостя:').capitalize()
            if check(guests, in_people):
                guests.remove(in_people)
                print(f'Пока, {in_people}')
            else :
                    print('Такого имени нету в списке')
    else :
            print('Введите "Пришел" или "Ушел"')




