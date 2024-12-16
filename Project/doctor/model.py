from datetime import datetime
import os
from flask import current_app, session
from interaction_with_bd import find_data_in_db, update_data_in_db
from sql_provider import SqlProvider

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

def insert_reception_notes(request_data):
    sql_statement = provider.get(
        'add_note.sql',
        {
            'date': datetime.strftime(datetime.now(), "%Y-%m-%d"),
            'diagnosis': request_data.get('diagnosis'),
            'complains': request_data.get('complains'),
            'appointment': request_data.get('appointment'),
            'id_patient': find_patient(request_data.get('id_schedule'))['id_visit_card'],
            'id_doctor': session['id_inside']
        }
    )
    change_app_mark(request_data.get('id_schedule'))
    update_data_in_db(current_app.config['db_config'], sql_statement)

def find_patient(id_schedule):
    sql_statement = provider.get(
        'find_patient.sql',
        {
            'id_shedule': id_schedule
        }
    )
    result = find_data_in_db(current_app.config['db_config'], sql_statement)
    return result[0]

def change_app_mark(id_schedule):
    sql_statement = provider.get(
        'change_app_mark.sql',
        {
            'id_shedule': id_schedule
        }
    )
    update_data_in_db(current_app.config['db_config'], sql_statement)