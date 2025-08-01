count_dogs = int(input('Введите количество собак: '))
list_dogs =[]
for inde in range(count_dogs):
    print(f'Под номерам#{inde + 1} собака',end=' ')
    dogs = int(input('имеет очков: '))
    list_dogs.append(dogs)

max_score= max(list_dogs)
min_score = min(list_dogs)
max_index = list_dogs.index(max_score)
min_index = list_dogs.index(min_score)
max_score , min_score = min_score , max_score
print(f'\tсобака под индексом {max_index + 1 }имеет {max_score}')
print(f'\tсобака под индексом {min_index + 1}имеет {min_score}')

