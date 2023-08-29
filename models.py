import datetime

import pandas as pd
from sqlalchemy import Column, Integer, String, DateTime, Date, Float,ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

from apiproject import mysql_engine

Base = declarative_base()

# APP 使用者資料
class User(Base):
    __tablename__ = "user"

    #columns
    user_id         = Column(Integer, primary_key=True, autoincrement=True)
    user_name       = Column(String(12))
    user_account    = Column(String(64), unique=True)
    user_password   = Column(String(128))
    born_date       = Column(Date)
    gender          = Column(String(2))
    telephone       = Column(String(32))
    address         = Column(String(128))
    user_type       = Column(Integer)
    institution_id  = Column(Integer, default=0)
    create_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    update_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    delete_time     = Column(DateTime)

    def __init__(self, name, account, password, born_date, gender,telephone, address, user_type):

        self.user_name      = name
        self.user_account   = account
        self.user_password  = password # save hashed password
        self.born_date      = born_date
        self.gender         = gender
        self.telephone      = telephone
        self.address        = address
        self.user_type      = user_type

# 日常監控數據
class SelfHealthData(Base):
    __tablename__ = "self_health_data"

    self_health_id  = Column(Integer, primary_key=True, autoincrement=True)
    patient_id      = Column(Integer, ForeignKey("user.user_id"))
    recorder_id     = Column(Integer, ForeignKey("user.user_id"))
    record_type     = Column(Integer, ForeignKey("record_type.type_id"))
    record_time     = Column(DateTime)
    record          = Column(Float)
    create_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    update_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    delete_time     = Column(DateTime)

    def __init__(self, patient_id, recorder_id, record_type, record_date, record):
        self.patient_id     = patient_id
        self.recorder_id    = recorder_id
        self.record_type    = record_type
        self.record_time    = record_date
        self.record         = record

# 醫療機構
class MedicalInstitution(Base):
    __tablename__ = "medical_institution"

    institution_id      = Column(Integer, primary_key=True, autoincrement=True)
    institution_name    = Column(String(32))
    institution_type    = Column(Integer)
    telephone           = Column(String(32))
    address             = Column(String(128))
    contact_person      = Column(String(16))
    create_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    update_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    delete_time     = Column(DateTime)

    def __init__(self, institution_name, institution_type, telephone, address, contact_person):

        self.institution_name   =   institution_name
        self.institution_type   =   institution_type
        self.telephone          =   telephone
        self.address            =   address
        self.contact_person     =   contact_person

# 醫事人員
class MedicalStaff(Base):
    __tablename__ = "medical_staff"

    staff_id            = Column(Integer, primary_key=True, autoincrement=True)
    staff_name          = Column(String(32))
    staff_account       = Column(String(64))
    staff_password      = Column(String(256))
    staff_position_code = Column(Integer)
    staff_position      = Column(String(16))
    create_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    update_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    delete_time     = Column(DateTime)

    def __init__(self, staff_name, staff_account, staff_password, staff_position_code, staff_position):
        self.staff_name             = staff_name
        self.staff_account          = staff_account
        self.staff_password         = staff_password
        self.staff_position_code    = staff_position_code
        self.staff_position         = staff_position

# 醫療機構與人員關聯表
class InstitutionStaffRelate(Base):
    __tablename__ = "institution_staff_relate"

    relate_id       = Column(Integer, primary_key=True, autoincrement=True)
    institution_id  = Column(Integer, ForeignKey("medical_institution.institution_id"))
    staff_id        = Column(Integer, ForeignKey("medical_staff.staff_id"))
    create_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    update_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    delete_time     = Column(DateTime)

    def __init__(self, institution_id, staff_id):
        self.institution_id =   institution_id
        self.staff_id       =   staff_id

# 處方與藥品關聯
class PrescriptionRelate(Base):
    __tablename__ =  "prescription_relate"

    relate_id       = Column(Integer, primary_key=True, autoincrement=True)
    prescription_id = Column(Integer, ForeignKey("medical_records.prescription_id"))
    medicine_id     = Column(Integer, ForeignKey("medicine.medicine_id"))
    create_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    update_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    delete_time     = Column(DateTime)

    def __init__(self, prescription_id, medicine_id):
        self.prescription_id    =   prescription_id
        self.medicine_id        =   medicine_id

