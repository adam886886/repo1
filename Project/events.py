from flask import Blueprint, render_template
from .db import get_db

bp = Blueprint('events', __name__, url_prefix='/events')

@bp.route('/')
def index():
    return render_template('events/index.html')

@bp.route('/geopolitics')
def geopolitics():
    db = get_db()
    events = db.execute('SELECT * FROM calendar_events').fetchall()
    return render_template('events/geopolitics.html', events=events)

@bp.route('/macro')
def macro():
    db = get_db()
    macro_data = db.execute('SELECT * FROM macrodata').fetchall()
    return render_template('events/macro.html', macro_data=macro_data)

@bp.route('/recap')
def recap():
    db = get_db()
    recap_data = db.execute('SELECT * FROM recapdata').fetchall()
    return render_template('events/recap.html', recap_data=recap_data)
