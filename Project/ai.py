from flask import Blueprint, render_template
from .db import get_db

bp = Blueprint('ai', __name__, url_prefix='/ai')

@bp.route('/')
def index():
    return render_template('ai/index.html', active_page='ai')