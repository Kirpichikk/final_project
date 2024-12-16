import requests
from flask import Blueprint, request, render_template, redirect, url_for
from auth.model import authorization, create_session_internal, create_session_external, create_token

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
        is_internal = True if request.form.get('is_internal') == 'on' else False
        if not is_internal:
            data = create_token(request.form)
            if data['status'] == 200:
                create_session_external(data['user'])
                return redirect(url_for('patient_bp.main_office_handler'))
        else:
            user = authorization(request.form)
            if user:
                create_session_internal(user)
                return redirect(url_for('privateOffice_bp.main_office_handler'))

        return render_template('auth_login.html', wrong = True)