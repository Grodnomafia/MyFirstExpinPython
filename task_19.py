people = int(input('Введите количество участников: '))
group_peop = int(input('Количество в команде: '))
members = []
count = 1
if people % group_peop == 0:
    for i in range(people // group_peop):
        members.append(list(range(count, count + group_peop )))
        count += group_peop
    for i in members:
        for i_new in i:
            print(i_new, end = ' ')
        print()

else :
    print(f'{people} невозможно поделить на команды по {group_peop} ')





