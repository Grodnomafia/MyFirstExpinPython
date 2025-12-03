import character

class Monsters(character.Character):
    def __init__(self,name,health,damage):
        super().__init__(name,health,damage)

    def make_move(self,allies,enemies):
        alive_enemies = [e for e in enemies if e.alive]
        if not alive_enemies:
            return
        target = alive_enemies[0]
        self.attack(target)

class Goblins(Monsters):
    def __init__(self,name):
        super().__init__(name,100,25)

    def make_move(self, allies, enemies):
        print(f'{self.name} Рычит и готовится к атаке')
        super().make_move(allies,enemies)

class Ork(Monsters):
    def __init__(self,name):
        super().__init__(name,90,20)

    def make_move(self, allies, enemies):
        print(f'{self.name} точит свой Axe и готовится к атаке')
        super().make_move(allies, enemies)
