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

def test_sentiment_analysis_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/sentimentAnalysis'
    response = client.get(url)
    assert response.status_code == 200


# def test_sentiment_post_req():
#     app = Flask(__name__)
#     configure_routes(app)
#     client = app.test_client()
#     response = client.post("/sentimentAnalysis", data={
#         "name": "neha Thipse",
#         "review": "Good food",        
#     })
#     assert response.status_code == 200


def test_helloada_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/hello/ada'
    response = client.get(url)
    assert response.status_code == 200  
    
 def test_helloanagha_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/hello/anagha'
    response = client.get(url)
    assert response.status_code == 200
