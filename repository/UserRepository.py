import datetime
import json
from pprint import pprint

from sqlalchemy.orm import sessionmaker

from apiproject import mysql_engine
from apiproject.models import User

'''
Table: Users
'''
mysql = mysql_engine()
Session = sessionmaker(bind=mysql_engine().engine)


def insert_one(user: dict):
    session = Session()

    try:
        session.add(User(**user))
        session.commit()

    except Exception as e:
        print(e)

    finally:
        session.close()
    return


def update_one(user: dict):
    session = Session()
    try:
        record = session.query(User) \
            .filter(User.user_id == User["user_id"]) \
            .one()

        for key, value in user.items():
            match key:
                case "user_name":
                    record.user_name = value
                case "user_account":
                    record.user_account = value
                case "user_password":
                    record.user_password = value
                case "born_date":
                    record.born_date = value
                case "telephone":
                    record.telephone = value
                case "address":
                    record.address = value
                case "user_type":
                    record.user_type = value
                case "institution_id":
                    record.institution_id = value
                case _:
                    pass

        record.update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        session.commit()

    except Exception as e:
        print(e)

    finally:
        session.close()

    return

def get_all():
    session = Session()
    records_list = []

    all_datas = session.query(User)
    for row in all_datas:
        tmp = vars(row)
        tmp.pop("_sa_instance_state")
        records_list.append(tmp)
    return records_list

def get_user_by_id(user_id:int):
    session = Session()
    result = {}
    try:
        records = session.query(User).filter(User.user_id==user_id).one()

        result = vars(records)
        result.pop("_sa_instance_state")


    except Exception as e:
        print("Error: ", e)

    finally:
        session.close()

    return result


def get_user_by_name(user_name:str):
    session = Session()
    records_list = []

    try:
        records = session.query(User).filter(User.user_name == user_name)

        for row in records:
            tmp = vars(row)
            tmp.pop("_sa_instance_state")
            records_list.append(tmp)

    except Exception as e:
        print("Error: ", e)

    finally:
        session.close()

    return records_list



def delete_one_by_id(user_id):
    session = Session()
    try:
        del_record = session.query(User).filter(User.self_health_id == user_id).first()
        session.delete(del_record)
        session.commit()

    except Exception as e:
        print("Error: ", e)
        return e
    finally:
        session.close()

    return del_record.user_id



if __name__ == '__main__':

    # pprint(get_all())

    pprint(get_user_by_id(1))

    pprint(get_user_by_name("Mary"))