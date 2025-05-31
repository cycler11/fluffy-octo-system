from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from . import books_bp
from .forms import BookForm
from ..models import Book, db
from ..decorators import role_required

@books_bp.route('/')
@login_required
def index():
    books = Book.query.all()
    return render_template('books/index.html', books=books)

@books_bp.route('/create', methods=['GET', 'POST'])
@login_required
@role_required('create')
def create():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(
            title=form.title.data,
            author=form.author.data,
            year=form.year.data,
            added_by=current_user.id
        )
        db.session.add(book)
        db.session.commit()
        flash('Book added successfully!', 'success')
        return redirect(url_for('books.index'))
    return render_template('books/create.html', form=form)

# Similar routes for edit, delete, detail would be here