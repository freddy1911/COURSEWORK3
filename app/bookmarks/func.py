from app.utils import open_json_read, add_post_json, del_post_json


def ad_bookmark(pk):
    """ Добавление в закладки """
    file = 'data/posts.json'
    data = open_json_read(file)
    for post in data:
        if pk == post["pk"]:
            posts = post
            json_file = 'data/bookmarks.json'
            add_post_json(json_file, posts)


def del_bookmarks(pk):
    """ Удаление из закладок """
    file = 'data/bookmarks.json'
    data = open_json_read(file)
    for post in data:
        if pk == post["pk"]:
            posts = post
            json_file = 'data/bookmarks.json'
            del_post_json(json_file, posts)


def all_bookmarks():
    """ Вывод списка закладок """
    file = 'data/bookmarks.json'
    data = open_json_read(file)
    posts = []
    for post in data:
        posts.append(post)
    return posts
