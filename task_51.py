def search_key(text_list , search):
    if search in text_list:
        return text_list[search]
    for i in text_list.values():
        if isinstance(i, dict):
            new_search = search_key(i, search)
            if new_search :
                break
    else:
        new_search = None
    return new_search


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


find_key = input('Искомый ключ: ')
key = search_key(site, find_key)
if key:
    print(key)
else:
    print('Ключ не найден')