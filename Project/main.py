from flask import Flask, session, json, url_for, redirect

from doctor.route import doctor_Blueprint
from patient.patient_route import patient_Blueprint
from private_office.main_route import privateOffice_Blueprint
from report.route import report_Blueprint
from request.request_manager import request_Blueprint
from access import login_required
from auth.route import auth_Blueprint

application=Flask(__name__) #создание точки входа __name__-ссылка на имя файла

with open("db_config.json") as f:
    application.config['db_config']= json.load(f)
with open("role_access.json") as f:
    application.config['db_access']= json.load(f)

application.secret_key = "my_secret_key"
application.register_blueprint(auth_Blueprint, url_prefix = '/auth')
application.register_blueprint(request_Blueprint, url_prefix = '/request')
application.register_blueprint(privateOffice_Blueprint, url_prefix = '/cabinet')
application.register_blueprint(patient_Blueprint, url_prefix = '/patient_office')
application.register_blueprint(doctor_Blueprint, url_prefix = '/reception')
application.register_blueprint(report_Blueprint, url_prefix = '/report')


@application.route('/logout')
def logout_handler():
    with open("db_config.json") as f:
        application.config['db_config'] = json.load(f)
    session.clear()
    return "вы вышли из системы"

@application.route('/')
@login_required
def init_handler():
    return redirect(url_for('privateOffice_bp.main_office_handler' if session.get('role') else 'patient_bp.main_office_handler'))

if __name__ == '__main__':
    application.run(host='127.0.0.1', port=5000)