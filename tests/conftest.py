import pytest
from app import create_app, db as _db
from app.models import User, Book

@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.app_context():
        _db.create_all()
        
        # Create test users
        roles = ['admin', 'librarian', 'reader', 'analyst', 'guest']
        for role in roles:
            user = User(username=f'test_{role}', role=role)
            user.password = 'password'
            _db.session.add(user)
        
        # Test books
        book = Book(title='Test Book', author='Test Author', year=2023)
        _db.session.add(book)
        _db.session.commit()
        
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def db(app):
    with app.app_context():
        _db.create_all()
        yield _db
        _db.session.remove()
        _db.drop_all()

@pytest.fixture
def auth_client(client, db):
    # Authenticate as admin
    client.post('/auth/login', data={
        'username': 'test_admin',
        'password': 'password'
    })
    return client