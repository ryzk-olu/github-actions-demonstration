import pytest
import sys
import os
from flask import Flask
from flask.testing import FlaskClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == "Hello, World!"

def test_hello(client):
    name = 'Alice'
    response = client.get(f'/hello/{name}')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == f"Hello, {name}!"

def test_get_data(client):
    response = client.get('/api/data')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['name'] == "My Simple Flask"
    assert json_data['status'] == "OK"
    assert json_data['version'] == "1.0"

