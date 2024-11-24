from flask import Blueprint, render_template, session

from access import role_required
from private_office.main_model import shedule
privateOffice_Blueprint = Blueprint(
    'privateOffice_bp',
    __name__,
    template_folder= 'templates'
)

@privateOffice_Blueprint.route('/')
@role_required
def main_office_handler():

    info_data = [session['doctor_name'], session['specialization'], session['name_department']]
    if session['role'] == 'doctor':
        unique_data = shedule(session['id_inside'])
        if unique_data is None:
            unique_data = False
        return render_template('doctor.html',
                               data = info_data,
                               unique_data = unique_data
                               )

    elif session['role'] == 'register':
        return render_template('register.html',
                                   data = info_data
                                   )
    elif session['role'] == 'supremedoctor':
        return render_template('supremedoctor.html',
                               data=info_data
                               )
    elif session['role'] == 'admin':
        print(session['role'])
        return render_template('admin.html',
                               data=info_data
                               )

