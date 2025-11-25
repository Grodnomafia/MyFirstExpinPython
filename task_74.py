import random

class People:
    def __init__(self,name,home):
        self.name = name
        self.home = home
        self.satiety = 50



    def satiety_food(self,):
        print('Открываю холодильник и начинаю есть')
        if self.home.fridge_eat >= 20:
            self.satiety += 20
            self.home.fridge_eat -= 20
        else :
            print(f'Ошибка не хватает еды в холодильнике, Остаток : {self.home.fridge_eat}')

    def my_work(self):
        print('Я пошел на работу и заработал 20$')
        self.satiety -= 20
        self.home.table_money += 20



    def game(self):
        print('Я начинаю играть')
        self.satiety -= 10




    def shop_food(self):
        if self.home.table_money >= 20:
            print('Пришел в магазин покупать продукты')
            self.home.fridge_eat += 20
            self.home.table_money -= 20
            print(f'Осталась денег {self.home.table_money} , в холодильнике {self.home.fridge_eat}')
        else :
            print('Не хватает денег купить в магазине')

    def is_life(self):
        return self.satiety > 0

    def __str__(self):
        if not self.is_life():
            return (f'Человек {self.name} - умер его'
                    f'\nСытность : ниже 0 ')
        return (f'{self.name} Сытность :{self.satiety}\nДенег в тумбочке:{self.home.table_money}\n'
                f'В холодильнике едениц еды:{self.home.fridge_eat}')

    def every_dat(self):
        random_num = random.randint(1, 6)
        if not self.is_life():
            return
        if self.satiety < 20:
            self.satiety_food()
        elif self.home.fridge_eat < 20:
            self.shop_food()
        elif self.home.table_money < 50:
            self.my_work()
        elif random_num == 1:
            self.my_work()
        elif random_num == 2:
            self.satiety_food()
        else:
            self.game()








class Home:
    def __init__(self):
        self.fridge_eat = 50
        self.table_money = 0




house = Home()
artem1 = People('Артем',house)
anna = People('Анна', house)
for i in range(365):
    artem1.every_dat()
    anna.every_dat()
    if not artem1.is_life() and not anna.is_life():
        print('Оба умерли')
        break

print(artem1)
print(anna)

