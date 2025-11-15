def foo(new):
    new_list = {}
    for count in new:
        new_list[count] = new_list.get(count, 0) + 1
    odd_coint = 0
    for odd in new_list.values():
        if odd % 2 != 0:
            odd_coint += 1
        if odd_coint > 1:
            return False
    return True
try:
    with open('world.txt', 'r', encoding='utf-8') as fail:
        for i in fail:
            new = i.strip()
            try:
                if  any(char.isdigit() for char in new):
                    raise ValueError
                result_palid = foo(new)
                if result_palid :
                    print(f'Полидром {new}')
                else:
                    print(f'Не является полидромом {new}')
                    raise Exception

            except ValueError:
                with open('errors.log', 'a', encoding='utf-8') as my_log:
                        my_log.write(f'{new}\n')
                        print(f'Полиндром не может состоять из цифр {new}')
            except Exception:
                with open('errors.log', 'a', encoding='utf-8') as my_log:
                        my_log.write(f'{new}\n')
except FileNotFoundError:
    print('Файл не найден')


