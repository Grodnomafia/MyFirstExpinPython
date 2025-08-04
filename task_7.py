S = input("Введите строку: ")

# Преобразуем строку в список символов для удобства замены
chars = list(S)
replacements = 0

for i in range(len(chars)):
    if chars[i] == ':':
        chars[i] = ';'
        replacements += 1

# Собираем список обратно в строку
new_S = ''.join(chars)

print(f"Исправленная строка: {new_S}")
print(f"Количество замен: {replacements}")