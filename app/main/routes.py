from flask import render_template
from flask_login import current_user
from . import main_bp

@main_bp.route('/')
def index():
    return render_template('index.html')