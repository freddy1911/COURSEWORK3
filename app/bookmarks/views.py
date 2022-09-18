from flask import Blueprint, redirect, render_template

from app.bookmarks.func import ad_bookmark, del_bookmarks, all_bookmarks

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')


@bookmarks_blueprint.route('/bookmarks/add/<int:pk>')
def add_bookmarks(pk):
    """ Вывод добавления в закладки """
    ad_bookmark(pk)
    return redirect("/", code=302)


@bookmarks_blueprint.route('/bookmarks/remove/<int:pk>')
def delate_bookmarks(pk):
    """ Вывод удаления из закладок"""
    del_bookmarks(pk)
    return redirect("/", code=302)


@bookmarks_blueprint.route('/bookmarks')
def index_bookmarks():
    """ Вывод страницы закладок"""
    posts = all_bookmarks()
    return render_template('bookmarks.html', posts=posts)