# 藥品與使用指示資料
class Medicine(Base):
    __tablename__ = "medicine"
    medicine_id     = Column(Integer, primary_key=True, autoincrement=True)
    medicine_name   = Column(String(16))
    medicine_dosage = Column(String(64))
    create_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    update_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    delete_time     = Column(DateTime)

    def __init__(self, medicine_name, medicine_dosage):
        self.medicine_name    =   medicine_name
        self.medicine_dosage  =   medicine_dosage

# 階段參數
class PhaseType(Base):
    __tablename__ = "phase_type"

    phase_id        = Column(Integer, primary_key=True, autoincrement=True)
    diseases_name   = Column(String(16))
    phase_code      = Column(String(16))
    phase_name      = Column(String(16))
    create_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    update_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    delete_time     = Column(DateTime)

    def __init__(self, diseases_name, phase_code, phase_name):
        self.diseases_name = diseases_name
        self.phase_code = phase_code
        self.phase_name = phase_name


# 紀錄類型參數
class RecordType(Base):
    __tablename__ = "record_type"

    # columns
    type_id = Column(Integer, primary_key=True, autoincrement=True)
    record_name = Column(String)
    record_name_cn = Column(String)
    record_unit = Column(String)
    record_group = Column(Integer)
    create_time = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    update_time = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    delete_time = Column(DateTime)

    def __init__(self, record_name, record_name_cn, record_unit, record_group):
        self.record_name = record_name
        self.record_name_cn = record_name_cn
        self.record_unit = record_unit
        self.record_group = record_group

    def __repr__(self) -> str:
        return f"RecordType(type_id={self.type_id!r}, record_name={self.record_name!r}, record_unit={self.record_unit!r}, record_group={self.record_group!r})"

# 回診/就診紀錄
class MedicalRecords(Base):
    __tablename__ = "medical_records"

    medical_record_id       = Column(Integer, primary_key=True, autoincrement=True)
    record_date             = Column(Date)
    patient_id              = Column(Integer, ForeignKey("user.user_id"))
    institution_id          = Column(Integer, ForeignKey("medical_institution.institution_id"))
    doctor_id               = Column(Integer, ForeignKey("medical_staff.staff_id"))
    dietitian_id            = Column(Integer, ForeignKey("medical_staff.staff_id"))
    educator_id             = Column(Integer, ForeignKey("medical_staff.staff_id"))
    phase_type              = Column(Integer, ForeignKey("phase_type.phase_id"))
    prescription_id         = Column(Integer)
    diagnosis               = Column(String(128))
    memo                    = Column(String)
    follow_up_date          = Column(Date)
    create_time = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    update_time = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    delete_time = Column(DateTime)

    def __init__(self, inputs):
        self.record_date = inputs["record_date"]
        self.patient_id = inputs["patient_id"]
        self.institution_id = inputs["institution_id"]
        self.doctor_id = inputs["doctor_id"]
        self.dietitian_id = inputs["dietitian_id"]
        self.educator_id = inputs["educator_id"]
        self.phase_type = inputs["phase_type"]
        self.prescription_id = inputs["prescription_id"]
        self.diagnosis = inputs["diagnosis"]
        self.memo       = inputs["memo"]
        self.follow_up_date = inputs["follow_up_date"]

# 檢驗數據
class MedicalRecordsData(Base):
    __tablename__ = "medical_records_data"
    medical_record_data_id  = Column(Integer, primary_key=True, autoincrement=True)
    medical_record_id       = Column(Integer, ForeignKey("medical_records.medical_record_id"))
    record_type             = Column(Integer, ForeignKey("record_type.type_id"))
    record                  = Column(Float)
    test_date               = Column(Date)
    create_time = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    update_time = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    delete_time = Column(DateTime)

    def __init__(self, medical_record_id, record_type, record, test_date):
        self.medical_record_id = medical_record_id
        self.record_type = record_type
        self.record = record
        self.test_date = test_date

if __name__ == '__main__':
    engine = mysql_engine().engine
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(User).all()

    records_list = []
    for row in result:
        tmp = vars(row)
        tmp.pop("_sa_instance_state")
        records_list.append(tmp)
    df = pd.DataFrame(records_list)
    print(df)


