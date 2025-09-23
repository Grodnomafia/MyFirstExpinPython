players_dict = {
1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

print(f'Все члены команды А,которые отдыхают: {', '.join([i['name'] for i in players_dict.values() if i['team'] == 'A' and i['status'] == 'Rest'])}')
print(f'Все члены команды Б, которые тренеруются: {', '.join([i['name'] for i in players_dict.values() if i['team'] == 'B' and i['status'] == 'Training'])}')
print(f'Все члены команды С,которые путеществуют: {', '.join([i['name'] for i in players_dict.values() if i['team'] == 'C' and i['status'] == 'Travel'])}')





# 1.	Все члены команды А, которые отдыхают.
# 2.	Все члены команды B, которые тренируются.
# 3.	Все члены команды C, которые путешествуют.

