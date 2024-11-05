from datetime import datetime
from connection import DBConnection
from sql_provider import SqlProvider
from flask import current_app, session
import os

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

def find_data_in_db(db_config, sql):
    with DBConnection(db_config) as cursor:
        if cursor.execute(sql) is None:
            return None
        else:
            schema = [column[0] for column in cursor.description]
            result = [dict(zip(schema, row)) for row in cursor.fetchall()]
            return result

def private_data (id_doctor):
    sql_statement = provider.get(
        'information.sql',
        {'id_doctor': id_doctor}
    )
    result = find_data_in_db(current_app.config['db_config'], sql_statement)
    return result

def shedule(id_doctor):
    sql_statement = provider.get(
        'schedule_for_today.sql',
        {
            'date': datetime.strftime(datetime.now(), "%Y-%m-%d"),
            'id_doctor': id_doctor
        }
    )
    result = find_data_in_db(current_app.config['db_config'], sql_statement)
    sorted_result = sorted(result, key = lambda x: x['rec_time'])
    return sorted_result