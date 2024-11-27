from base64 import b64encode

from connection import DBConnection
from sql_provider import SqlProvider
from flask import current_app, session
import os

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

def find_user_in_db(db_config, sql):
    with DBConnection(db_config) as cursor:
        if cursor.execute(sql) is None:
            return None
        else:
            schema = [column[0] for column in cursor.description]
            for row in cursor.fetchall():
                result = dict(zip(schema, row))
            return result

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

def create_session_internal(role, id, name, spec, dep):
    session['role'] = role
    session['id_inside'] = id
    session['doctor_name'] = name
    session['specialization'] = spec
    session['name_department'] = dep
    session.permanent = True
    return

def create_session_external(id, config):
    session['id_inside'] = id
    current_app.config['db_config']['user'] = "patient"
    current_app.config['db_config']['password'] = config
    session.permanent = True
    return