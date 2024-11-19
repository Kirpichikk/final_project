import os
from flask import current_app
from datetime import datetime
from connection import DBConnection
from sql_provider import SqlProvider

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

def update_data_in_db(db_config, sql):
    with DBConnection(db_config) as cursor:
        if cursor.execute(sql) is None:
            return None

def find_data_in_db(db_config, sql):
    with DBConnection(db_config) as cursor:
        if cursor.execute(sql) is None:
            return None
        else:
            schema = [column[0] for column in cursor.description]
            result = [dict(zip(schema, row)) for row in cursor.fetchall()]
            return result

def find_in_db(db_config, sql):
    with DBConnection(db_config) as cursor:
        if cursor.execute(sql) is None:
            return None
        else:
            result = [row for row in cursor.fetchall()]
            if len(result) == 0:
                return None
            else:
                return result

def get_personal_data(id_user):
    sql_statement = provider.get(
        'find_data_patient.sql',
        {
            'id': id_user
        }
    )
    result = find_data_in_db(current_app.config['db_config'], sql_statement)
    result[0]['birthday'] = datetime.strftime(result[0]['birthday'], "%d.%m.%Y")
    return result[0]

def get_previous_visits(id_user):
    sql_statement = provider.get(
        'previous_visits.sql',
        {
            'id': id_user
        }
    )
    result = find_in_db(current_app.config['db_config'], sql_statement)
    return result

def find_specialization():
    with open('patient/sql/find_specialization_list.sql', 'r') as file:
        sql_script = file.read()
    result = find_in_db(current_app.config['db_config'], sql_script)
    unique_result = list(set(result))
    sorted_result = sorted(unique_result)
    return sorted_result

def find_doctors(specialization):
    sql_statement = provider.get(
        'find_doctors.sql',
        {
            'specialization': specialization
        }
    )
    result = find_in_db(current_app.config['db_config'], sql_statement)
    return result

def find_timetable(list_doctor):
    result={}
    for id in list_doctor:
        sql_statement = provider.get(
            'find_timetable.sql',
            {
                'id': id[0]
            }
        )
        time = find_in_db(current_app.config['db_config'], sql_statement)
        if time is None:
            result[id[1]] = None
        else:
            result[id[1]] = time


    sorted_result = {}
    for i in result:
        sorted_result[i] = {}
        if result[i] != None:
            for j in result[i]:
                if j[0] not in sorted_result[i]:
                    sorted_result[i][j[0]] = [j[1:]]
                else:
                    sorted_result[i][j[0]].append(j[1:])

    for i in sorted_result:
        for j in sorted_result[i]:
            sorted_items = sorted_result[i][j]
            sorted_result[i][j] = sorted(sorted_items, key = lambda x: x[0])
        sorted_keys = sorted_result[i]
        sorted_result[i] = dict(sorted(sorted_keys.items()))
    sorted_result = dict(sorted(sorted_result.items()))

    return sorted_result

def checking_data(id_shedule):
    sql_statement = provider.get(
        'information_for_conf.sql',
        {
            'id': id_shedule
        }
    )
    result = find_data_in_db(current_app.config['db_config'], sql_statement)
    return result

def change_shedule(*data):
    sql_statement = provider.get(
        'change_shedule.sql',
        {
            'id_patient': data[0],
            'id_schedule': data[1]
        }
    )
    update_data_in_db(current_app.config['db_config'], sql_statement)