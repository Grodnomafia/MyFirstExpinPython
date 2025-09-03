def calculatios(oneprice,oneyears):
    return round((oneprice * oneyears) / 100, 2 )

price = [1.09, 23.56, 57.84, 4.56, 6.78]
one_years = int(input('Повышения на первый год : '))
two_years = int(input('Повышения на второй год: '))


new_one  = [calculatios(x,one_years) + x for x in price]
new_two = [calculatios(x,two_years) + x for x in new_one]
print(f'Сумма цен за каждый год: {sum(price)} ,{sum(new_one)} ,{sum(new_two)} ')


