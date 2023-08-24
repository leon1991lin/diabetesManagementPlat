import datetime
import json
from pprint import pprint

import pandas as pd
from sqlalchemy.orm import sessionmaker

from apiproject import mysql_engine
from apiproject.models import SelfHealthData, RecordType, User

'''
Table - self_health_data
    Create: insert_one(dict), insert_all(list)
    Update: update_one_record()
    Read:   get_all(), get_patient_data_by_patient_id()
    Delete: delete_one_by_id()
'''
mysql = mysql_engine()
Session = sessionmaker(bind=mysql_engine().engine)

def insert_one(self_health_data:dict):
    session = Session()
    # new_record = SelfHealthData(
    #     patient_id  = self_health_data["patient_id"],
    #     recorder_id = self_health_data["recorder_id"],
    #     record_type = self_health_data["record_type"],
    #     record_date = self_health_data["record_date"],
    #     record      = self_health_data["record"],
    # )

    try:
        # session.add(new_record)
        session.add(SelfHealthData(**self_health_data))
        session.commit()

    except Exception as e:
        print("Error: ", e)
        session.rollback()
        return f"Insert Error: {e}"

    finally:
        session.close()
    return  "Success"


def insert_all(self_health_datas:list):
    session = Session()
    new_records=[]


    for self_health_data in self_health_datas:
        # new_records.append(SelfHealthData(
        #                     patient_id  = self_health_data["patient_id"],
        #                     recorder_id = self_health_data["recorder_id"],
        #                     record_type = self_health_data["record_type"],
        #                     record_date = self_health_data["record_date"],
        #                     record      = self_health_data["record"],
        #                 ))
        new_records.append(SelfHealthData(**self_health_data))
    try:
        session.add_all(new_records)
        session.commit()

    except Exception as e:
        print("Error: ", e)
        session.rollback()
        return f"Insert Error: {e}"

    finally:
        session.close()
    return "Success"

def update_one_record(self_health_update_data):
    session = Session()
    try:
        record = session.query(SelfHealthData)\
                .filter(SelfHealthData.patient_id==self_health_update_data["patient_id"])\
                .filter(SelfHealthData.record_date==self_health_update_data["record_date"])\
                .filter(SelfHealthData.record_type==self_health_update_data["record_type"])\
                .first()

        record.record=self_health_update_data["record"]
        record.update_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        session.commit()

    except Exception as e:
        print("Error: ", e)
        session.rollback()
        return f"Update Error: {e}"

    finally:
        session.close()

    return "Success"

def get_all():
    session = Session()
    records_list = []

    all_datas = session.query(SelfHealthData)
    for row in all_datas:
        tmp = vars(row)
        tmp.pop("_sa_instance_state")
        records_list.append(tmp)
    return records_list

def get_patient_data_by_patient_id(patient_id:int):
    session = Session()
    records_list = []

    try:
        records = session.query(SelfHealthData).filter(SelfHealthData.patient_id==patient_id)

        for row in records:

            tmp = vars(row)
            tmp.pop("_sa_instance_state")
            records_list.append(tmp)

    except Exception as e:
        print("Error: ", e)

    finally:
        session.close()

    return records_list


def delete_one_by_id(self_health_id):
    session = Session()
    try:
        del_record = session.query(SelfHealthData).filter(SelfHealthData.self_health_id==self_health_id).first()
        session.delete(del_record)
        session.commit()

    except Exception as e:
        print("Error: ", e)
        session.rollback()
        return f"Delete Error: {e}"
    finally:
        session.close()

    return "Success"


"""
Join RecordType table & User table
"""

def get_data_by_patient_id_join(patient_id:int):
    session = Session()
    records_list = []

    try:
        records = session.query(SelfHealthData, RecordType, User) \
            .filter(SelfHealthData.record_type == RecordType.type_id) \
            .filter(SelfHealthData.patient_id == User.user_id) \
            .filter(SelfHealthData.patient_id == patient_id).all()

        for selfHealthData, recordType, user in records:

            tmp1 = vars(selfHealthData)
            tmp2 = vars(recordType)
            tmp3 = vars(user)

            tmp1.update(tmp2)
            tmp1.update(tmp3)
            tmp1.pop("_sa_instance_state")
            records_list.append(tmp1)

    except Exception as e:
        print("Error: ", e)

    finally:
        session.close()

    return records_list





if __name__ == '__main__':

    self_health_data={
        "patient_id"    : 99,
        "recorder_id"   : 99,
        "record_type"   : 5,
        "record_date"   : "2023/08/23",
        "record"        : 82
    }

    self_health_datas=[
        {
        "patient_id"    : 99,
        "recorder_id"   : 99,
        "record_type"   : 6,
        "record_date"   : "2023/08/23",
        "record"        : 120
        },
        {
            "patient_id": 99,
            "recorder_id": 99,
            "record_type": 7,
            "record_date": "2023/08/23",
            "record": 80
        },
        {
            "patient_id": 99,
            "recorder_id": 99,
            "record_type": 8,
            "record_date": "2023/08/23",
            "record": 110
        }
    ]

    # insert_one(self_health_data)

    # insert_all(self_health_datas)

    # update_one_record(self_health_data)

    # records = get_patient_data_by_patient_id(99)
    # pprint(records)

    # pprint(get_all())

    # delete_one_by_id(80)

    df = pd.DataFrame(get_data_by_patient_id_join(1))
    print(df.columns)
    print(df.info())
