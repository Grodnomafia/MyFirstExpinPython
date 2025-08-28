basic = [1, 5, 3]
side = [1, 5, 1, 5]
side_two = [1, 3, 1, 5, 3, 3]

basic.extend(side)

print(f'Количество цифр 5 = {basic.count(5)}')
print(f'1 раз измененый список: {basic}')
while 5 in basic:
    basic.remove(5)
print(f'2 раз измененый список:  {basic}')
basic.extend(side_two)
print(f'3 раз измененый список: {basic}')
print(f'Количество цифр 3 = {basic.count(3)}')



