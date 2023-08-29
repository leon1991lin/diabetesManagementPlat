import json
import pandas as pd
from pprint import pprint

from apiproject.repository import MedicalRecordsRspository, MedicalRecordsDataRepository, PrescriptionRepository

def get_patient_medical_records(user_id:int):

    result_dict = MedicalRecordsRspository.get_newest_records_by_id(user_id)[0]

    result_dict["medical_datas"] = MedicalRecordsDataRepository.get_data_by_recrod_id(result_dict.pop("medical_record_id"))
    result_dict["prescriptions"] = PrescriptionRepository.get_prescription_by_id(result_dict.pop("prescription_id"))

    return result_dict

if __name__ == '__main__':
    pprint(get_patient_medical_records(1))