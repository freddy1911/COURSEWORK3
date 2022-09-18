from flask import render_template, Blueprint, request

from app.logs.logs import my_logger
from app.posts.comments_dao import CommentsDAO
from app.posts.posts_dao import PostDAO

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
upload_posts = PostDAO()
comments_dao = CommentsDAO()
""" Подключение логированния"""
logger_posts = my_logger('posts', 'logs/posts.log')


@posts_blueprint.route('/')
def index_page():
    """ Главная страница"""
    logger_posts.info("Main page start")
    posts = upload_posts.all_posts()
    len_bookmarks = upload_posts.len_bookmarks()
    return render_template('index.html', posts=posts, bookmarks_num=len_bookmarks)


@posts_blueprint.route('/authors/<poster_name>')
def get_posts_by_user(poster_name):
    """ Вывод ленты пользователя"""
    logger_posts.info("Post with name")
    try:
        posts = upload_posts.get_posts_by_user(poster_name)
        return render_template('user-feed.html', posts=posts, title=poster_name)
    except:
        return render_template('404.html')


@posts_blueprint.route('/search')
def search():
    """ Вывод поиска"""
    logger_posts.info("Search start")
    query = request.args.get('s').lower()
    found_posts = upload_posts.search_for_posts(query)
    if len(found_posts) > 0:
        return render_template('search.html', posts=found_posts[0:10], title=query, len=len(found_posts))
    else:
        return render_template('search_not_found.html', title=query)


@posts_blueprint.route('/posts/<int:pk>')
def get_post_by_pk(pk):
    """ вывод отдельного поста"""
    logger_posts.info("Posts with PK")
    post = upload_posts.get_post_by_pk(pk)
    comments = comments_dao.get_comments_by_post_id(pk)
    return render_template('post.html', name=post["poster_name"], ava=post["poster_avatar"], pic=post["pic"],
                           content=post["content"], comments=comments, comm_len=len(comments), pk=post["pk"])


@posts_blueprint.route('/tag/<tagname>')
def hashtags(tagname):
    """ вывод по хештегам """
    hash_posts = upload_posts.hashtag_posts(tagname)
    return render_template('tag.html', posts=hash_posts, title=tagname)
