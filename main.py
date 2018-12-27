from flask import Flask, jsonify, request

from models import User
from models import Incident
import random
import datetime

incidents=[]

app = Flask(__name__)

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

     


if __name__=='__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
