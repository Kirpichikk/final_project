from datetime import datetime
import os
from flask import current_app
from interaction_with_bd import find_data_in_db, update_data_in_db
from sql_provider import SqlProvider

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

def insert_reception_notes(diagnosis, complains, appointment, id_patient, id_doctor):
    sql_statement = provider.get(
        'add_note.sql',
        {
            'date': datetime.strftime(datetime.now(), "%Y-%m-%d"),
            'diagnosis': diagnosis,
            'complains': complains,
            'appointment': appointment,
            'id_patient': id_patient,
            'id_doctor': id_doctor
        }
    )
    return update_data_in_db(current_app.config['db_config'], sql_statement)

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