import copy
def foo(my_list,name):
    if 'title' in my_list:
         my_list['title'] = f'Куплю/продам {name} недорого'
    if 'h2' in my_list:
         my_list['h2'] = f'У нас самая низкая цена на {name}'
    for i in my_list.values():
        if isinstance(i, dict):
            foo(i,name)
    return my_list



def main():
    site = {
            'html': {
                'head': {
                    'title': 'Куплю/продам телефон недорого'
                        },
                'body': {
                    'h2': 'У нас самая низкая цена на iPhone',
                    'div': 'Купить',
                    'p': 'Продать'
                        }
                    }
            }
    my_exmaple = list()
    try:
        quantity_site = int(input('Сколько сайтов? '))
    except ValueError:
        print('Введите целое число')
    for i in range(quantity_site):
        product_name = input('Введите названия продукта для нового сайта: ')
        newsite = copy.deepcopy(site)
        foo(newsite,product_name)
        my_exmaple.append((product_name,newsite))

        for product_name, site_structure in my_exmaple:
            print(f'\nСайт для: {product_name}')
            print('Структура сайта:')
            print(site_structure)


main()