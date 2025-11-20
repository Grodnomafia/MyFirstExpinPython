

class Potate:
    states_potate = {0 : 'росток', 1 : 'маленькая', 2 : ' средняя ', 3 : 'большая'}

    def __init__(self, index):
         self.potate_index = index
         self.state  = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print(f'Картошка {self.potate_index} сейчас {Potate.states_potate[self.state]}')
    def is_ripe(self):
        return self.state == 3

class GardenPotate:

    def __init__(self,count):
        self.potatos = [Potate(index= i) for i in range(1, count + 1)]

    def grow_all(self):
        print('Картошка  проростает!')
        for i_patate in self.potatos:
            i_patate.grow()

    def are_all_ripe(self):
        if not all([i_patate.is_ripe() for i_patate in self.potatos]):
            print('Картошка еше не созрела\n')

        else :
            print('Вся картошка созрела , можно собирать\n')


my_garden = GardenPotate(5)
my_garden.are_all_ripe()
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()
