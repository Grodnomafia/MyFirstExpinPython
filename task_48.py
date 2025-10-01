def test(text):
    polidr_list = dict()
    for i in text:
        if i in polidr_list:
            polidr_list[i] += 1
        else :
            polidr_list[i] = 1
    count = 0
    for i_new in polidr_list.values():
        if i_new % 2 != 0:
            count += 1
    if count <= 1:
        return 'yes'
    else :
        return 'no'


def main():
    text = input('Введите текст: ')
    polindrom = test(text)

    if polindrom == 'yes':
        print('Можно сделать полиндромом')
    else :
        print('Нельзя сделать полиндромом')




main()