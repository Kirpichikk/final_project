from flask import Blueprint, session

patient_Blueprint = Blueprint(
    'patient_bp',
    __name__,
    template_folder= 'templates'
)

@patient_Blueprint.route('/')
def main_office_handler():
    return session['id_inside']

@patient_Blueprint.route('/specialization')
def specialization_handler():
    pass

@patient_Blueprint.route('/doctor_date')
def doctor_handler():
    pass

@patient_Blueprint.route('/confirmation')
def confirmation_handler():
    pass