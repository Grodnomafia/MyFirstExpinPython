def main():
    quantity = int(input('Количество роликов: '))
    size_rolik = []
    for i_size in range(quantity):
        size = int(input('Размеры пары: '))
        size_rolik.append(size)

    people = int(input('Количество людей: '))
    size_people = []
    for i_rolik in range(people):
        rolik = int(input('Размер ноги человека: '))
        size_people.append(rolik)


    size_rolik.sort()
    size_people.sort()

    people_index = 0
    rolik_index = 0
    count = 0

    while rolik_index < len(size_rolik) and people_index < len(size_people):
        if size_rolik[rolik_index] == size_people[people_index]:
            count += 1
            people_index += 1
            rolik_index += 1
        elif size_rolik[rolik_index] < size_people[people_index]:
            rolik_index += 1
        else :
            people_index += 1

    print(f'Наибольшее количество людей, которые могут взять ролики: {count}')

if __name__ == '__main__':
    main()
