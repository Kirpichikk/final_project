from sched import scheduler

from flask import Blueprint, render_template, session

from private_office.model import private_data, shedule

privateOffice_Blueprint = Blueprint(
    'privateOffice_bp',
    __name__,
    template_folder= 'templates'
)

@privateOffice_Blueprint.route('/')
def main_office_handler():
    if session['role'] == 'doctor':
        schedule = shedule(session['id_inside'])
        print(schedule)
        data = private_data(session['id_inside'])

    return render_template('private_office.html',
                           data = data[0],
                           unique_data = schedule,
                           role = session['role']
                           )
