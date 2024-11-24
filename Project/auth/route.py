import requests
from flask import Blueprint, request, render_template, session, redirect, url_for, current_app

from access import role_required
from auth.model import authorization, create_basic_auth_token

auth_Blueprint = Blueprint(
    'auth_bp',
    __name__,
    template_folder= 'templates'
)

@auth_Blueprint.route('/', methods = ['GET', 'POST'])
def login_handler():
    if request.method == 'GET':
        return render_template('auth_login.html')
    else:
        login = request.form.get('login', '')
        password = request.form.get('password', '')

        is_internal = True if request.form.get('is_internal') == 'on' else False

        if not is_internal:
            # make external API call
            response = requests.get(
                f'http://127.0.0.1:5002/api/auth/find-user',
                headers={'Authorization': create_basic_auth_token(login, password)}
            )

            resp_json = response.json()
            if resp_json['status'] == 200:
                id_user =  resp_json['user']
                session['id_inside'] = id_user['id_inside']
                current_app.config['db_config']['user'] = "patient"
                current_app.config['db_config']['password'] = id_user['db_config']
                session.permanent = True
                return redirect(url_for('patient_bp.main_office_handler'))
        else:
            # find internal user
            user = authorization(login, password)
            if user:
                session['role'] = user['role']
                session['id_inside'] = user['id_inside']
                session['doctor_name'] = user['doctor_name']
                session['specialization'] = user['specialization']
                session['name_department'] = user['name_department']
                session.permanent = True
                return redirect(url_for('privateOffice_bp.main_office_handler'))

        return render_template('auth_login.html', wrong = True)



