def test_create_book(auth_client):
    response = auth_client.post('/books/create', data={
        'title': 'New Book',
        'author': 'New Author',
        'year': 2023
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'New Book' in response.data

def test_role_access(client, db):
    # Attempt to create book as reader
    client.post('/auth/login', data={
        'username': 'test_reader',
        'password': 'password'
    })
    response = client.get('/books/create')
    assert response.status_code == 403