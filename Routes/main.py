from flask import Flask, jsonify, request


from Models.models import Incident
import random
import datetime

incidents=[]


app = Flask(__name__)

@app.route('/api/v1/red-flags', methods=['GET'])
def all_redflags():
    '''Convert each flag in incidents list to json'''

    allflags = [flag.to_json() for flag in incidents]
    response ={
        'status':200,
        'data': allflags
    }
    if len(allflags) < 1:
        return jsonify({'message': 'No incidents yet'}), 400
    return jsonify(response)


@app.route('/api/v1/red-flags', methods=['POST'])
def save_redflag():
    '''Convert input data to json'''

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


@app.route('/api/v1/red-flags/<red_flag_id>', methods=['GET'])
def spec_redflag(red_flag_id):
    '''Specific Get'''

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


@app.route('/api/v1/red-flags/<red_flag_id>', methods=['DELETE'])
def del_redflag(red_flag_id):
    '''Delete''' 

    if red_flag_id == '' or red_flag_id==None:
        response ={
            'message':'No data sent',
                    }
        return jsonify(response), 400
    if len(incidents) == 0:
        response={
            'message':'List is empty'
        }
        return jsonify(response), 500
    flag_id = int(red_flag_id)
    incidents.pop(int(flag_id))
    response = {
            'message':'Flag has successfully been deleted',
            'status' : 200
            }
    return jsonify(response), 200

 
@app.route('/api/v1/red-flags/<red_flag_id>', methods=['PATCH'])
def edit_redflag (red_flag_id):
    '''Edit Red-Flag'''

    flag_id = red_flag_id
    if flag_id=='' or flag_id == None:
        response ={
            'message':'No flag id chosen',
                    }
        return jsonify(response), 400
    
    flagToEdit = incidents[int(flag_id)]
    infoToAdd = request.get_json()
    if not infoToAdd:
        response = {
            'message':'No data sent'
        }
        return jsonify(response), 400
    
    requestvalues = ['id', 'createdOn', 'createdBy', 'type', 'location', 'status', 'Images', 'Videos', 'comment']

    flagToEditDict = flagToEdit.to_json()
    for field in requestvalues:
        flagToEditDict[field] = infoToAdd[field]

    edit = Incident(flagToEditDict['id'], flagToEditDict['createdOn'], flagToEditDict['createdBy'], flagToEditDict['type'], flagToEditDict['location'], flagToEditDict['status'], flagToEditDict['Images'], flagToEditDict['Videos'], flagToEditDict['comment'])
    incidents[int(flag_id)]= edit
    response= {
        'message' : 'successfully edited',
        'status' : '201'
    }
    return jsonify(response), 201
    
        



