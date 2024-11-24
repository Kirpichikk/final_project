from connection import DBConnection, db_config
from sql_provider import SqlProvider
from flask import current_app
import os

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

def call_proc(db_config, proc_name, *args):
    with DBConnection(db_config) as cursor:
        if cursor is None:
            return None
        param_list = []
        for arg in args:
            param_list.append(arg)
        res = cursor.callproc(proc_name, param_list)
    return res

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

def find_data_in_db(db_config, sql):
    with DBConnection(db_config) as cursor:
        if cursor.execute(sql) is None:
            return None
        else:
            schema = [column[0] for column in cursor.description]
            result = [dict(zip(schema, row)) for row in cursor.fetchall()]
            return result

def create_report(year, month):
    call_proc(current_app.config['db_config'], 'report', year, month)
    return

def find_date():
    with open('report/sql/find_dates.sql', 'r') as file:
        sql_script = file.read()
    result = find_data_in_db(current_app.config['db_config'], sql_script)
    years = [i['year'] for i in result]
    unique_years = sorted(list(set(years)))
    month = [i['month'] for i in result]
    return unique_years, month

def count_report(year, month):
    sql_statement = provider.get(
        'count_reports.sql',
        {'year': year, 'month': month}
    )
    return find_in_db(current_app.config['db_config'], sql_statement)

def button_date():
    with open('report/sql/find_dates_for_buttons.sql', 'r') as file:
        sql_script = file.read()
    result = find_data_in_db(current_app.config['db_config'], sql_script)
    return result

def select_report(year, month):
    sql_statement = provider.get(
        'select_report.sql',
        {'year': year, 'month': month}
    )
    return find_data_in_db(current_app.config['db_config'], sql_statement)