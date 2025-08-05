n = int(input("Количество контейнеров: "))
containers = []


for i in range(n):
    while True:
        weight = int(input(f"Введите вес контейнера {i + 1}: "))
        if weight > 200:
            print("Ошибка: вес не должен превышать 200.")
            continue
        if i > 0 and weight > containers[-1]:
            print("Ошибка: последовательность должна быть невозрастающей.")
            continue
        containers.append(weight)
        break

x = int(input("Введите вес нового контейнера: "))
if x > 200:
    print("Ошибка: вес нового контейнера не должен превышать 200.")
else:
    pos = 1
    for weight in containers:
        if x > weight:
            break
        pos += 1
    print(f"Номер, который получит новый контейнер: {pos}")