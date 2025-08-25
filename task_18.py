decod = []
newbit = []
fail = 0
pack = int(input('Количество пакетов: '))
for i in range(pack):
    print(f'Пакет под номером {i + 1}')
    for i_pack in range(4):
        bit = int(input(f'{i_pack + 1} бит: '))
        decod.append(bit)
    if decod.count(-1) <= 1:
        newbit.extend(decod)
    else :
        print('много ошибок в пакете')
        fail += 1
    decod = []
print(f'Полученая сообщения {newbit}')
print(f'Количество ошибок в сообщении {newbit.count(-1)}')
print(f'количество потеряных пакетов {fail}')
