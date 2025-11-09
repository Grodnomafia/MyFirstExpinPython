import os
def counting_program(path):
    count = 0
    my_dir = 0
    my_fail = 0
    if os.path.exists(path):
        for i in os.listdir(path):
            try:
                new_path = os.path.join(path,i)
                if os.path.isfile(new_path):
                    count += os.path.getsize(new_path)
                    my_fail += 1
                elif os.path.isdir(new_path):
                    new_result,sub_dir,sub_fail = counting_program(new_path)
                    count += new_result
                    my_dir += 1
                    my_dir += sub_dir
                    my_fail += sub_fail
            except PermissionError:
                print(f'отказ доступа {new_path}')
                continue

        return count,my_dir,my_fail

def main():
    my_path = input('Введите путь к каталогу:')
    if not my_path:
        print('Путь не может быть пустым')
        return
    result = counting_program(my_path)
    if result :
        result, quantity_dir, quantity_fail = result

        kb_result = result // 1024
        mb_result = kb_result // 1024
        gb_result = mb_result // 1024
        print("*" * 50)
        print(f'Общее количество файлов в этой деректории \n{kb_result} кб {result} байт {mb_result} мегабайт {gb_result} гигабайт')
        print(f'Количество файлов в деректории {my_path} : {quantity_fail}')
        print("*" * 50)
        print(f'Количество директорий в деректории {my_path} : {quantity_dir}')
    else:
        print('Нету такого пути')

main()