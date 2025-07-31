num_monster = int(input('Введите количество монстров: '))
mage_num = int(input('Введите номер мага: '))
damage_monster = []
for _ in range(num_monster):
    print('урон у Монстр', _+1, end ='')
    damage = int(input(': '))

    damage_monster.append(damage)
for i_monster in range (num_monster):
    if damage_monster[i_monster] < 100 and i_monster != mage_num - 1:
        damage_monster[i_monster] += damage_monster[mage_num - 1]
print(f'Итоговый урон монстров {damage_monster}')




