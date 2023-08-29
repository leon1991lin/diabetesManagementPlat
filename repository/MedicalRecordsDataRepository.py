import datetime, json
from pprint import pprint

import pandas as pd
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker, aliased

from apiproject import mysql_engine
from apiproject.models import  MedicalRecordsData, RecordType

'''
Table: medical_records_data
'''
mysql = mysql_engine()
Session = sessionmaker(bind=mysql_engine().engine)

def get_data_by_recrod_id(medical_record_id:int):
    session = Session()
    records_list = []
    records = session.query(MedicalRecordsData, RecordType.record_name_cn, RecordType.record_name, RecordType.record_unit ) \
            .join(RecordType, MedicalRecordsData.record_type == RecordType.type_id) \
            .filter(MedicalRecordsData.medical_record_id == medical_record_id)\
            .all()

    for record, record_name, record_name_cn, record_unit in records:
        tmp={}
        record_dict = vars(record)
        tmp["record"] = record_dict["record"]
        tmp["test_date"] = record_dict["test_date"]
        tmp["record_name"] = record_name
        tmp["record_name_cn"] = record_name_cn
        tmp["record_unit"] = record_unit
        records_list.append(tmp)
    # pprint(records_list)

    return records_list

if __name__ == '__main__':
    get_data_by_recrod_id(1)