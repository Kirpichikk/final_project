
from flask import Flask, session, redirect

from access import login_required
from auth.route import auth_Blueprint
from request.request_manager import request_Blueprint

db_config = {
    'host' : '127.0.0.1',
    'port' : 3306,
    'user' : 'root',
    'password' : 'Aniretake105',
    'db' : 'new_schema'
}

application=Flask(__name__) #создание точки входа __name__-ссылка на имя файла

application.secret_key = "my_secret_key"
application.register_blueprint(auth_Blueprint, url_prefix = '/auth')
application.register_blueprint(request_Blueprint, url_prefix = '/request')

@application.route('/logout')
def logout_handler():
    session.clear()
    return redirect('/auth/')

@application.route('/')
@login_required
def init_handler():
    return redirect('/request/')

if __name__ == '__main__':
    application.run(host='127.0.0.1', port=5000)