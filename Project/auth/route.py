import requests
from flask import Blueprint, request, render_template, redirect, url_for
from auth.model import authorization, create_basic_auth_token, create_session_internal, create_session_external

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
                create_session_external(id_user['id_inside'], id_user['db_config'])
                return redirect(url_for('patient_bp.main_office_handler'))
        else:
            # find internal user
            user = authorization(login, password)
            if user:
                create_session_internal(user['role'],
                                        user['id_inside'],
                                        user['doctor_name'],
                                        user['specialization'],
                                        user['name_department']
                                        )
                return redirect(url_for('privateOffice_bp.main_office_handler'))

        return render_template('auth_login.html', wrong = True)



