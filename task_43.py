import random
nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
nums_1, nums_2 = set(nums_1), set(nums_2)

print(nums_1)
print(nums_2)
print(f'Минимальный элемент 1-го множества{min(nums_1)}\nМинимальный элемент 2-го множества{min(nums_2)}')
nums_1.remove(min(nums_1)), nums_2.discard(min(nums_2))

a = random.randint(100, 200)
b = random.randint(100, 200)
nums_1.add(a),nums_2.add(b)
print('Случайное число для 1-го множества',a,'\nСлучайное число для 2-го множества',b)
print(nums_1,'\n',nums_2)
nums_3 = nums_1.union(nums_2)
print('Объединение множеств:',nums_3)
nums_4 = nums_1.intersection(nums_2)
print('Пересечение множеств:',nums_4 )
print(sorted(nums_2.difference(nums_1)))
