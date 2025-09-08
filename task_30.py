my_list = input('Введите список: ')

start_list = my_list.find('h')
end_list = my_list.rfind('h')
if start_list != end_list:
    answer_list = my_list[start_list + 1:end_list:]
    answer_list = answer_list[::-1]
else :
  answer_list = ''

print(f'Развёрнутая последовательность между первым и последним h:{answer_list}')