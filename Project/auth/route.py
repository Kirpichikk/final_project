
from flask import Blueprint, request, render_template, session, redirect, url_for
from auth.model import authorization

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
        user = authorization(
            request.form.get('login', ''),
            request.form.get('password', '')
        )
        if user is None:
            return render_template('auth_login.html', wrong = True)
        else:
            print(user)
            session['role'] = user['role']
            session['id_inside'] = user['id_inside']
            session['doctor_name'] = user['doctor_name']
            session['specialization'] = user['specialization']
            session['name_department'] = user['name_department']
            print(session)
            session.permanent = True
            return redirect(url_for('privateOffice_bp.main_office_handler'))


