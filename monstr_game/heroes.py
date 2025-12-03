import character

class Hero(character.Character):

    def __init__(self,name,health,damage,role):
        super().__init__(name,health,damage)
        self.role = role

    def make_move(self, allies, enemies):
        alive_enemies = [e for e in enemies if e.alive]
        if not alive_enemies:
            return
        target = alive_enemies[0]
        self.attack(target)

class Tank(Hero):
    def __init__(self,name):
        super().__init__(name,120,30,'tank')

    def make_move(self, allies, enemies):
        print(f'{self.name} Одевает доспехи  и готовится к атаке')
        super().make_move(allies, enemies)

class Healer(Hero):
    def __init__(self,name):
        super().__init__(name,80,10,'Healer')

    def make_move(self, allies, enemies):
        print(f'{self.name} Готовит аптечки и готовится к атаке')
        super().make_move(allies, enemies)