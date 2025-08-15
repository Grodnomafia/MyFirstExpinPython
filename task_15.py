films = [ 'Крепкий орешек', 'Назад в будущее', 'Таксист',
'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня',
'Проклятый остров', 'Начало', 'Матрица']
my_list = []


def testfilm(newfilm, list_films):
    for i_film in list_films:
        if i_film.lower() == newfilm.lower():
            return i_film
    return None

while True:
    print(f'Ваш текуший список фильмов {my_list}')
    addfilm = input('Введите названия фильма: ')
    new_films = testfilm(addfilm,films)
    if new_films:

        print('Команды: добавить, вставить, удалить')
        comands = input('Введите команду: ').lower()
        if comands == 'Добавить'.lower():
            my_list.append(new_films)
        elif comands == 'вставить':
            copy = int(input('На какое место вставить: '))
            my_list.insert(copy - 1 ,addfilm)
        elif comands == 'удалить':

            my_list.remove(new_films)

    else:
        print('Фильма нету в списке')
