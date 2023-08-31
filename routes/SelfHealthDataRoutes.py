import json
from datetime import date

from flask import Blueprint, request, jsonify

from apiproject.service import SelfHealthDataService

selfHealthData = Blueprint("selfHealthData", __name__, template_folder='routes')

@selfHealthData.route('/selfHealthData', methods=["GET"])
def selfHeathDatas():
    '''
    file: swagger/selfHealthData/selfHealthData.yml
    '''
    return SelfHealthDataService.read_all(), 200

@selfHealthData.route('/selfHealthData', methods=["POST"])
def saveNewData():
    '''
    file: swagger/selfHealthData/addSelfHealthData.yml
    '''
    data =json.loads(request.get_data())
    if type(data) == dict:
        msg = SelfHealthDataService.add_record(data)
    elif type(data) == list:
        msg = SelfHealthDataService.add_records(data)
    else:
        msg = {"message" : "* input data error."}
    return msg, 200

@selfHealthData.route('/selfHealthData', methods=["PATCH"])
def updateOneRecord():
    '''
    file: swagger/selfHealthData/upSelfHealthData.yml
    '''
    data = json.loads(request.get_data())
    msg = SelfHealthDataService.update_record(data)
    return msg, 200

@selfHealthData.route('/selfHealthData/<self_health_id>', methods=["DELETE"])
def deleteOne(self_health_id):
    '''
    file: swagger/selfHealthData/delSelfHealthData.yml
    '''
    return SelfHealthDataService.delete_by_id(self_health_id), 200

@selfHealthData.route('/selfHealthData/newest/<patient_id>', methods=["GET"])
def newest_summary(patient_id):
    '''
    file: swagger/selfHealthData/newest_data_for_user.yml
    '''
    return jsonify(SelfHealthDataService.read_newest_by_patient_id(patient_id)), 200

@selfHealthData.route("/selfHealthData/monthlydata", methods=["POST"])
def monthly_data():
    '''
    file: swagger/selfHealthData/monthlydata_for_user.yml
    '''
    input_data = json.loads(request.get_data())
    if ("patient_id" not in input_data.keys()) or ("search_month"  not in input_data.keys()) or ("record_names" not in input_data.keys()):
        return "Input Data Error: miss item", 400
    elif (type(input_data["patient_id"]) != int) or (type(input_data["search_month"]) != str) or (type(input_data["record_names"]) != list):
        return "Input Data Error: error data type", 400
    else:
<<<<<<< HEAD
        return jsonify(SelfHealthDataService.read_monthly_data(patient_id=input_data["patient_id"], record_names=input_data["record_names"], start_date=input_data["search_month"])), 200
=======
        return jsonify(SelfHealthDataService.read_monthly_data(patient_id=input_data["patient_id"],record_names=input_data["record_names"], start_date=input_data["search_month"])), 200
>>>>>>> 38669ad1fa8a111210b152a746a8b52b81ea700d

@selfHealthData.route('/selfHealthData/weeklydata/<patient_id>', methods=["GET"])
def weekly_data(patient_id):
    '''
    file: swagger/selfHealthData/weekly_avgdata_for_user.yml
    '''
    return jsonify(SelfHealthDataService.read_weekly_by_patient_id(patient_id=patient_id, searchDay=date.fromisoformat("2023-08-23"))), 200
