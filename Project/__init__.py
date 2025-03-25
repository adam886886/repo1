import os
from flask import Flask, render_template
from . import db
from .auth import bp as auth_bp
from .events import bp as events_bp
from .risk_summary import bp as risk_summary_bp
from .timeline import bp as timeline_bp
from .ai import bp as ai_bp

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'project.sqlite'),
    )
    if test_config:
        app.config.update(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    db.init_app(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(risk_summary_bp)
    app.register_blueprint(timeline_bp)
    app.register_blueprint(ai_bp)
    @app.route('/')
    def index():
        return render_template('index.html')
    return app
