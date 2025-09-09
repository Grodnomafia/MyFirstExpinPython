



def cesar(text, shift):
    alfavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    new_text = []
    for i in text:
        if i in alfavit:
            position = alfavit.index(i)
            new_position = (position + shift) % 33
            new_text.append(alfavit[new_position])
        else :
            new_text.append(i)
    return ''.join(new_text)





def main():
    my_text = input('введите текст: ')
    my_shift = int(input('Введите сдвиг: '))
    my_list = cesar(my_text, my_shift)
    print(my_list)


main()


