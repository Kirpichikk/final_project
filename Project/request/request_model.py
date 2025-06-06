import os
from flask import current_app
from connection import DBConnection
from interaction_with_bd import find_in_db, update_data_in_db
from sql_provider import SqlProvider
from datetime import datetime

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

def filter_date():
    with open('request/sql/find_max_date.sql', 'r') as file:
        sql_script = file.read()
    result = find_in_db(current_app.config['db_config'], sql_script)
    max_date = result[0]
    min_date = datetime.now().date().isoformat()
    return max_date, min_date

def find_names():
    with open('request/sql/find_names.sql', 'r') as file:
        sql_script = file.read()
    result = find_in_db(current_app.config['db_config'], sql_script)
    return result

def find_time(id_doctor, rec_date):
    sql_statement = provider.get(
        'find_time.sql',
        {
            'id_doctor': id_doctor,
            'rec_date': rec_date
        }
    )
    result = find_in_db(current_app.config['db_config'], sql_statement)
    return result

def find_floor(number):
    sql_statement = provider.get(
        'find_floor.sql',
        {
            'number': number
        }
    )
    result = find_in_db(current_app.config['db_config'], sql_statement)
    return result

def find_specialization():
    with open('request/sql/find_specialization_list.sql', 'r') as file:
        sql_script = file.read()
    result = find_in_db(current_app.config['db_config'], sql_script)
    unique_result = list(set(result))
    sorted_result = sorted(unique_result)
    return sorted_result

def find_doctors(name):
    sql_statement = provider.get(
        'find_specialization.sql',
        {
            'specialization': name
        }
    )

    result = find_in_db(current_app.config['db_config'], sql_statement)
    return result

def find_name_doctor(id):
    sql_statement = provider.get(
        'find_name.sql',
        {
            'id': id
        }
    )
    result = find_in_db(current_app.config['db_config'], sql_statement)
    return result

def find_patient(id):
    sql_statement = provider.get(
        'find_patient.sql',
        {
            'id': id
        }
    )
    result = find_in_db(current_app.config['db_config'], sql_statement)
    return result

def create_note(patient, name, date, time):
    sql_statement = provider.get(
        'create_note.sql',
        {
            'patient': patient,
            'date': date,
            'time': time,
            'id': name
        }
    )
    update_data_in_db(current_app.config['db_config'], sql_statement)

def get_from_request(request_data):
    doctor = find_name_doctor(request_data.get('name'))
    doctor_id = request_data.get('name')
    date = request_data.get('date')
    time = request_data.get('time')
    patient = request_data.get('id_patient', '')
    return doctor, doctor_id, date, time, patient