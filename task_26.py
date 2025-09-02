def main():
    n = int(input('Количество человек в списке: '))
    k = int(input('Какое число в считалке? '))

    people = list(range(1 , n + 1))
    people_index = 0

    while len(people) > 1:
        print(f'Текуший круг людей {people}')
        print(f'Начала счета с номера {people[people_index]}')
        people_index = (people_index + k - 1) % len(people)
        removed_people = people.pop(people_index)
        print(f'Выбывает человек под номером {removed_people}')
        if people_index >= len(people):
            people_index = 0
    print(f'Остается человек под номером {people[0]}')







if __name__ == '__main__':
    main()