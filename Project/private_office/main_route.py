from flask import Blueprint, render_template, session, request

from private_office.main_model import private_data, shedule

privateOffice_Blueprint = Blueprint(
    'privateOffice_bp',
    __name__,
    template_folder= 'templates'
)

@privateOffice_Blueprint.route('/')
def main_office_handler():
    if session['role'] == 'doctor':
        schedule = shedule(session['id_inside'])
        data = private_data(session['id_inside'])

    return render_template('private_office.html',
                           data = data[0],
                           unique_data = schedule,
                           role = session['role']
                           )

@privateOffice_Blueprint.route('/reception', methods=['POST'])
def reception_handler():
    name = request.form['name']
    return render_template('reception.html',
                           name = name
                           )
