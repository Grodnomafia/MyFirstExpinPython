import os
import random



def search_path(my_path,fail):
    my_list = []
    if not os.path.exists(my_path):
        return my_list
    try:
        for i in os.listdir(my_path):

            full_path = os.path.join(my_path,i)
            if fail.lower() == i.lower() and os.path.isfile(full_path):
                my_list.append(full_path)

            elif os.path.isdir(full_path):
                try:
                    new_result = search_path(full_path,fail)
                    my_list.extend(new_result)
                except PermissionError:
                    print(f'Отказана в доступе {full_path}')
                    continue

    except PermissionError:
        print(f'Ошибка в доступе {my_path}')
    return my_list

def search_read(read_fail):
    if not read_fail:
        print('нету файла для выбора')
        return None
    random_text = random.choice(read_fail)
    print(f'Рандомный путь {random_text}')
    print('.' * 50)
    final = open(f'{random_text}','r' , encoding='utf-8')
    for i in final:
        print(i,end='')
def main():
    path = input('Введите путь поиска: ').strip()
    search_fail = input('введите названия файла: ').strip()
    result = search_path(path,search_fail)
    read = search_read(result)


main()

