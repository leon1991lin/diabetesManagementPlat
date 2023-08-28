from pprint import pprint

from sqlalchemy.orm import sessionmaker

from apiproject import mysql_engine
from apiproject.models import RecordType

mysql = mysql_engine()
Session = sessionmaker(bind=mysql_engine().engine)

def get_all():
    session = Session()
    records_list = []

    all_datas = session.query(RecordType)
    for row in all_datas:
        tmp = vars(row)
        tmp.pop("_sa_instance_state")
        records_list.append(tmp)
    return records_list

def get_id_by_name(name):
    session = Session()
    return (session.query(RecordType).filter(RecordType.record_name_cn == name).first()).type_id

if __name__ == '__main__':
    
    # pprint(get_all())

    pprint(get_id_by_name("身高"))