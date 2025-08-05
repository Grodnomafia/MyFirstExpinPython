worldlist = []
count = [0, 0, 0]
for i in range(3):
    print(f'Введите {i + 1} слово :', end = '')
    word = input(' ')
    worldlist.append(word)

text = input('Слово из текста: ')
while text != 'end':
    for index in range(3):
        if worldlist[index] == text:
            count[index] += 1
    text = input('Слова из текста: ')


for ai in range(3):
    print(f'{worldlist[ai]}Количество {count[ai]}')