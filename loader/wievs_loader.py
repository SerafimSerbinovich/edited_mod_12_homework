import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request, send_from_directory
from functions import add_post, save_picture

# Need to add templates
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates_name')


# Create view for new-post page
@loader_blueprint.route('/posts')
def post_page():
    return render_template('post_form.html')


# Create view for /post with POST method
@loader_blueprint.route('/posts', methods=['POST'])
def add_post_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Нет картинки или описания'
    if picture.filename.split('.')[-1] not in ['jpeg', 'png']:
        logging.error('Загруженный файл не картинка')
        return 'Неверный формат файла'
    try:
        picture_path = save_picture(picture)
    except FileNotFoundError:
        logging.info('Файл не найден')
        return "Файл не найден"
    except JSONDecodeError:
        return "Невалидный файл!"

    post = add_post({'pic': picture_path, 'content': content})

    return render_template('post_uploaded.html', post=post)


# open all downloaded files
@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory('uploads', path)



