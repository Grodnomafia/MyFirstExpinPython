import json


def check_edit(old, new, diff_list):
    try:
        with open(old, 'r', encoding='utf-8') as f:
            old_doc = json.load(f)
        with open(new, 'r', encoding='utf-8') as f:
            new_doc = json.load(f)
    except Exception as x:
        print(x)
    result = {}

    old_file = old_doc.get('data', {})
    new_file = new_doc.get('data', {})
    for i in diff_list:
        if i in old_file and i in new_file:
            if old_file[i] != new_file[i]:
                result[i] = new_file[i]

    return result


def save_json(file, file_name='result_json.json'):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(file, f, indent=4, ensure_ascii=False)


def main():
    diff_list = ['services', 'staff', 'datetime']
    old = 'json_old.json'
    new = 'json_new.json'
    result = check_edit(old, new, diff_list)
    # Вывод результата
    print(result)

    # файл сохранен в файл json
    save_json(result)


if __name__ == '__main__':
    main()