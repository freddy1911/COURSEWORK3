import pytest

from app.posts.posts_dao import PostDAO


# Создаём фикстуру для класса
@pytest.fixture()
def posts_dao():
    posts_dao = PostDAO()
    return posts_dao


class TestPost:
    def test_all_posts(self, posts_dao):
        """ Тестируем все посты """
        all_posts = posts_dao.all_posts()
        assert type(all_posts) == list, "Ошибка выдачи формата"
        assert len(all_posts) > 0, "Пустой список"

    def test_get_post_by_pk(self, posts_dao):
        """ Тестируем отдельный пост """
        post = posts_dao.get_post_by_pk(1)
        assert post["poster_name"] == 'leo', "Ошибка выдачи"
