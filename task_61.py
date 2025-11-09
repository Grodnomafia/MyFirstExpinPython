import os

with open('First_tour.txt', 'r') as my_fail:
    result = []
    K = my_fail.readline().strip()

    all_text = my_fail.readlines()
    for i in all_text:
        if i.strip():
            famaly,name,score = i.strip().split()
            if int(K) < int(score):
                result.append((name[0],famaly,int(score)))
    result.sort(key=lambda x: x[2] ,reverse = True)


with open('second_tour.txt', 'w',encoding='utf-8') as fail:
    fail.write(f'Количество участников {len(result)}\n')
    for num, (name,surname,score) in enumerate(result, 1):
        result_lines = f'{num}){name}.{surname} {score}\n'
        fail.write(result_lines)
