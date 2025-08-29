violator_songs = [ ['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43], ['Personal Jesus', 4.56], ['Halo', 4.9],
['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20], ['Policy of Truth', 4.76], ['Blue Dress', 4.29], ['Clean', 5.83]]

music = int(input('Сколько песен выбрать? '))
my_playlist = []
time_sound = 0

def playlist_test(playlist,play_sound):
    for i in playlist:
        if i[0].capitalize() == play_sound:
            return i[1]
    return  False





for i in range(music):
    sound = input(f'Названия {i+1} песни: ').capitalize()
    if playlist_test(violator_songs, sound):
        my_playlist.append(sound)
        time_sound += playlist_test(violator_songs,sound)


    else :
        print('Нету песни в списки')

print(f'Ваш новый плейлист {my_playlist}')
print(f'Общее время звучания песен — {time_sound: .2f} минуты' )