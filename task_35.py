
def test_main(password_main):
    char = 0
    if len(password_main) < 8:
        return False
    check_pass = any(i.isupper() for i in password_main)
    if not check_pass:
        return  False
    check = sum(1 for i in password_main if i.isdigit())
    if check < 3:
        return False
    return True



def main():
    print("Придумайте пароль (должен содержать минимум 8 символов,")
    print("хотя бы одну заглавную букву и не менее 3 цифр)")
    while True:
        password = input('Придумайте пороль: ')
        if test_main(password):
            print('Это надежный пороль!')
            break
        else :
            print('Пароль ненадёжный. Попробуйте ещё раз.')



main()

