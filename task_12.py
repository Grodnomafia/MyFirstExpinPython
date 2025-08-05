films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон',
         'Богемская рапсодия', 'Город грехов', 'Мементо',
         'Отступники', 'Деревня']

quantity = int(input('Сколько фильмов хотите добавить? '))
my_films = []

for i in range(quantity):
    film = input(f'Введите название {i+1} фильма: ')
    if film in films:
        my_films.append(film)
    else:
        print(f'Ошибка: фильма "{film}" нет в нашем списке')

print('\nВаш список любимых фильмов:', ', '.join(my_films))