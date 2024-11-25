from flask import session, redirect, url_for, request, current_app
from functools import wraps



def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'role' in session:
            return func(*args, **kwargs)
        return redirect(url_for('auth_bp.login_handler'))
    return wrapper

def role_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'role' in session:
            user_role = session.get('role')
            user_req = request.endpoint
            access = current_app.config['db_access']
            if user_role in access and user_req in access[user_role]:
                return func(*args, **kwargs)
            else:
                return redirect(url_for('privateOffice_bp.main_office_handler'))
        else:
            return redirect(url_for('patient_bp.main_office_handler'))
    return wrapper