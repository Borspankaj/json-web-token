from flask import Blueprint , request , jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


routes_blueprint = Blueprint('routes' , __name__ )


@routes_blueprint.route('/')
def index():
    return "running"

@routes_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Missing username or password'}), 400

    username = data['username']
    password = data['password']

    if username == 'admin' and password == 'admin':
        
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'error': 'Invalid username or password'}), 401