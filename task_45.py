def count_text(txt):
    count_txt = dict()
    for i in txt:
        count_txt[i] = count_txt.get(i , 0) + 1
    return  count_txt


def histogramm(text):
    histo = dict()
    for simbol , count in text.items():
        if count not in histo:
            histo[count] = []
        histo[count].append(simbol)
    return histo




def main():
    text = input('Введите текст: ')
    new_text = count_text(text)
    histogram = histogramm(new_text)
    print('Инвертированный словарь частот:')
    for key, numb in sorted(histogram.items()):
        print(f'Количество {key} символов : {numb}')








main()





