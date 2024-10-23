from flask import Blueprint, request, render_template, session ,redirect
from connection import DBConnection
from sql_provider import SqlProvider
import os

db_config = {
    'host' : '127.0.0.1',
    'port' : 3306,
    'user' : 'root',
    'password' : 'Aniretake105',
    'db' : 'supermarket'
}

auth_Blueprint = Blueprint(
    'auth_bp',
    __name__,
    template_folder= 'templates'
)

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

@auth_Blueprint.route('/', methods = ['GET', 'POST'])
def login_handler():
    if request.method == 'GET':
        return render_template('auth_login.html')
    else:
        login = request.form.get('login', '')
        password = request.form.get('password', '')
        sql_statement = provider.get(
            'find_internal_user.sql',
            {'login': login, 'password': password}
        )
        user = find_user_in_db(db_config, sql_statement)
        if user is None:
            return render_template('auth_login.html', wrong = True)
        else:
            session['user_id'] = user['user_id']
            session['user_group'] = user['user_group']
            session.permanent = True
            return redirect('/request/')

def find_user_in_db(db_config, sql):
    with DBConnection(db_config) as cursor:
        if cursor.execute(sql) is None:
            return None
        else:
            schema = [column[0] for column in cursor.description]
            for row in cursor.fetchall():
                result = dict(zip(schema, row))
            return result