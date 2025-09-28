def pair_check(count):
    pair_list = dict()
    for i in range(count):
        if i == 0:
            signature = 'Первая пара: '
        elif i == 1:
            signature = 'Вторая пара: '
        elif i == 2:
            signature ='Третья пара: '
        else :
            signature = f'{i + 1} пара: '
        pait = input(f'{signature}').strip()
        if '--' in pait:
           words = pait.split('--')
        elif '-' in pait:
            words = pait.split('-')
        elif ' ' in pait:
            words = pait.split(' ')
        else:
            print('Некорректный формат пары. Используйте разделитель "--", "-" или пробел.')
            continue
        if len(words) != 2:
            print('Не верный формат должно быть 2 слова между разделителям')

        word1 = words[0].strip()
        word2 = words[1].strip()

        pair_list[word1.lower()] = word2
        pair_list[word2.lower()] = word1
    return  pair_list




def first():
    try:
        quantity = int(input('Введите количество пар: '))
        if quantity <= 0:
            print('Ошибка ,число пар должно быть положительным')
            return
    except:
        print('Некоретный ввод , число должно быть целым')
        return

    pair_list = pair_check(quantity)

    while True:
        search_sim = input('Ведите слова').strip()
        if not pair_list:
            print('Вы вели пустую строку')
            continue
        synonym = pair_list.get(search_sim.lower())
        if synonym:
            print(f"Синоним: {synonym}")
            break
        else:
            print("Такого слова в словаре нет.")


first()