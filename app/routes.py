from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify(message="Hello, World!")

@main.route('/hello/<name>')
def hello(name):
    return jsonify(message=f"Hello, {name}!")

@main.route('/api/data')
def get_data():
    data = {
        'name': 'My Simple Flask',
        'status': 'OK',
        'version': '1.0'
    }
    return jsonify(data)
