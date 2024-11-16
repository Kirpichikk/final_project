from flask import session, redirect, url_for

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
        if session['id_inside'] == 'register':
            return func(*args, **kwargs)
        return redirect(url_for('privateOffice_bp.main_office_handler'))
    return wrapper