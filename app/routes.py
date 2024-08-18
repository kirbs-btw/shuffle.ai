from flask import Blueprint, render_template
from .backend.DbHandler import DbHandler
from .backend.MilvusHandler import MilvusHandler

main = Blueprint('main', __name__)

DB_HANDLER = DbHandler()
MILVUS_HANDLER = MilvusHandler()


@main.route('/')
def index():
    return render_template('index.html')

@main.post('/word_search')
def get_songs_from_word_search():
    pass

@main.post('/')