import os
def search(path,my_fail):
    list_file = []
    if not os.path.exists(path):
        return list_file
    try:
        for x in os.listdir(path):
            full_path = os.path.join(path,x)
            if x == my_fail and os.path.isfile(full_path):
                list_file.append(full_path)
            elif os.path.isdir(full_path):
                try:
                    new_result = search(full_path,my_fail)
                    list_file.extend(new_result)
                except PermissionError:
                    print(f'Отказано в доступе к директории: {full_path}')
                    continue
    except PermissionError:
        print(f'отказана в доступе {path}')

    return list_file





def main():
    text = input('Введите путь: ')
    fail = input('Введите файл: ')
    result = search(text,fail)
    if result:
        for i in result:
            print(f'Найденый файл {i}')
    else :
        print('Ошибка деректории не найдена')
main()