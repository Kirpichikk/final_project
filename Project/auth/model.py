from base64 import b64encode

import requests
from urllib3 import request

from connection import DBConnection
from interaction_with_bd import find_user_in_db
from sql_provider import SqlProvider
from flask import current_app, session, json
import os

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

def authorization (request_data):
    sql_statement = provider.get(
        'find_internal_user.sql',
        {'login': request_data.get('login', ''), 'password': request_data.get('password', '')}
    )
    return find_user_in_db(current_app.config['db_config'], sql_statement)

def create_token(request_data):
    login = request_data.get('login', '')
    password = request_data.get('password', '')
    credentials_b64 = b64encode(f'{login}:{password}'.encode('ascii')).decode('ascii')
    token = f'Basic {credentials_b64}'
    response = requests.get(
        f'http://127.0.0.1:5002/api/auth/find-user',
        headers={'Authorization': token}
    )
    return response.json()

def create_session_internal(args):
    session['role'] = args['role']
    session['id_inside'] = args['id_inside']
    session['doctor_name'] = args['doctor_name']
    session['specialization'] = args['specialization']
    session['name_department'] = args['name_department']
    session.permanent = True
    config = args['db_config']
    with open("db_config.json") as f:
        current_app.config['db_config'] = json.load(f)[config]
    return


def create_session_external(args):
    session['id_inside'] = args['id_inside']
    config = args['db_config']
    with open("db_config.json") as f:
        current_app.config['db_config'] = json.load(f)[config]
    session.permanent = True
    return

