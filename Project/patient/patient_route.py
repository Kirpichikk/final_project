from flask import Blueprint

patient_Blueprint = Blueprint(
    'patient_bp',
    __name__,
    template_folder= 'templates'
)

@patient_Blueprint.route('/')
def main_office_handler():
    return "hello"