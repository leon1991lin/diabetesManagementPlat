import datetime, json
from pprint import pprint

import pandas as pd
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker, aliased

from apiproject import mysql_engine
from apiproject.models import User, MedicalRecords, MedicalInstitution, MedicalStaff, MedicalRecordsData

'''
Table: medical_records
'''
mysql = mysql_engine()
Session = sessionmaker(bind=mysql_engine().engine)


def get_newest_records_by_id(patient_id:int):
    session = Session()
    records_list = []

    FirstMedicalRecordDay = session.query(MedicalRecords.patient_id, MedicalRecords.record_date)\
                            .filter(MedicalRecords.phase_type == 1)\
                            .subquery()

    NearlyMedicalRecordDay = session.query(func.max(MedicalRecords.record_date))\
                            .filter(MedicalRecords.patient_id == patient_id)\
                            .subquery()
    DoctorInfo      = aliased(MedicalStaff)

    records = session.query(User.user_name,
                            User.gender,
                            User.born_date,
                            MedicalRecords.medical_record_id,
                            MedicalRecords.prescription_id,
                            MedicalRecords.diagnosis,
                            MedicalRecords.record_date,
                            FirstMedicalRecordDay.c.record_date,
                            DoctorInfo.staff_name
                            )\
            .join(User, MedicalRecords.patient_id==User.user_id)\
            .join(MedicalInstitution, MedicalRecords.institution_id == MedicalInstitution.institution_id) \
            .join(FirstMedicalRecordDay, MedicalRecords.patient_id == FirstMedicalRecordDay.c.patient_id) \
            .join(DoctorInfo , MedicalRecords.doctor_id == DoctorInfo.staff_id) \
            .filter(MedicalRecords.patient_id == patient_id) \
            .filter(MedicalRecords.record_date.in_(NearlyMedicalRecordDay)) \
            .all()

    for record in records:
        tmp_list = [i for i in record]
        records_list.append(tmp_list)

    columns = ["patient_name", "patient_gender", "patient_born_date", "medical_record_id", "prescription_id", "diagnosis", "record_date", "first_visit_date", "doctor"]

    return pd.DataFrame(records_list, columns=columns).to_dict("records")

if __name__ == '__main__':
    df= get_newest_records_by_id(1)

    pprint(df)

