import datetime

from sqlalchemy import Column, Integer, String, DateTime, Date, Float,ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

from apiproject import mysql_engine

Base = declarative_base()

class RecordType(Base):
    __tablename__="record_type"

    # columns
    type_id         = Column(Integer, primary_key=True, autoincrement=True)
    record_name     = Column(String)
    record_unit     = Column(String)
    record_group    = Column(Integer)
    create_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    update_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    delete_time     = Column(DateTime)

    def __init__(self, record_name, record_unit, record_group):
        self.record_name=record_name
        self.record_unit=record_unit
        self.record_group=record_group


    def __repr__(self) -> str:
        return f"RecordType(type_id={self.type_id!r}, record_name={self.record_name!r}, record_unit={self.record_unit!r}, record_group={self.record_group!r})"

class User(Base):
    __tablename__ = "user"

    #columns
    user_id         = Column(Integer, primary_key=True, autoincrement=True)
    user_name       = Column(String(12))
    user_account    = Column(String(64), unique=True)
    user_password   = Column(String(128))
    born_date       = Column(Date)
    telephone       = Column(String(32))
    address         = Column(String(128))
    user_type       = Column(Integer)
    create_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    update_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    delete_time     = Column(DateTime)

    def __init__(self, name, account, password, born_date, telephone, address, user_type):

        self.user_name      = name
        self.user_account   = account
        self.user_password  = password # save hashed password
        self.born_date      = born_date
        self.telephone      = telephone
        self.address        = address
        self.user_type      = user_type

class SelfHealthData(Base):
    __tablename__ = "self_health_data"

    self_health_id  = Column(Integer, primary_key=True, autoincrement=True)
    patient_id      = Column(Integer, ForeignKey("user.user_id"))
    recorder_id     = Column(Integer, ForeignKey("user.user_id"))
    record_type     = Column(Integer, ForeignKey("record_type.type_id"))
    record_date     = Column(Date)
    record          = Column(Float)
    create_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    update_time     = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    delete_time     = Column(DateTime)

    def __init__(self, patient_id, recorder_id, record_type, record_date, record):
        self.patient_id     = patient_id
        self.recorder_id    = recorder_id
        self.record_type    = record_type
        self.record_date    = record_date
        self.record         = record


if __name__ == '__main__':
    engine = mysql_engine().engine
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(User).all()

    for i in result:
        print(i.user_name)

