from base64 import b64encode

from connection import DBConnection
from sql_provider import SqlProvider
from flask import current_app
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