import os
def program_dir(text):
    abs_list =os.path.abspath(text)
    if  not os.path.exists(abs_list):
        print('Ошибка такой директории не существует')
        return
    if not os.path.isdir(abs_list):
        print('Ошибка , не является директорией ')
        return
    try :
        final_list = os.listdir(abs_list)
        for items in final_list:
            result = os.path.join(abs_list,items)
            print(f'   {result}')
    except PermissionError:
        print('Ошибка , нет доступа и прав к указаной директории')
my_text = input("Введите путь к директории (или нажмите Enter для текущей): ").strip()
if not my_text:
    my_text = '.'

program_dir(my_text)
