from abc import ABC,abstractmethod
from dataclasses import dataclass
@dataclass
class Jornal:
    jornal = {}
    def add_person(self,name,subject,grade):
        if name not in self.jornal:
            self.jornal[name] = {}
        if subject not in self.jornal[name]:
            self.jornal[name][subject] = []
        self.jornal[name][subject].append(grade)

    def mid_all(self,student):
        my_jornal = self.jornal.get(student,{})
        if not my_jornal:
            return 0
        all_grades = []
        for subject, grade  in my_jornal.items():
            all_grades.extend(grade)

        return sum(all_grades) / len(all_grades)
    def mid_subject(self,student,subject):
        my_subject = self.jornal.get(student,{}).get(subject,[])
        if not my_subject:
            return 0.0
        return sum(my_subject) / len(my_subject)





class Notifilter(ABC):
    @abstractmethod
    def send(self,student,message):...

class SmsNotifilter(Notifilter):
    def send(self,student,message):
        print(f'[SMS] {student} имеет {message}')

class EmailNotifilter(Notifilter):
    def send(self,student,message):
        print(f'[EMAIL] {student} имеет {message}')


@dataclass
class Monitoring:
    jornal_person : Jornal
    notifil_method : Notifilter
    normal_grade : float = 3.5
    added_list = set()

    def run(self,name):
        avg = self.jornal_person.mid_all(name)
        if avg < self.normal_grade and name not in self.added_list:
            self.notifil_method.send(name,f'{avg} это меньше чем {self.normal_grade}')

            self.added_list.add(name)
        return avg




x = Jornal()
x.add_person('artem','fisika',2)
x.add_person('artem','fisika',3)
x.add_person('artem','fisik',3)
result = Monitoring(x,EmailNotifilter())
result.run('artem')
print(x.mid_subject('artem','fisika'))
