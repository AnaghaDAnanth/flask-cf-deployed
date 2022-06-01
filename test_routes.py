from flask import Flask
import json

from routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    # assert response.get_data() == b'Hello, World!'
    assert response.status_code == 200
