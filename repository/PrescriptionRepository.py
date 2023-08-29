import datetime, json
from pprint import pprint

import pandas as pd
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker, aliased

from apiproject import mysql_engine
from apiproject.models import User, MedicalRecords, MedicalInstitution, MedicalStaff, MedicalRecordsData, RecordType, \
    PrescriptionRelate, Medicine

'''
Table: prescription_relate & medicine
'''
mysql = mysql_engine()
Session = sessionmaker(bind=mysql_engine().engine)

def get_prescription_by_id(prescription_id:int):
    session = Session()
    records_list = []

    records = session.query(PrescriptionRelate, Medicine)\
                    .join(Medicine, PrescriptionRelate.medicine_id == Medicine.medicine_id)\
                    .filter(PrescriptionRelate.prescription_id == prescription_id) \
                    .all()

    for prescriptionRelate, medicine in records:
        tmp = {}
        prescription_dict = vars(prescriptionRelate)
        prescription_dict.update(vars(medicine))
        tmp["medicine_name"] = prescription_dict["medicine_name"]
        tmp["medicine_dosage"] = prescription_dict["medicine_dosage"]
        records_list.append(tmp)
    # pprint(records_list)
    return records_list

if __name__ == '__main__':
    get_prescription_by_id(1)