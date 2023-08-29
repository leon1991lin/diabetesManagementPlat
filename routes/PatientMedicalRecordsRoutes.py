import json
from flask import Blueprint, request

from apiproject.service import MedicalRecordsService

medicalRecords = Blueprint("medicalRecords", __name__, template_folder='routes')

@medicalRecords.route('/medicalRecords/<user_id>', methods=["GET"])
def getMedicalRecordsByUserID(user_id):
    return MedicalRecordsService.get_patient_medical_records(user_id)