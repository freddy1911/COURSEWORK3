
from app.posts.posts_class import Post
from app.utils import open_json_read


class PostDAO:

    def all_posts(self):
        """ Получение всех постов"""
        file = 'data/posts.json'
        data = open_json_read(file)
        posts = []
        for post in data:
            posts.append(Post(
                post["poster_name"],
                post["poster_avatar"],
                post["pic"],
                post["content"],
                post["views_count"],
                post["likes_count"],
                post["pk"]
            ))
        return posts

    def get_posts_by_user(self, name):
        """ Получение постов по пользователю"""
        file = 'data/posts.json'
        data = open_json_read(file)
        posts = []
        for post in data:
            if post["poster_name"] == name:
                posts.append(Post(
                    post["poster_name"],
                    post["poster_avatar"],
                    post["pic"],
                    post["content"],
                    post["views_count"],
                    post["likes_count"],
                    post["pk"]
                ))
        return posts

    def search_for_posts(self, word):
        """ Поиск по постам"""
        file = 'data/posts.json'
        data = open_json_read(file)
        found_posts = []
        for post in data:
            if word in post["content"].lower():
                found_posts.append(Post(
                    post["poster_name"],
                    post["poster_avatar"],
                    post["pic"],
                    post["content"],
                    post["views_count"],
                    post["likes_count"],
                    post["pk"]
                ))
        return found_posts

    def get_post_by_pk(self, pk):
        """ Вывод поста"""
        file = 'data/posts.json'
        data = open_json_read(file)
        for post in data:
            if pk == post["pk"]:
                posts = post
                hashtags = []
                for word in posts["content"].split():
                    if word[0] == "#":
                        hashtags.append(word)
                    if word in hashtags:
                        link = f'<a href="/tag/{word[1:]}">{word}</a>'
                        posts["content"] = posts["content"].replace(word, link, 1)
                return posts

    def hashtag_posts(self, tagname):
        """ Вывод по хэштегам """
        file = 'data/posts.json'
        data = open_json_read(file)
        hashtag_posts = []
        for post in data:
            if '#' + tagname in post["content"]:
                hashtag_posts.append(post)
        return hashtag_posts

    def len_bookmarks(self):
        """Вывод количество закладок"""
        return len(open_json_read('data/bookmarks.json'))