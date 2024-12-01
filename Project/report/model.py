from connection import DBConnection
from interaction_with_bd import find_data_in_db, find_in_db, call_proc
from sql_provider import SqlProvider
from flask import current_app
import os

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

def create_report(name_report, *args):
    call_proc(current_app.config['db_config'], name_report, *args)
    return

def find_date():
    with open('report/sql/find_dates.sql', 'r') as file:
        sql_script = file.read()
    result = find_data_in_db(current_app.config['db_config'], sql_script)
    years = [i['year'] for i in result]
    unique_years = sorted(list(set(years)))
    month = [i['month'] for i in result]
    return unique_years, month

def find_date_doctor():
    with open('report/sql/find_dates_doctors.sql', 'r') as file:
        sql_script = file.read()
    result = find_data_in_db(current_app.config['db_config'], sql_script)
    years = [i['year'] for i in result]
    unique_years = sorted(list(set(years)))
    month = [i['month'] for i in result]
    return unique_years, month

def find_date_patient():
    with open('report/sql/find_dates_patient.sql', 'r') as file:
        sql_script = file.read()
    result = find_data_in_db(current_app.config['db_config'], sql_script)
    years = [i['year'] for i in result]
    unique_years = sorted(list(set(years)))
    return unique_years

def count_report(year):
    sql_statement = provider.get(
        'count_reports.sql',
        {'year': year}
    )
    return find_in_db(current_app.config['db_config'], sql_statement)

def count_report_doctor(year, month):
    sql_statement = provider.get(
        'count_reports_doctor.sql',
        {'year': year, 'month': month}
    )
    return find_in_db(current_app.config['db_config'], sql_statement)

def count_report_visits(year, month):
    sql_statement = provider.get(
        'count_reports_visits.sql',
        {'year': year, 'month': month}
    )
    return find_in_db(current_app.config['db_config'], sql_statement)

def button_visits():
    with open('report/sql/find_dates_for_visits.sql', 'r') as file:
        sql_script = file.read()
    result = find_data_in_db(current_app.config['db_config'], sql_script)
    return result

def button_patient():
    with open('report/sql/find_dates_for_patient.sql', 'r') as file:
        sql_script = file.read()
    result = find_data_in_db(current_app.config['db_config'], sql_script)
    return result

def button_doctor():
    with open('report/sql/find_dates_for_doctor.sql', 'r') as file:
        sql_script = file.read()
    result = find_data_in_db(current_app.config['db_config'], sql_script)
    return result

def select_report_for_patient(year):
    sql_statement = provider.get(
        'select_report_patient.sql',
        {'year': year}
    )
    return find_data_in_db(current_app.config['db_config'], sql_statement)

def select_report_for_visits(year, month):
    sql_statement = provider.get(
        'select_report_visits.sql',
        {'year': year, 'month': month}
    )
    return find_data_in_db(current_app.config['db_config'], sql_statement)

def select_report_for_doctor(year, month):
    sql_statement = provider.get(
        'select_report_doctor.sql',
        {'year': year, 'month': month}
    )
    return find_data_in_db(current_app.config['db_config'], sql_statement)