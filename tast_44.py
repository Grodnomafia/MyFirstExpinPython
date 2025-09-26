def great_list(sound, list_sound):
    return  list_sound.get(sound, 0)




def main():
    violator_songs = {
        'World in My Eyes': 4.86,
        'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56,
        'Halo': 4.9,
        'Waiting for the Night': 6.07,
        'Enjoy the Silence': 4.20,
        'Policy of Truth': 4.76,
        'Blue Dress': 4.29,
        'Clean': 5.83
    }
    box_save = 'первый', 'второй' , 'третий','четвёртый','пятый','шестой','седьмой','восьмой','девятый'
    how_music = int(input('Сколько песен выбрать? '))
    if 0 > how_music or how_music > len(violator_songs):
        print(f"Пожалуйста, введите число от 1 до {len(violator_songs)}")
        return
    total_time = 0
    for i in range(how_music):
        music = input(f'Введите названия {box_save[i]} песени: ')
        total = great_list(music.title(), violator_songs)
        if total == 0:
            print('Песня не найдена в списке')
        else :
            total_time += total
    print(f'⏱️ Общее время звучания: {total_time:.2f} минуты')


main()