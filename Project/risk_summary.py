from flask import Blueprint, render_template
from .db import get_db

bp = Blueprint('risk_summary', __name__, url_prefix='/risksummary')

@bp.route('/')
def index():
    return render_template('risk_summary/index.html',active_page='risk_summary')