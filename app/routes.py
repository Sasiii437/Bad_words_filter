from flask import Blueprint, render_template, request
from .utils import clean_sentence

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    sanitized_sentence = None
    original_sentence = None
    if request.method == 'POST':
        original_sentence = request.form.get('sentence')
        sanitized_sentence = clean_sentence(original_sentence)
    return render_template('index.html', original_sentence=original_sentence, sanitized_sentence=sanitized_sentence)
