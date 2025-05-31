def test_login(client):
    response = client.post('/auth/login', data={
        'username': 'test_admin',
        'password': 'password'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'You have been logged in' in response.data

def test_unauthorized_access(client):
    response = client.get('/books/create')
    assert response.status_code == 302  # Redirect to login