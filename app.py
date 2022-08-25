import logging

from flask import Flask, request, render_template, send_from_directory

# blueprints import
from main.views_main import main_blueprint
from loader.wievs_loader import loader_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

logging.basicConfig(filename='basic.log', level=logging.INFO)


@app.route("/uploads/<path:path>")
def static_dir(path):
    path = '/' + path
    return send_from_directory('uploads', path)


app.run()

