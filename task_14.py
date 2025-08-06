def palindrom(word):

    word = word.lower()

    return word == word[::-1]







variabl = input('Введите слово: ')

if palindrom(variabl):
    print(' Слово является палиндромом')
else :
    print('Слово не является палиндромом')