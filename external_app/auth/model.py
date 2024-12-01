import os
from base64 import b64decode

from flask import current_app

from database.sql_provider import SQLProvider
from database.operations import select_dict

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

def valid_authorization_request(api_request):
    auth_header = api_request.headers.get('Authorization', '')
    if not auth_header:
        return False
    if not auth_header.startswith('Basic '):
        return False
    if len(auth_header) <= len('Basic '):
        return False
    return True


def decode_basic_authorization(api_request):
    auth_header = api_request.headers.get('Authorization')
    token = auth_header.split()[-1]
    login_and_password = b64decode(token.encode('ascii')).decode('ascii').split(':')
    if len(login_and_password) != 2:
        raise ValueError('Invalid login and password format')
    login, password = login_and_password
    return login, password

def find_userr(login, password):
    sql = provider.get('user.sql', dict(login=login, password=password))
    return select_dict(current_app.config['db_config'], sql)