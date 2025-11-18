with open('regestrations.txt', 'r', encoding='utf-8') as my_fail:
    erors_logs = []
    good_logs = []
    for i_line in my_fail:
        i_line = i_line.strip()
        if not i_line:
            continue
        parts = i_line.split()
        try:
            if len(parts) == 3:
                name, emeil, age_str = parts
                name_ok = True
                email_ok = True
                age_ok = True
            else :
                raise Exception
            try:
                age = int(age_str)
                if age > 99 or age < 10:
                    erors_logs.append(f' {parts} Поле «Возраст» НЕ представляет число от 10 до 99')
                    age_ok = False
            except ValueError:
                erors_logs.append(f' {parts} Поля возраст содержит буквы, ошибка')
                age_ok = False


            if '@' not in emeil or '.' not in emeil:
                erors_logs.append(f'{parts} Поле «Имейл» НЕ содержит @ и точку')
                email_ok = False
            if not name.isalpha():
                erors_logs.append(f'{parts} Поле с именем содержит цифры  ')
                name_ok = False
            if name_ok and email_ok and age_ok :
                good_logs.append(f'Правильные контакты : {parts}')



        except Exception as e:
            erors_logs.append(f'Ошибка обработки {parts}')


with open('registrations_bad.log', 'w', encoding='utf-8') as bad_fail:
    for i_bad in erors_logs:
        bad_fail.write(f'Неправельные контакты : {i_bad}\n')
with open('registrations_good.log','w', encoding='utf-8') as good_fail:
    for i_good in good_logs:
        good_fail.write(f'{i_good}\n')