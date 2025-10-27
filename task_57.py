import os
def fail_system(my_path):
    if not os.path.exists(my_path):
        print('указаный путь , не существует')
    if os.path.isdir(my_path):
        print('Это папка')
    elif os.path.isfile(my_path):
        size = os.path.getsize(my_path)
        print(f'Это файл\nРазмер файла - {size}')
    elif os.path.islink(my_path):
        print('Это сылка')


def main():
    demo_path = input('Введите путь: ').strip()
    test = fail_system(demo_path)


main()