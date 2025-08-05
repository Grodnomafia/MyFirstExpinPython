# Ввод количества видеокарт
n = int(input('Количество видеокарт: '))
old_list = []

# Заполняем список видеокартами
for i in range(n):
    card = int(input(f'Видеокарта {i+1}: '))
    old_list.append(card)

# Находим максимальное значение
max_card = max(old_list)

# Создаем новый список без максимальных значений
new_list = [card for card in old_list if card != max_card]

# Выводим результаты
print('\nСтарый список видеокарт:', old_list)
print('Новый список видеокарт:', new_list)