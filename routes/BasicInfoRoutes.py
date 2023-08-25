import json
from flask import Blueprint, request

from apiproject.service import BasicInfoService

basicInfo = Blueprint("basicInfo", __name__, template_folder='routes')

@basicInfo.route('/basicInfo/recordType', methods=["GET"])
def getRecordType():
    '''
    file: swagger/basicInfo/recordType.yml
    '''
    return BasicInfoService.getRecordType()




