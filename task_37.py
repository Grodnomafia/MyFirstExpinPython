


def check_ip(ip_part):
    parts = ip_part.split('.')

    if len(parts) != 4:
        print("Адрес — это четыре числа, разделённые точками.")
        return

    for part in parts:
        if not part.isdigit():
            print(f'{part}это не целое число')
            return
        part = int(part)
        if part < 0 or part > 255 :
            print(f'Число {part} должно быть от 0 до 255')
            return
    print('Ip adress- коректен')




def main():
    ip = input('Введите Ip-adress: ')
    finish = check_ip(ip)


main()