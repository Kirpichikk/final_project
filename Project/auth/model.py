from base64 import b64encode

from connection import DBConnection
from interaction_with_bd import find_user_in_db
from sql_provider import SqlProvider
from flask import current_app, session
import os

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

def authorization (login, password):
    sql_statement = provider.get(
        'find_internal_user.sql',
        {'login': login, 'password': password}
    )
    return find_user_in_db(current_app.config['db_config'], sql_statement)

def create_basic_auth_token(login, password):
    credentials_b64 = b64encode(f'{login}:{password}'.encode('ascii')).decode('ascii')
    token = f'Basic {credentials_b64}'
    return token

def create_session_internal(args):
    session['role'] = args['role']
    session['id_inside'] = args['id_inside']
    session['doctor_name'] = args['doctor_name']
    session['specialization'] = args['specialization']
    session['name_department'] = args['name_department']
    session.permanent = True
    return

def create_session_external(id, config):
    session['id_inside'] = id
    current_app.config['db_config']['user'] = "patient"
    current_app.config['db_config']['password'] = config
    session.permanent = True
    return