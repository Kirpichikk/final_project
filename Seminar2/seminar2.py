
from flask import Flask, render_template, request, session, redirect
from connection import DBConnection
from auth.route import auth_Blueprint
from access import login_required

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

@application.route('/static')
def static_handler():
    return render_template('index.html')

@application.route('/dynamic')
def dynamic_handler():
    # fetch from database
    languages=['C', 'C++', 'Go', 'JavaScript', 'Python']
    return render_template('dynamic.html',
                           languages=languages
                           )

@application.route('/form', methods=['GET', 'POST'])
def init_handler():
    if request.method == 'GET':
        return render_template('product_form.html')
    elif request.method == 'POST':
        name = request.form['product_name']
        sql = f'select * from doctor where id_doctor="{name}"'
        with DBConnection(db_config) as cursor:
            cursor.execute(sql)
            schema = [column[0] for column in cursor.description]
            result = [dict(zip(schema, row)) for row in cursor.fetchall()]

        render_data= {
            'status': True if result else False,
            'data': result
        }
        return render_template('database_output.html',
                               render_data=render_data
                               )

@application.route('/logout')
def logout_handler():
    session.clear()
    return redirect('/')

@application.route('/')
@login_required
def hello_handler():
        return 'Hello world'

if __name__ == '__main__':
    application.run(host='127.0.0.1', port=5000)