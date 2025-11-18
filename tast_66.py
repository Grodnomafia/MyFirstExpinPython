def validator(data):
    if len(data) != 3:
        raise IndexError('НЕ присутствуют все три поля')
    name, emeil, age_str = data
    try:
        age = int(age_str)
    except ValueError:
        raise ValueError('Поля возраст не представляет целое число')
    if age < 10 or age > 99:
        raise ValueError('Поля возраст не представляет целое число от 10 до 99')
    if '@' not in emeil or '.' not in emeil:
        raise SyntaxError('Поля емейл не содержит @ или точку ')
    if not name.isalpha():
        raise NameError('Поля с именем содержит не только буквы')
    return True





def main():
    with open('regestrations.txt', 'r', encoding='utf-8') as my_fail:
        erors_logs = []
        good_logs = []
        for i_line in my_fail:
            i_line = i_line.strip()
            if not i_line:
                continue
            parts = i_line.split()
            try:
                if validator(parts):
                    good_logs.append(i_line)
            except (IndexError, NameError, SyntaxError, ValueError) as e:
                    erors_logs.append(f'{i_line:<40} {e}')

    with open('registrations_bad.log', 'w', encoding='utf-8') as bad_fail:
        for i_bad in erors_logs:
            bad_fail.write(f'Неправельные контакты : {i_bad}\n')
    with open('registrations_good.log','w', encoding='utf-8') as good_fail:
        for i_good in good_logs:
            good_fail.write(f'{i_good}\n')

main()