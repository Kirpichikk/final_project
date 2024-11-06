from flask import Blueprint, render_template, session, request, redirect, url_for

from private_office.main_model import private_data, shedule, change_app_mark, insert_reception_notes, find_patient

privateOffice_Blueprint = Blueprint(
    'privateOffice_bp',
    __name__,
    template_folder= 'templates'
)

@privateOffice_Blueprint.route('/')
def main_office_handler():

    info_data = private_data(session['id_inside'])
    if session['role'] == 'doctor':
        unique_data = shedule(session['id_inside'])
        if unique_data is None:
            unique_data = False

    elif session['role'] == 'register':
        unique_data = None

    return render_template('private_office.html',
                           data = info_data[0],
                           unique_data = unique_data,
                           role = session['role']
                           )

@privateOffice_Blueprint.route('/reception', methods=['POST'])
def reception_handler():
    if len(request.form) == 3:
        return render_template('reception.html',
                           data = request.form
                           )
    else:
        insert_reception_notes(
            request.form.get('diagnosis'),
            request.form.get('complains'),
            request.form.get('appointments'),
            find_patient(request.form.get('id_schedule'))['id_visit_card'],
            session['id_inside']
        )
        change_app_mark(request.form.get('id_schedule'))
        return redirect(url_for('privateOffice_bp.main_office_handler'))
