from datetime import datetime
from interaction_with_bd import find_data_in_db
from sql_provider import SqlProvider
from flask import current_app
import os

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

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


