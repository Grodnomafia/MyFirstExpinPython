class Student:

    def __init__(self,full_name , group_num, grade):
        self.name = full_name
        self.group = group_num
        self.grade = grade

    def calculatr(self):
        return sum(self.grade) / len(self.grade)

    def print_result(self):
        return (f'{self.name}|группа: {self.group} |оценки: {self.grade}'
                f'|средний бал: {self.calculatr():.2f}')


# list_student = [Student(input('Введите имя'), input('Введите группу'),
# [int(input('введите бал:')) for j in range(2)]) for i in range(2)]
def creat_student_manual():
    student_list = []
    try:
        for i in range(3):
            name = input('Введите имя и фамилию: ').strip()
            if not name:
                print('Ошибка имя не может быть пустым')
                continue
            elif not name.replace(' ', '').isalpha():
                print('Ошибка имя должно содержать только буквы')
            num_gr = input('Введите номер группы: ').strip()
            if not num_gr:
                print('Ошибка , номер группы не может быть пустым')
                continue
            grades = []

            for y in range(3):
                try:
                    grade = int(input('Введите балл: '))
                    if grade < 1 or grade > 5:
                        print('Ошибка , введите бал от 1 до 5')
                        grade = int(input('Введите балл: '))
                    grades.append(grade)
                except ValueError:
                    print('Ошибка вводите только цифры')
                    grade = int(input('Введите балл: '))
                    grades.append(grade)
            student_list.append(Student(name,num_gr,grades))
    except Exception as e:
        print(f'{e}')




    return student_list

def main():
    while True:
        try:
            print('=====Программа=====')
            print()
            print('1.Выйти из программы')
            print('2.Запустить сортировку списка студентов')
            my_answer = int(input('Введите 1 или 2: '))
            if my_answer == 1:
                print('Программа заверщена')
                break
            elif my_answer == 2:
                sort_group = sorted(creat_student_manual(),key=lambda x: x.calculatr())
                print('=========Список студентов, отсортированный по среднему баллу (по возрастанию):==========')
                for i, text in enumerate(sort_group,1):
                    print(f'{i}.{text.print_result()}')

            else:
                raise ValueError('вводите 2 или 3')
        except ValueError as e:
            print(f'Возникла ошибка: {e}')

main()





# Реализуйте модель с именем Student, содержащую поля «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
# Затем создайте список из десяти студентов (данные о студентах можете придумать или запросить у пользователя)
# и отсортируйте список по возрастанию среднего балла. Выведите результат на экран.