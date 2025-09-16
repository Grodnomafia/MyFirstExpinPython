
def coding(text):
    test_text = []
    count = 1
    new_text = text[0]
    for i in range(1, len(text)):
        if new_text == text[i]:
            count += 1
        else :
            test_text.append(new_text + str(count))
            new_text = text[i]
            count = 1
    test_text.append(new_text + str(count))
    return ''.join(test_text)






def main():
    print('Программа кодировки строк')
    print("Пример: 'aaaabbсaa' → 'a4b2с1a2'")
    text_user = input('Введите строку: ')
    finis_coding = coding(text_user)
    print(f'закодированая строка:{finis_coding}')




main()