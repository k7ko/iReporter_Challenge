from flask import Flask, jsonify, request

from models import User
from models import Incident
import random
import datetime

incidents=[]

app = Flask(__name__)

#Get
@app.route('/api/v1/red-flags', methods=['GET'])
def all_redflags():
#convert each flag in incidents list to json

    allflags = [flag.to_json() for flag in incidents]
    response ={
        'status':200,
        'data': allflags
    }
    if len(allflags) < 1:
        return jsonify({'message': 'No incidents yet'}), 400
    return jsonify(response)


#Post
@app.route('/api/v1/red-flags', methods=['POST'])
def save_redflag():
#convert input data to json
    data = request.get_json()
    print(data)
    if not data:
        response ={
            'status': 400,
                    }
        return jsonify(response), 400

    postedData = ['id', 'createdOn', 'createdBy', 'type', 'location', 'status', 'Images', 'Videos', 'comment']
    if not all(item in data for item in postedData):
        response = {
            'message': 'Missing parameter(s)',
            'status' : 400
        }
        return jsonify(response), 400

    incident = Incident(data['id'], data['createdOn'], data['createdBy'], data['type'], data['location'], data['status'], data['Images'], data['Videos'], data['comment'])
    incidents.append(incident)
    response = {
            'status' : 201,
            'message': 'Successfully posted',
            'data': incident.__dict__
        }
    return jsonify(response), 201

#specific Get
@app.route('/api/v1/red-flags/<red_flag_id>', methods=['GET'])
def spec_redflag(red_flag_id):
    flag_id = red_flag_id
    flag = int(flag_id)

    oneFlag = incidents[flag]
    oneFlagConv = oneFlag.to_json()
    response ={
        'status' : 200,
        'message':'Successful',
        'data': oneFlagConv
    }
    return jsonify(response)
    
        


if __name__=='__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
