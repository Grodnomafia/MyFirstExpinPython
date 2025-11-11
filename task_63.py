import zipfile
import os
from collections import Counter



def zipfail_unpack(zippath,extract_to=os.path.abspath('.')):
    try:
        with zipfile.ZipFile(zippath,'r') as zip_ref:
            zip_ref.extractall(extract_to)
            print(f"Архив распакован в папку: {extract_to}")
            return True
    except FileNotFoundError:
        print(f"Ошибка: файл {zippath} не найден")
        return False
    except zipfile.BadZipfile:
        print("Ошибка: поврежденный архив")
        return False

def search_txt(directory='.'):
    list_search_dir = []
    for i in os.listdir(directory):
        if i.endswith('.txt'):
            list_search_dir.append(os.path.join(directory,i))
    return list_search_dir
def count_letters(my_name):
    letters_count = Counter()
    try:
        with open(my_name, 'r', encoding='utf-8') as file:
            for i in file:

                for char in i:
                    if char.isalpha():
                        letters_count[char] += 1

    except FileNotFoundError:
        print(f'Ошибка: файл {my_name} не найден')
    except UnicodeDecodeError:
        print(f'Ошибка: не удалось прочитать файл {my_name}')
    return  letters_count

def main():
    zip_path = 'D:\\voina i mir.zip'
    zip_unpack = 'final-voina-i-mir.txt'
    if not zipfail_unpack(zip_path):
        return
    txt_files = search_txt()
    if not txt_files:
        print('тхт файлы не найдены')
        return
    print(f'Найденые файлы :{[os.path.basename(f) for f in txt_files]}')
    total_counter = Counter()
    for i in txt_files:
        print(f'Обрабатываем файл {os.path.abspath(i)}')
        file_counter = count_letters(i)
        total_counter += file_counter
    sorted_letters = total_counter.most_common()
    print("Выводим сколько букв в романе Война и Мир")
    totalsum = sum(total_counter.values())
    print(f'\t\t\t{totalsum}')
    print(f'Уникальных символов {len(total_counter)}')
    for i,(letter,count) in enumerate(sorted_letters[:20],1):
        mystatic = (count / totalsum) * 100
        print(f'{i:2d}. "{letter}" : {count:8d} раз ({mystatic:6.2f}%')

    with open(zip_unpack, 'w', encoding='utf-8') as my_result:
        my_result.write(f'Полная статистика букв ')
        for name, bykvs in  sorted_letters:
            my_result.write(f'эта буква {name} была в тексте количество раз {bykvs}\n')

main()
