from dataclasses import dataclass
from typing import List, Optional
@dataclass
class Student:
    name : str
    grade : int
@dataclass
class StudentReposit:
    box_student : List[Student]

    def add_student(self,student:Student)->None:
        self.box_student.append(student)

    def get_info(self)->List[Student]:
        return self.box_student
@dataclass
class StatisStudent:
    repository:StudentReposit

    def get_all(self)->float:
        studentrepos = self.repository.get_info()
        if not studentrepos:
            return 0
        sum_grade = sum(i.grade  for i  in studentrepos)
        return sum_grade / len(studentrepos)
    def get_best_student(self)->Student:
        static = self.repository.get_info()
        return max(filter(lambda s: s.grade > 4,static),key=lambda x:x.grade)
@dataclass
class Report_Student:
    repository:StudentReposit
    statSeriver:StatisStudent
    def best_repost(self):
        print('Отчет по студентам')
        for i in self.repository.get_info():
            print('*'*20)
            print(f'Студент {i.name} : {i.grade}')
        print('*' * 20)
        print(f'Средний бал : {self.statSeriver.get_all()} ')
        print('*' * 20)
        _ = self.statSeriver.get_best_student()
        print(f'Лучший ученик : {_.name}')
        print('*' * 20)


# Создание класса для печати отчета:
# Генерация отчета с информацией о студенте, среднем балле и лучшем студенте.
# Вывод всех студентов и их оценок.
# Практическая реализация:
# Создание экземпляров каждого из классов.
# Добавление нескольких студентов в репозиторий.
# Печать отчета с помощью созданного метода.
test1,test2,test3 = Student('Артем',3),Student('Виктория',4),Student('Есения',5)

reposit = StudentReposit([test1,test2,test3])
static = StatisStudent(reposit)
report = Report_Student(reposit,static)
report.best_repost()






