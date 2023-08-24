from flask import render_template, redirect, request, url_for, flash, abort
from flask_cors import CORS

from apiproject.routes import SelfHeathDataRoutes
from apiproject.service import SelfHeathDataService
from apiproject import app


app.register_blueprint(SelfHeathDataRoutes.selfHeathData)

@app.route('/')
def home():
    return "Wellcome to  DM API."

if __name__ == '__main__':
    app.run(debug=True, port="8016")