from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import db, Book

books_bp = Blueprint('books', __name__)

@books_bp.route('/')
@login_required
def index():
    books = Book.query.all()
    return render_template('books/index.html', books=books)

@books_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if current_user.role not in ['admin', 'librarian']:
        flash('У вас нет прав для этой операции', 'danger')
        return redirect(url_for('books.index'))
    
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = int(request.form['year'])
        
        book = Book(
            title=title,
            author=author,
            year=year,
            added_by=current_user.id
        )
        db.session.add(book)
        db.session.commit()
        flash('Книга успешно добавлена!', 'success')
        return redirect(url_for('books.index'))
    return render_template('books/create.html')

# Аналогичные функции для edit, delete, detail
