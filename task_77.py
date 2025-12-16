import os


def search(start_dir = None, start_search = None)->str:
    if not start_search:
        start_search = 'D:\\'
    if not start_dir:
        start_dir = 'bin'

    try:
        os.chdir(start_search)
    except FileNotFoundError :
        print('Не удается найти Корень диска: ',start_search)
    for roots , dirs , files in os.walk(start_search):
        if start_dir in dirs:
            puth_dir = os.path.join(roots,start_dir)
            for _roots, _dirs, _files in os.walk(puth_dir):
                for i in _files:
                    result = os.path.join(_roots,i)
                    yield result
            return
    yield f'Не найдена'

root_start = input('Введите корень диска для поиска: ').strip()
dir_search  = input('Введите названия папки: ').strip()





x = search(start_dir=dir_search,start_search=root_start)
for i in x:
    print(i)
