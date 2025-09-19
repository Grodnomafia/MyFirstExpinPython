def count_alfavit(text_count):
    count_up = 0
    count_lower = 0
    for i in text_count:
        if i.isupper():
            count_up += 1
        elif i.islower():
            count_lower += 1
    return count_up, count_lower

def main():
    text = input('Введите текст: ')


    new = count_alfavit(text)
    print(f'Количество заглавных букв:{new[0]}\nКоличество строчных букв:{new[1]}')

    # Up_alfa, low_alpfa = count_alfavit(text)
    # print('Количество заглавных букв:', Up_alfa)
    # print('Количество строчных букв:', low_alpfa)
main()



