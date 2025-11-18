import  random
def main():
    count = 0
    finish_count = 777
    try:
        with open('out_file.txt', 'w') as my_fail:
            while count <  finish_count:
                players_number = int(input('Введите число: '))
                count += players_number
                if random.randint(1, 13 ) == 1:
                    raise Exception('Вас постигла неудача')
                my_decod = str(players_number)
                my_fail.write(f'{my_decod}\n')



    except ValueError:
        print('Вводите только целые числа ')
    except Exception as e:
        print(f'{e}')
    else:
        print('Програма сработала успешна')



main()
