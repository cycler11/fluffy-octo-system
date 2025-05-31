from flask import Flask, render_template, request, redirect, url_for
from models import db, Book
from database import init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data/library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация базы данных
db.init_app(app)
with app.app_context():
    init_db()

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        
        new_book = Book(title=title, author=author, year=year)
        db.session.add(new_book)
        db.session.commit()
        
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    book = Book.query.get_or_404(id)
    
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.year = request.form['year']
        
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('edit.html', book=book)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    book = Book.query.get_or_404(id)
    
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('delete.html', book=book)

@app.route('/detail/<int:id>')
def detail(id):
    book = Book.query.get_or_404(id)
    return render_template('detail.html', book=book)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)