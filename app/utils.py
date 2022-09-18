import json
from json import JSONDecodeError


def open_json_read(my_file):
    """ Открываем файл json"""
    try:
        with open(my_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f'Файл {my_file} не найден')
    except JSONDecodeError:
        print('Невалидный файл')


def add_post_json(json_file, post):
    """ Добавляем в файл json"""
    posts = open_json_read(json_file)
    posts.append(post)
    try:
        with open(json_file, 'w', encoding="utf-8") as file:
            json.dump(posts, file, ensure_ascii=False)
        return posts
    except FileNotFoundError:
        print(f'Файл {json_file} не найден')
    except JSONDecodeError:
        print('Невалидный файл')


def del_post_json(json_file, post):
    """ Удаляем из файла json"""
    posts = open_json_read(json_file)
    posts.remove(post)
    try:
        with open(json_file, 'w', encoding="utf-8") as file:
            json.dump(posts, file, ensure_ascii=False)
        return posts
    except FileNotFoundError:
        print(f'Файл {json_file} не найден')
    except JSONDecodeError:
        print('Невалидный файл')