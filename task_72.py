class Parent:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.child = []

    def info_print(self):
        print('===Родитель===')
        print(f'Имя: {self.name} | Возраст: {self.age} лет')
        print(f'Наличие дитей: \n{self.child_life()}')
        if self.child:
            print(self.food_child())


    def food_child(self):
        if self.child:
            children_info = []
            for i in self.child:
                child_info = []
                if i.state:
                    child_info.append('Беспокойное')
                else:
                    child_info.append('Спокойное')
                if i.hungry:
                    child_info.append('Голодный')
                else:
                    child_info.append('Сытый')
                children_info.append(f'{i.name} cостояние: {','.join(child_info)}')
            return '\n'.join(children_info)



    def add_child(self,child):
        if child:
            if self.age - child.age < 16:
                print(f'Ребенку {child.name} не может быть {child.age}\n'
                      f'Должен быть меньше возраста родителя хотя бы на 16 лет')
            else:
                self.child.append(child)
                print(f'Родился ребенок {child.name}')


    def child_life(self):
        if not self.child:
            return  ('Детей нету')
        else:
            return '\n'.join([f'имя:{i.name} Возвраст:{i.age} лет' for i in self.child])

    def hungry(self,child_name):
        chilnd_hungry = self.search_name(child_name)
        if chilnd_hungry:
            print(f'{self.name} покормила {chilnd_hungry.name} ')
            return chilnd_hungry.hungry_edit()
        else:
            return print('Ребенок не найден')


    def state_relax(self,child_name):
        state_child  = self.search_name(child_name)
        if state_child:
            print(f'{self.name} успокоила {state_child.name} ')
            return  state_child.relax()
        else:
            return print('Ребенок не найден')

    def search_name(self,name):
        for i  in self.child:
            if i.name == name:
                return i
        return None


class Child:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.state = True # False - спокойное True- Беспокойное
        self.hungry = True # False - сытый True- голодный

    def hungry_edit(self):
        if self.hungry:
            self.hungry = False
        else:
            self.hungry = True

    def relax(self):
        if self.state:
            self.state = False
        else:
            self.state = True




papa = Parent('Артем', 35)
papa.info_print()
child1 = Child('Алеся', 13)
child2 = Child('Ильяс', 9)
child3 = Child('Митя', 20)
papa.add_child(child1)
papa.add_child(child2)
papa.add_child(child3)
papa.info_print()
papa.state_relax('Алеся')
papa.state_relax('Ильяс')
papa.info_print()
papa.hungry('Ильяс')
papa.hungry('Алеся')
papa.info_print()


# Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
# ● имя,
# ● возраст,
# ● список детей.
# И он может:
# ● сообщить информацию о себе,
# ● успокоить ребёнка,
# ● покормить ребёнка.
# У ребёнка есть:
# ● имя,
# ● возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
# ● состояние спокойствия,
# ● состояние голода.