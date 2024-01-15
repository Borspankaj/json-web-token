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

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    
    else:
        return jsonify({'error': 'Invalid username or password'}), 401


@routes_blueprint.route('/login') 
@jwt_required()
def protected():
    current_user = "Retrieved from JWT claims: {}".format(get_jwt_identity())
    return jsonify(logged_in_as=current_user), 200
