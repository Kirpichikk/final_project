from flask import Blueprint, request, render_template, url_for, redirect

from access import role_required
from request.request_model import find_names, find_time, find_floor, find_specialization, find_doctors, filter_date, \
    find_name_doctor, find_patient, create_note

request_Blueprint = Blueprint(
    'request_bp',
    __name__,
    template_folder= 'templates'
)

@request_Blueprint.route('/findFreeTime', methods=['GET', 'POST'])
@role_required
def time_handler():
    if request.method == 'GET':
        names = find_names()
        max_date, min_date = filter_date()
        return render_template('form.html',
                               request = 'time',
                               names = names,
                               max = max_date[0],
                               min = min_date
                               )
    else:
        result = find_time(
            request.form.get('names'),
            request.form.get('date')
        )
        state = False if result is None else True

        return render_template('output.html',
                               data = result,
                               boolValue = state,
                               request='time',
                               Name = request.form.get('names'),
                               Date = request.form.get('date')
                               )

@request_Blueprint.route('/createNote', methods=['POST'])
@role_required
def user_handler():
    doctor = find_name_doctor(request.form.get('name'))
    doctor_id = request.form.get('name')
    date = request.form.get('date')
    time = request.form.get('time')
    patient = request.form.get('id_patient', '')
    if patient == '':
        return render_template('choice_user.html',
                               name = doctor,
                               date = date,
                               time = time,
                               id = doctor_id
        )
    else:
        find = find_patient(patient)
        if find:
            create_note(patient,doctor_id,date,time)
            return(redirect(url_for('privateOffice_bp.main_office_handler')))
        else:
            return render_template('choice_user.html',
                                   name=doctor,
                                   date=date,
                                   time=time,
                                   id=doctor_id,
                                   error = True
            )

@request_Blueprint.route('/findFloor', methods=['GET', 'POST'])
@role_required
def floor_handler():
    if request.method == 'GET':
        return render_template('form.html', request = 'floor')
    else:
        result = find_floor(request.form.get('num'))
        state = False if result is None else True

        return render_template('output.html',
                               data=result,
                               boolValue=state,
                               request='floor'
                               )

@request_Blueprint.route('/findSpecialization', methods=['GET', 'POST'])
@role_required
def specialization_handler():
    if request.method == 'GET':
        specialization = find_specialization()
        return render_template('form.html',
                               request = 'specialization',
                               names = specialization
                               )
    else:
        result = find_doctors(request.form.get('names'))

        return render_template('output.html',
                               data=result,
                               request='specialization'
                               )