
N = int(input("Введите число: "))
odd_numbers = []
for num in range(1, N+1):
    if num % 2 == 1:
        odd_numbers.append(num)
print(f"Список из нечётных чисел от одного до N: {odd_numbers}")