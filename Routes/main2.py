from flask import Flask, jsonify, request
from Models.usermodel import User
import datetime

register=[]

app = Flask(__name__)

@app.route('/api/v1/registration', methods=['POST'])
def user_registration():
    '''Registration of User using Post'''
    '''Convert Input Data to json'''
    data = request.get_json()
    if not data:
        response ={
            'status' : 400
        }
        return jsonify(response), 400
    postedData = ['id', 'name', 'email', 'username', 'password', 'isAdmin']
    if not all(item in data for item in postedData):
        response = {
            'message': 'Missing parameter(s)',
            'status' : 400
        }
        return jsonify(response), 400
    person = User(data['id'], data['name'], data['email'], data['username'], data['password'], data['isAdmin'])
    register.append(person)
    response = {
            'status' : 201,
            'message': 'Successfully posted',
            'data': person.__dict__
        }
    return jsonify(response), 201
