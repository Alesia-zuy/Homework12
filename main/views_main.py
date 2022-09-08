from flask import Blueprint, Flask, render_template, request
from functions import get_posts_by_word
from json import JSONDecodeError

POST_PATH = "posts.json"

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='template')


@main_blueprint.route("/")
def page_index():
    """
    Страница поиска постов
    """
    return render_template('index.html')


@main_blueprint.route("/search/")
def page_search():
    s = request.args.get('s')
    try:
        posts = get_posts_by_word(s)
    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'
    return render_template('post_list.html', s=s)
