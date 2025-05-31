from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object(Config)

# Явная установка URI базы данных
if 'DATABASE_URL' in app.config:
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE_URL']

db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = 'auth.login'

# Регистрация Blueprint'ов
from auth.routes import auth_bp
from books.routes import books_bp
from main.routes import main_bp

app.register_blueprint(auth_bp)
app.register_blueprint(books_bp)
app.register_blueprint(main_bp)

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

@app.errorhandler(403)
def forbidden_error(error):
    return render_template('errors/403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500

# Инициализация БД при запуске
with app.app_context():
    db.create_all()
    
    from models import User
    from config import Config
    
    # Создание начальных пользователей
    for user_data in Config.INITIAL_USERS:
        user = User.query.filter_by(username=user_data['username']).first()
        if not user:
            user = User(username=user_data['username'], role=user_data['role'])
            user.password = user_data['password']
            db.session.add(user)
    
    db.session.commit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
