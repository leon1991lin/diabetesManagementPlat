from flask import render_template, redirect, request, url_for, flash, abort
from flask_cors import CORS

from apiproject.routes import SelfHealthDataRoutes, UserRoutes, BasicInfoRoutes, PatientMedicalRecordsRoutes
<<<<<<< HEAD
=======
from apiproject.service import SelfHealthDataService
>>>>>>> 38669ad1fa8a111210b152a746a8b52b81ea700d
from apiproject import app

app.register_blueprint(SelfHealthDataRoutes.selfHealthData)
app.register_blueprint(UserRoutes.user)
app.register_blueprint(BasicInfoRoutes.basicInfo)
app.register_blueprint(PatientMedicalRecordsRoutes.medicalRecords)

@app.route('/')
def home():
    '''
    file: routes/swagger/testPage.yml
    '''
    return "Wellcome to  DM API."

if __name__ == '__main__':
    app.run(debug=True, port="8016")