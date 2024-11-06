from flask import session, redirect, url_for

from functools import wraps

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'role_id' in session:
            return func(*args, **kwargs)
        return redirect(url_for('auth_bp.login_handler'))
    return wrapper