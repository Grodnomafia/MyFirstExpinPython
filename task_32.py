def ipadres(list_adress,count):
    while 4 > count :
        try:
            ip_addres = int(input(f'Введите {count + 1} число от 0 до 255: '))
            if ip_addres > 255 or ip_addres < 0:
                print('ошибка ввода надо водить с 0 до 255')
            else :
                list_adress.append(str(ip_addres))
                count += 1
        except ValueError:
            print('Введите целое число')
    return '.'.join(list_adress)


def main():
    count = 0
    list_adress = []
    print("-" * 20)
    print(f'Ващ ip адрес: {ipadres(list_adress,count)}')
    print("-" * 20)

main()