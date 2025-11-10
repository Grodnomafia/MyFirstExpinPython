
def analysis():
    with open('text.txt', 'r') as file :
        text = file.read().lower()

    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    keeps_letters = {}
    for i in text:
        if i in english_letters:
            keeps_letters[i] = keeps_letters.get(i, 0) + 1
    total = sum(keeps_letters.values())
    if total == 0:
        with open('analysis.txt', 'w') as write_fail:
            write_fail.write('')
        return

    result_letters = {}
    for letters , counts  in keeps_letters.items():
        finish = counts / total
        result_letters[letters] = finish

    sorted_letters = sorted(result_letters.items(),key=lambda x:(-x[1], x[0]))
    with open('analysis.txt', 'w') as write_fail:
        for letts, nums in sorted_letters:
            write_fail.write(f'{letts} {nums:.3f}\n')





analysis()