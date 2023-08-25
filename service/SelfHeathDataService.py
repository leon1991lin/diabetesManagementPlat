import json
from pprint import pprint

# from apiproject.TableRepository import dm_table
from apiproject.repository import SelfHeathDataRepository


def add_record(data):

    if type(data) == str:
        try:
            data = json.loads(data)
            msg = SelfHeathDataRepository.insert_one(data)
        except Exception as e:
            msg = f"Input Type Error: {e} , input data:{data}."


    elif type(data) == dict:
        if      ("patient_id"   in data.keys()) \
            and ("record_type"  in data.keys()) \
            and ("record_date"  in data.keys())\
            and ("record"       in  data.keys()):

            msg = SelfHeathDataRepository.insert_one(data)

        else:

            msg =  f"Input Data Key Error: need 'patient_id','record_type', 'record_date' and 'record'."

    else:

        msg = f"Input Type Error: type need to be 'dict' , input data type: {type(data)}."

    return {"message":msg}


def add_records(data_list:list):

    for data in data_list:

        if type(data) == str:
            try:
                data = json.loads(data)

            except Exception as e:
                msg = f"Input Type Error: {e} , input data:{data}."
                return {"message":msg}

        elif type(data) == dict:
            if ("patient_id" in data.keys()) \
                    and ("record_type" in data.keys()) \
                    and ("record_date" in data.keys()) \
                    and ("record" in data.keys()):
                pass

            else:
                msg = f"Input Element Key Error: need 'patient_id','record_type', 'record_date' and 'record'."
                return {"message": msg}

        else:

            msg = f"Input Element Type Error: element type need to be 'dict' , input data type: {type(data)}."
            return {"message": msg}

        msg = SelfHeathDataRepository.insert_all(data_list)
        return {"message": msg}

def update_record(data):

    if type(data) == str:
        try:
            data = json.loads(data)
            msg = SelfHeathDataRepository.update_one_record(data)
        except Exception as e:
            msg = f"Update Type Error: {e} , input data:{data}."


    elif type(data) == dict:
        if ("patient_id" in data.keys()) \
                and ("record_type" in data.keys()) \
                and ("record_date" in data.keys()) \
                and ("record" in data.keys()):

            msg = SelfHeathDataRepository.update_one_record(data)

        else:

            msg = f"Update Data Key Error: need 'patient_id','record_type', 'record_date' and 'record'."

    else:

        msg = f"Update Type Error: type need to be 'dict' , input data type: {type(data)}."

    return {"message": msg}

def delete_by_id(self_health_id):

    try:

        return {"message": SelfHeathDataRepository.delete_one_by_id(self_health_id)}

    except Exception as e:

        return {"message": f"Delete Error: {e}."}

def read_all():

    return {"message": SelfHeathDataRepository.get_all()}



if __name__ == '__main__':

   data={
        "patient_id"    : 99,
        "recorder_id"   : 99,
        "record_type"   : 5,
        "record_date"   : "2023/08/24",
        "record"        : 85
    }
   datas = [
       {
           "patient_id": 99,
           "recorder_id": 99,
           "record_type": 6,
           "record_date": "2023/08/24",
           "record": 120
       },
       {
           "patient_id": 99,
           "recorder_id": 99,
           "record_type": 7,
           "record_date": "2023/08/24",
           "record": 80
       },
       {
           "patient_id": 99,
           "recorder_id": 99,
           "record_type": 8,
           "record_date": "2023/08/24",
           "record": 110
       }
   ]
   # pprint(add_record(data))

   # pprint(add_records(datas))

   # pprint(update_record(data))

   pprint(delete_by_id(82))