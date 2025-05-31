from models import db, Book

def init_db():
    db.create_all()
    
    # Добавляем тестовые данные
    if not Book.query.first():
        books = [
            Book(title='Война и мир', author='Лев Толстой', year=1869),
            Book(title='Преступление и наказание', author='Федор Достоевский', year=1866),
            Book(title='1984', author='Джордж Оруэлл', year=1949)
        ]
        db.session.add_all(books)
        db.session.commit()