from flask import Blueprint, render_template
from .db import get_db

bp = Blueprint('timeline', __name__, url_prefix='/timeline')

@bp.route('/')
def index():
    return render_template('timeline/index.html',active_page='timeline')