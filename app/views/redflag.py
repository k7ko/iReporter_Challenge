"""Routes for RedFlags"""
from flask import Flask, jsonify, request, Blueprint
from app.models.redflag import Incident
import jwt
import datetime


bp = Blueprint("red-flags", __name__, url_prefix='/api/v1')
redflag = Incident()


@bp.route('/red-flags', methods=['GET'])
def all_redflags():
    '''Function for getting all Red-Flags'''
    data = redflag.get_all_redflag()
    if data is None:
        return jsonify({'message': 'No incidents yet'})
    response = {
        'status': 200,
        'data': data
    }  
    return jsonify(response)


@bp.route('/red-flags', methods=['POST'])
def save_redflag():
    '''Function for creating a red flag'''
    data = request.get_json()
    redflagType = data['redflagtype']
    location = data['location']
    status = data['status']
    images = data['images']
    videos = data['videos']
    comment = data['comment']
    info = redflag.create_redflag(
        redflagType,
        location,
        status,
        images,
        videos,
        comment
    )
    if not data:
        return jsonify({'message': 'No data input', 'status': 400}), 400

    # postedData = ['created_on', 'created_by', 'type', 'location', 'status', 'images', 'videos', 'comment']
    # if not all(item in data for item in postedData):
    #     response = {
    #         'message': 'Missing parameter(s)',
    #         'status' : 400
    #     }
    #     return jsonify(response), 400

    # incident = redflag(data['id'], data['created_on'], data['created_by'], data['type'], data['location'], data['status'], data['images'], data['videos'], data['comment'])
    # incidents.append(incident)
    response = {
            'status': 201,
            'message': 'Successfully posted',
            'data': info
        }
    return jsonify(response), 201


@bp.route('/red-flags/<red_flag_id>', methods=['GET'])
def spec_redflag(red_flag_id):
    '''Function to get specific red flag'''

    redflagId = int(red_flag_id)
    record = redflag.get_one_redflag(redflagId)
    # oneFlagConv = oneFlag.to_json()
    if record is None:
        return jsonify({'status': 400, 'message': 'No data found'})
    response = {
        'status': 200,
        'message': 'Successful',
        'data': record
    }
    return jsonify(response)


@bp.route('/red-flags/<red_flag_id>', methods=['DELETE'])
def del_redflag(red_flag_id):
    '''Function to delete a red flag'''

    if red_flag_id == '' or red_flag_id is None:
        response = {
            'message': 'No data sent',
                    }
        return jsonify(response), 400
    # if len(incidents) == 0:
    #     response={
    #         'message':'List is empty'
    #     }
    #     return jsonify(response), 500
    redflagId = int(red_flag_id)
    redflag.delete_redflag(redflagId)
    response = {
            'message': 'Flag has successfully been deleted',
            'status': 200
            }
    return jsonify(response), 200


@bp.route('/red-flags/<red_flag_id>', methods=['PATCH'])
def edit_redflag(red_flag_id):
    '''Function to edit Red Flag'''

    if red_flag_id == '' or red_flag_id is None:
        response = {
            'message': 'No flag id chosen',
                    }
        return jsonify(response), 400

    new_location = request.get_json()

    if not new_location:
        response = {
            'message': 'No data sent'
        }
        return jsonify(response), 400

    flag_id = int(red_flag_id)
    location = new_location['location']
    update = redflag.update_redflag_location(flag_id, location)
    response = {
        'status': '201',
        'id': update['redflagid'],
        'message': 'successfully edited'
    }
    return jsonify(response), 201
