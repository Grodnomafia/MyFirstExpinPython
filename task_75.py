class Ship:

    def __init__(self,model):
        self.__model = model


    def __str__(self):
        return f'Модель коробля {self.__model}'

    def swip_ship(self):
        print(f'{self.__model} плывет по воде')

    def get_name(self):
        return f'{self.__model}'


class Cargo_ship(Ship):
    def __init__(self,model):
        super().__init__(model)
        self.workload = 0

    def workload_on(self,up):
        self.workload += up
        print(f'Корабл {self.get_name()} загрузился и составляет {self.workload} тонн')

    def workload_off(self,off):
        if self.workload > 0:
            self.workload -= off
        else :
            print('Корабл и так разгружен')

class Warship(Ship):
    def __init__(self,model,gun):
        super().__init__(model)
        self.gun = gun

    def fire(self):
        print(f'{self.get_name()} выстрелил из {self.gun}')


shipwar = Warship('avrora', 'Кинжал')
cargship = Cargo_ship('Грузовик')
print(cargship)
print(shipwar)
cargship.swip_ship()
cargship.workload_on(1)
shipwar.fire()