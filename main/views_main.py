from flask import Blueprint, Flask, render_template


main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route("/")
def page_index():
    """
    Страница поиска постов
    """
    return render_template('index.html')
