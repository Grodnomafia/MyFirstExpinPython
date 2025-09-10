def main():
    new = []
    count = 0

    for i in range(3):
        my_text = input('Введите слова: ').strip().lower()
        new.append(my_text)

    text = input('Введите текст: ').lower().split()
    print(text)
    for search_word in new:
        word_count = text.count(search_word)
        count += word_count
        print(f"Слово '{search_word}': {word_count} раз(а)")


    print(f'общее вхождения {count}')





main()