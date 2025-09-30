while True:
    try:
        count_order = int(input('Введите количество заказов: '))
        if count_order <= 6:
            break
        print('Ошибка заказов может быть не больше 6')
    except ValueError:
        print('Ошибка, вводите только целые числа.')
        continue
main_orders = dict()
for i in range(count_order):
    order_num = input(["Первый заказ: ", "Второй заказ: ", "Третий заказ: ", "Четвертый заказ: ", "Пятый заказ: ", "Шестой заказ: ",][i]).title()
    order_temporary = order_num.split()
    if len(order_temporary) != 3:
        print('Ошибка, Должна быть "Фамилия" "Названия пиццы" "Количество"')
        continue
    order_name = order_temporary[0]
    pizza_name = ' '.join(order_temporary[1:-1])
    count_ord = int(order_temporary[-1])
    if order_name not in main_orders:
        main_orders[order_name] = {}
    if pizza_name not in main_orders[order_name]:
        main_orders[order_name][pizza_name] = 0
    main_orders[order_name][pizza_name] += count_ord
for i in sorted(main_orders.keys()):
    print(f'Человек по фамилии: {i}')
    for pizz, count in sorted(main_orders[i].items()):
        print(f'Пицца: {pizz}, количество: {count}')





