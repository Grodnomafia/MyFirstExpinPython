def count_mes(i):
    return  i.count('!') + i.count('?')

result_list = []


first_mes =input('первое сообщение: ')
two_mes=input('Второе сообщение: ')


first = count_mes(first_mes)
two = count_mes(two_mes)

if first > two:
    result_list.extend([first_mes , two_mes])
    result =' '.join(result_list)

elif two > first:
    result_list.extend([two_mes, first_mes])
    result = ' ' .join(result_list)
else :
    result = 'ой'

print(result)




