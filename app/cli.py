import click
from flask.cli import with_appcontext
from .models import db, User
from .config import Config

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Initialize the database"""
    db.create_all()
    
    # Create initial users
    for user_data in Config.INITIAL_USERS:
        user = User.query.filter_by(username=user_data['username']).first()
        if not user:
            user = User(username=user_data['username'], role=user_data['role'])
            user.password = user_data['password']
            db.session.add(user)
    
    db.session.commit()
    click.echo('Database initialized')

def register_commands(app):
    app.cli.add_command(init_db_command)