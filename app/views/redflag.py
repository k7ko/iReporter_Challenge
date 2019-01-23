"""Routes for RedFlags"""
from flask import Flask, jsonify, request, Blueprint
from app.models.redflag import Incident
import jwt
import datetime


bp = Blueprint("red-flags", __name__, url_prefix='/api/v1')
redflag = Interventions()

@bp.route('/red-flags', methods=['GET'])
def all_redflags():
    '''Function for getting all Red-Flags'''
    allflags = [flag.to_json() for flag in incidents]  # Convert each flag in incidents list to json
    if len(allflags) < 1:
        return jsonify({'message': 'No incidents yet'})
    response = {
        'status': 200,
        'data': allflags
    }
    
    return jsonify(response)


@bp.route('/red-flags', methods=['POST'])
def save_redflag():
    '''Convert input data to json'''

    data = request.get_json()
    if not data:
        response ={
            'status': 400,
                    }
        return jsonify(response), 400

    postedData = ['id', 'created_on', 'created_by', 'type', 'location', 'status', 'images', 'videos', 'comment']
    if not all(item in data for item in postedData):
        response = {
            'message': 'Missing parameter(s)',
            'status' : 400
        }
        return jsonify(response), 400

    incident = Incident(data['id'], data['created_on'], data['created_by'], data['type'], data['location'], data['status'], data['images'], data['videos'], data['comment'])
    incidents.append(incident)
    response = {
            'status' : 201,
            'message': 'Successfully posted',
            'data': incident.__dict__
        }
    return jsonify(response), 201


@bp.route('/red-flags/<red_flag_id>', methods=['GET'])
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


@bp.route('/red-flags/<red_flag_id>', methods=['DELETE'])
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

 
@bp.route('/red-flags/<red_flag_id>', methods=['PATCH'])
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
    
    requestvalues = ['id', 'created_on', 'created_by', 'type', 'location', 'status', 'images', 'videos', 'comment']

    flagToEditDict = flagToEdit.to_json()
    for field in requestvalues:
        flagToEditDict[field] = infoToAdd[field]

    edit = Incident(flagToEditDict['id'], flagToEditDict['created_on'], flagToEditDict['created_by'], flagToEditDict['type'], flagToEditDict['location'], flagToEditDict['status'], flagToEditDict['images'], flagToEditDict['videos'], flagToEditDict['comment'])
    incidents[int(flag_id)]= edit
    response= {
        'message' : 'successfully edited',
        'status' : '201'
    }
    return jsonify(response), 201
    
        



