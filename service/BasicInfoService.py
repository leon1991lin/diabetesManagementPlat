from apiproject.repository import RecordTypeRspository

def getRecordType():
    return RecordTypeRspository.get_all()

