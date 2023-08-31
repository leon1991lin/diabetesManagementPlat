import json
import pandas as pd
from pprint import pprint

from apiproject.repository import MedicalRecordsRspository, MedicalRecordsDataRepository, PrescriptionRepository
from apiproject.service import ageCalculation, SelfHealthDataService

def get_patient_medical_records(user_id:int):

    result_dict = MedicalRecordsRspository.get_newest_records_by_id(user_id)[0]

    result_dict["medical_datas"] = MedicalRecordsDataRepository.get_data_by_recrod_id(result_dict.pop("medical_record_id"))
    result_dict["prescriptions"] = PrescriptionRepository.get_prescription_by_id(result_dict.pop("prescription_id"))
    result_dict["patient_age"] = ageCalculation.getAge(result_dict.pop("patient_born_date"))
    result_dict['patient_gender'] = "男性" if result_dict.pop("patient_gender") == "M" else "女性"
    result_dict['patient_BMI'] = SelfHealthDataService.read_newest_by_patient_id(user_id)["datas"]["BMI"]
    return result_dict

if __name__ == '__main__':
    pprint(get_patient_medical_records(1))