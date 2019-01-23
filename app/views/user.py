"""routes for User"""
from flask import Flask, jsonify, request, Blueprint, make_response
from app.models.user import User
from db import DataBaseConnection
from werkzeug.security import generate_password_hash, check_password_hash
import jwt  # pip install pyjwt
import datetime
from functools import wraps


user = User()
bp2 = Blueprint('users', __name__, url_prefix='/api/v1')


@bp2.route('/registration', methods=['POST'])
def user_registration():
    '''Function registering a user'''
    data = request.get_json()  # Converting to json
    # hashed_password = generate_password_hash(data['password'])
    if not data:
        response = {
            'status': 400
        }
        return jsonify(response), 400
    postedData = ['name', 'email', 'phoneNumber', 'username', 'password']
    if not all(item in data for item in postedData):
        response = {
            'message': 'Missing parameter(s)',
            'status': 400
        }
        return jsonify(response), 400
    name = data['name']
    email = data['email']
    phoneNumber = data['phoneNumber']
    username = data['username']
    password = data['password']
    user.register_user(name, email, phoneNumber, username, password)

    response = {
            'status': 201,
            'message': 'Successfully posted',
    }
    return jsonify(response), 201


@bp2.route('/login', methods=['POST'])
def login():
    """Function to log in user"""
    data = request.get_json()
    username = data['username']
    password = data['password']
    # auth = request.authorization
    # if not auth or not auth.username or not auth.password:
    #     return jsonify({'message': 'Log in required'})

    user_in_db = user.login_user(username)
    if user_in_db is None:
        return jsonify({'message': 'Username or Password does not exist'})
    # return jsonify({'message': user_in_db['password']})

    if user_in_db['password'] == password:
        exp_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        token = jwt.encode(
            {
                'username': user_in_db['username'],
                'exp': exp_time,              
            }, "beingworkedon"
        )
        response = {
            'token': token.decode('UTF-8'),
            'status': 200,  # Because its python 3, token is returned in byte so we decode it to string using this 
            'message': 'Successfully logged in'
        }
        return jsonify(response), 200
    return jsonify({'message': 'Wrong Password'}), 400


# def token_required(f):
#     """Function to protect multiple routes"""
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.args.get('token')  # Getting token out of the querry string
#         if not token:
#             return jsonify({'message': 'Token is missing'}), 403
#         try:
#             data = jwt.decode(token, app.config['SECRET_KEY'])
#         except:
#             return jsonify(['message': 'Token is invalid']), 403
#         return f9*args, **kwargs)

#     return decorated