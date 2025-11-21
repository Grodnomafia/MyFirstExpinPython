import random
class Warrior:

    def __init__(self,name):
        self.name = name
        self.health = 100

    def atack_mod(self,other):
        damage = 20
        other.health -= damage
        print(f'{self.name} нанес урон в размере {damage} по {other.name}!'
              f' У {other.name} осталась {other.health} HP')

    def health_is(self):
        return self.health > 0




voin1 = Warrior('Воин1')
voin2 = Warrior('Воин2')
print('====Начнется битва====')
print(f'===={voin1.name} = {voin1.health}hp ///// {voin2.name} = {voin2.health}====')
while all([voin1.health_is() , voin2.health_is()]):
    atack,deffend = random.choice([(voin1,voin2),(voin2,voin1)])
    if  deffend.health_is():
        atack.atack_mod(deffend)
if voin1.health_is():
    print(f'{voin1.name} победил')
else :
    print(f'{voin2.name} победил')







# Вы работаете в команде разработчиков мобильной игры, и вам досталась часть от ТЗ заказчика.
# Есть два юнита, каждый называется «Воин». Каждому устанавливается здоровье в 100 очков. Они бьют друг друга в случайном порядке.
# Тот, кто бьёт, здоровье не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника осталось здоровья.
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
