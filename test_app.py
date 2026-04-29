from app import app

def test_hello():
    # We use Flask's test_client to simulate a request without running the server
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b"Hello, CI/CD World!"  