class Famaly:
    Famaly_name = 'Davidov'
    Famaly_money = 1000000
    famaly_house = False

    def information(self):

        print('**'*50)
        print('**'*7,'Фамилия семьи:',self.Famaly_name,'**'*7)
        print(f'{'**'*7}Бюджет семьи:{self.Famaly_money}{'**'*7}')
        print(f'{'**'*7}Наличия дома {'есть' if self.famaly_house else 'нету'}{'**'*7}')

    def get_money(self,money):
        print(f'Получена зарплата {money}')
        self.Famaly_money += money
        print(f'Текуший баланс денег {self.Famaly_money}')

    def buy_house(self,house_price, discount = 0):
        print(f'Цена дома {house_price}')
        house_price -= house_price * discount / 100
        print(f'Цена со скидкой {house_price}')
        if house_price <= self.Famaly_money:
            self.Famaly_money -= house_price
            self.famaly_house = True




my_famal = Famaly()
my_famal.information()
my_famal.buy_house(house_price=1005000, discount=2)
my_famal.information()




