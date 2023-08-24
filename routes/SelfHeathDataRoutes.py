import json

from flask import Blueprint, request, jsonify

from apiproject.service import SelfHeathDataService

selfHeathData = Blueprint("selfHeathData", __name__, template_folder='routes')

@selfHeathData.route('/selfHeathData')
def selfHeathDatas():
    '''
    file: swagger/selfHealthData.yml
    '''
    return SelfHeathDataService.read_all()

@selfHeathData.route('/selfHeathData/add', methods=["POST"])
def saveNewData():
    data =json.loads(request.get_data())
    if type(data) == dict:
        msg = SelfHeathDataService.add_record(data)
    elif type(data) == list:
        msg = SelfHeathDataService.add_records(data)
    else:
        msg = {"message" : "* input data error."}
    return msg, 200

@selfHeathData.route('/selfHeathData/del/<self_health_id>', methods=["DELETE"])
def deleteOne(self_health_id):
    return SelfHeathDataService.delete_by_id(self_health_id), 200

@selfHeathData.route('/selfHeathData/update', methods=["PATCH"])
def updateOneRecord():
    data = json.loads(request.get_data())
    msg = SelfHeathDataService.update_record(data)
    return msg, 200

