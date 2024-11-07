import os
from flask import current_app
from connection import DBConnection
from sql_provider import SqlProvider

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

def find_data_with_description_in_db(db_config, sql):
    with DBConnection(db_config) as cursor:
        if cursor.execute(sql) is None:
            return None
        else:
            schema = [column[0] for column in cursor.description]
            result = [dict(zip(schema, row)) for row in cursor.fetchall()]
            return result

def find_data_in_db(db_config, sql):
    with DBConnection(db_config) as cursor:
        if cursor.execute(sql) is None:
            return None
        else:
            result = [row for row in cursor.fetchall()]
            if len(result) == 0:
                return None
            else:
                return result

def find_names():
    with open('request/sql/find_names.sql', 'r') as file:
        sql_script = file.read()
    result = find_data_in_db(current_app.config['db_config'], sql_script)
    return result

def find_time(id_doctor, rec_date):
    sql_statement = provider.get(
        'find_time.sql',
        {
            'id_doctor': id_doctor,
            'rec_date': rec_date
        }
    )
    result = find_data_in_db(current_app.config['db_config'], sql_statement)
    return result

def find_floor(number):
    sql_statement = provider.get(
        'find_floor.sql',
        {
            'number': number
        }
    )
    result = find_data_in_db(current_app.config['db_config'], sql_statement)
    return result

def find_specialization():
    with open('request/sql/find_specialization_list.sql', 'r') as file:
        sql_script = file.read()
    result = find_data_in_db(current_app.config['db_config'], sql_script)
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

    result = find_data_in_db(current_app.config['db_config'], sql_statement)
    return result