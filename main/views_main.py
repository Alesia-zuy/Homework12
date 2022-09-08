from flask import Blueprint, render_template, request
from functions import get_posts_by_word

POST_PATH = "../posts.json"

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='template', static_folder='static')


@main_blueprint.route("/")
def page_index():
    """
    Страница поиска постов
    """
    return render_template('index.html')


@main_blueprint.route("/search/")
def page_search():
    s = request.args.get('s')
    posts = get_posts_by_word(s)
    return render_template('post_list.html', s=s, posts=posts)
