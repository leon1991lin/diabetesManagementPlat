from datetime import datetime, timedelta, date
import json
import pandas as pd
from pprint import pprint

from apiproject.repository import SelfHealthDataRepository, RecordTypeRspository


def add_record(data):

    if type(data) == str:
        try:
            data = json.loads(data)
            msg = SelfHealthDataRepository.insert_one(data)
        except Exception as e:
            msg = f"Input Type Error: {e} , input data:{data}."


    elif type(data) == dict:
        if      ("patient_id"   in data.keys()) \
            and ("record_type"  in data.keys()) \
            and ("record_date"  in data.keys())\
            and ("record"       in  data.keys()):

            msg = SelfHealthDataRepository.insert_one(data)

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

        msg = SelfHealthDataRepository.insert_all(data_list)
        return {"message": msg}

def update_record(data):

    if type(data) == str:
        try:
            data = json.loads(data)
            msg = SelfHealthDataRepository.update_one_record(data)
        except Exception as e:
            msg = f"Update Type Error: {e} , input data:{data}."


    elif type(data) == dict:
        if ("patient_id" in data.keys()) \
                and ("record_type" in data.keys()) \
                and ("record_date" in data.keys()) \
                and ("record" in data.keys()):

            msg = SelfHealthDataRepository.update_one_record(data)

        else:

            msg = f"Update Data Key Error: need 'patient_id','record_type', 'record_date' and 'record'."

    else:

        msg = f"Update Type Error: type need to be 'dict' , input data type: {type(data)}."

    return {"message": msg}

def delete_by_id(self_health_id):

    try:

        return {"message": SelfHealthDataRepository.delete_one_by_id(self_health_id)}

    except Exception as e:

        return {"message": f"Delete Error: {e}."}

def read_all():

    return {"message": SelfHealthDataRepository.get_all()}

def read_newest_by_patient_id(patient_id):

    df = pd.DataFrame(SelfHealthDataRepository.get_data_by_patient_id_join(patient_id))
    sector = df.groupby("record_name")

    present_items = ["GlucoseAC", "GlucosePC", "DBP", "SBP", "Height", "Weight"]

    newest_data = {}
    for item in present_items:
        newest_data[item] = sector.get_group(item)["record"].iloc[0]
        # newest_data[item] = df.loc[df["record_name"]==item, "record"].iloc[0]

    newest_data["BMI"] = round(newest_data["Weight"]/((newest_data["Height"]/100)**2), 2)

    return {
        "patient_id":patient_id,
        "patient_name":df["user_name"][0],
        "datas" : newest_data
    }

def read_monthly_data(patient_id, record_names,start_date):
    df = pd.DataFrame()
    for record_name in record_names:
        tmp_df = pd.DataFrame(SelfHealthDataRepository.get_monthly_data(patient_id=patient_id, start_date=start_date, record_type=RecordTypeRspository.get_id_by_name(record_name)))
        df = pd.concat([df, tmp_df])

    df = df.sort_values(by=["record_time", "record_type"], ascending=True)

    return df.to_dict("records")

def read_weekly_by_patient_id(patient_id, searchDay=datetime.now().date()):
    resultList = []

    curr_day = searchDay
    present_items = {"avgGlucoseAC":5, "avgGlucosePC":6, "avgDBP":7, "avgSBP":8}

    df = pd.DataFrame(SelfHealthDataRepository.get_patient_data_by_patient_id(patient_id))
    if df.empty:
        return resultList

    df["record_date"] = df["record_time"].apply(lambda t: t.date())
    df = df.loc[df.record_type.isin(present_items.values())]

    while curr_day >= (searchDay - timedelta(days=7)):

        tmp = {
            "record_date":curr_day.strftime("%Y-%m-%d"),
            "avgGlucoseAC":-99,
            "avgGlucosePC": -99,
            "avgDBP":-99,
            "avgSBP":-99
        }
        curr_df = df.loc[df.record_date == curr_day]
        if curr_df.empty:
            pass
        else:
            secdf = curr_df.groupby("record_type")
            for name, type in present_items.items():
                tmp[name] = secdf.get_group(type)["record"].mean()

        resultList.append(tmp)

        curr_day -= timedelta(days=1)

    def keyfn(ele):
        return ele["record_date"]

    resultList.sort(key=keyfn, reverse=True)
    pprint(resultList)
    return resultList


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

   # pprint(delete_by_id(82))

   # pprint(read_newest_by_patient_id(1))

   # pprint(read_monthly_data(1, ["飯前血糖","飯後血糖"], "202308"))

   pprint(read_weekly_by_patient_id(1, date.fromisoformat("2023-08-23")))