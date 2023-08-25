import json
from flask import Blueprint, request

from apiproject.service import SelfHeathDataService

selfHeathData = Blueprint("selfHeathData", __name__, template_folder='routes')

@selfHeathData.route('/selfHeathData', methods=["GET"])
def selfHeathDatas():
    '''
    file: swagger/selfHealthData/selfHealthData.yml
    '''
    return SelfHeathDataService.read_all(), 200

@selfHeathData.route('/selfHeathData', methods=["POST"])
def saveNewData():
    '''
    file: swagger/selfHealthData/addSelfHealthData.yml
    '''
    data =json.loads(request.get_data())
    if type(data) == dict:
        msg = SelfHeathDataService.add_record(data)
    elif type(data) == list:
        msg = SelfHeathDataService.add_records(data)
    else:
        msg = {"message" : "* input data error."}
    return msg, 200

@selfHeathData.route('/selfHeathData', methods=["PATCH"])
def updateOneRecord():
    '''
    file: swagger/selfHealthData/upSelfHealthData.yml
    '''
    data = json.loads(request.get_data())
    msg = SelfHeathDataService.update_record(data)
    return msg, 200

@selfHeathData.route('/selfHeathData/<self_health_id>', methods=["DELETE"])
def deleteOne(self_health_id):
    '''
    file: swagger/selfHealthData/delSelfHealthData.yml
    '''
    return SelfHeathDataService.delete_by_id(self_health_id), 200



