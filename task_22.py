shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
        ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200],['седло', 2700]]
my_request = input('Введите названия детали: ')



def seach(request , shop_list):
        count_details = 0
        count_price = 0

        for i in shop_list:
                for i_new in i:
                        if i_new == request:
                                count_details += 1
                                count_price += i[1]

        return count_details, count_price



details , price = seach(my_request, shop)
print(f'Количество деталей {details}, Общая цена деталей {price}')
