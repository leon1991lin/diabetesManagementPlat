import json
from datetime import date

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

@selfHeathData.route('/selfHeathData/newest/<patient_id>', methods=["GET"])
def newest_summary(patient_id):
    return SelfHeathDataService.read_newest_by_patient_id(patient_id), 200

@selfHeathData.route("/selfHeathData/monthlydata", methods=["POST"])
def monthly_data():
    input_data = json.loads(request.get_data())
    if ("patient_id" not in input_data.keys()) or ("search_month"  not in input_data.keys()) or ("record_names" not in input_data.keys()):
        return "Input Data Error: miss item", 400
    elif (type(input_data["patient_id"]) != int) or (type(input_data["search_month"]) != str) or (type(input_data["record_names"]) != list):
        return "Input Data Error: error data type", 400
    else:
        return SelfHeathDataService.read_monthly_data(patient_id=input_data["patient_id"],record_names=input_data["record_names"], start_date=input_data["search_month"]), 200

@selfHeathData.route('/selfHeathData/weeklydata/<patient_id>', methods=["GET"])
def weekly_data(patient_id):
    return SelfHeathDataService.read_weekly_by_patient_id(patient_id, searchDay=date.fromisoformat("2023-08-20")), 200
