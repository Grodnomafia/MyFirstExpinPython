def my_program(all_list,key,temporary = 0,depth = None):
    if depth is not None and temporary >= depth:
        return None
    if key in all_list:
        return all_list[key]

    for i in all_list.values():
        if isinstance(i , dict):
            result = my_program(i, key, temporary + 1, depth)
            if result is not None:
                return result
    return None

def main():
    site = {
        'html': {
            'head': {
                'title': 'Мой сайт'
            },
            'body': {
                'h2': 'Здесь будет мой заголовок',
                'div': 'Тут, наверное, какой-то блок',
                'p': 'А вот здесь новый абзац'
            }
        }
    }

    text = input('Введите искомый ключ: ')
    argument = input('Хотите ввести максимальную глубину:Y/N ' ).lower()
    depth = None
    if argument == 'y':
        depth = int(input('Введите глубину: '))

    result = my_program(site,text,depth=depth)

    if result is not None:
        print(f'Значения ключа {text} : {result}')
    else :
        print('Ключ не найден')


main()