import os
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

import pandas as pd
from sqlalchemy import create_engine
from apiproject.config import settings, template

username="root"
password="0000"
host="localhost"
port="3306"
database_name="dmplat"

app = Flask(__name__)

swagger = Swagger(app, template=template)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SWAGGER'] = settings
app.config["TEMPLATES_AUTO_RELOAD"] = True


class mysql_engine():
    def __init__(self):
        self.username = "root"
        self.password = "0000"
        self.host = "localhost"
        self.port = "3306"
        self.database_name = "dmplat"
        self.engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database_name}')


    def get_data_to_df(self, sql:str):

        if sql.split(" ")[0].upper() != "SELECT":
            print("error, only can select datafrom db")
            return None
        try:
            with self.engine.engine.connect() as con, con.begin():
                df = pd.read_sql(sql, con)
            con.close()
        except Exception as e:
            print(e)
            df = None
        return df

    def execute_sql(self, sql:str):

        if sql.split(" ")[0].upper() not in ["UPDATE", "INSERT", "DELETE"]:
            print("error")
            return None

        try:
            with self.engine.engine.connect() as con, con.begin():
                con.execute(sql)
            con.close()

        except Exception as e:
            print(e)
            raise e


        return

if __name__ == '__main__':
    engine = mysql_engine()

    print(engine.get_data_to_df("SELECT user_name FROM dmplat.user;"))

    print(engine.execute_sql("UPDATE user SET user_name='Leon' WHERE user_id=1;"))

    print(engine.get_data_to_df("SELECT user_name FROM dmplat.user;"))