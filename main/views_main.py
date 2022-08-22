import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request
from functions import get_posts_by_word

# Create an exemplar of class
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates_name')


# Create a view for /
@main_blueprint.route('/')
def main():
    return render_template('index.html')


# Create a view for search/
@main_blueprint.route('/search/')
def search_page():
    search_query = request.args.get('s', '')

    logging.info('Выполняется поиск')

    try:
        suitable_posts = get_posts_by_word(search_query)
    except FileNotFoundError:
        return 'Файл не найден!'
    except JSONDecodeError:
        return "Невалидный файл!"

    return render_template('post_list.html', query=search_query, posts=suitable_posts)
