import datetime, json
from pprint import pprint

import pandas as pd
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker, aliased

from apiproject import mysql_engine
from apiproject.models import  MedicalInstitution, User

'''
Table: medical_institution
'''
mysql = mysql_engine()
Session = sessionmaker(bind=mysql_engine().engine)

def get_all():
    session = Session()
    records_list = []
    records = session.query(MedicalInstitution).all()

    for record in records:
        tmp = vars(record)
        tmp.pop("_sa_instance_state")
        records_list.append(tmp)
    pprint(records_list)
    return records_list


if __name__ == '__main__':
    get_all()