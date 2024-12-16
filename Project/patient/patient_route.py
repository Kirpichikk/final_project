from flask import Blueprint, session, render_template, request
import locale
from patient.patient_model import get_personal_data, get_previous_visits, find_specialization, find_doctors, \
    find_timetable, checking_data, change_shedule

locale.setlocale(locale.LC_TIME, 'Russian_Russia.1251')
patient_Blueprint = Blueprint(
    'patient_bp',
    __name__,
    template_folder= 'templates'
)

@patient_Blueprint.route('/')
def main_office_handler():
    result = get_personal_data(session['id_inside'])
    visits = get_previous_visits(session['id_inside'])
    return render_template('main_office.html',
                           data = result,
                           visits = visits
                           )

@patient_Blueprint.route('/specialization')
def specialization_handler():
    data = find_specialization()
    return render_template('specialization.html',
                           data = data
                           )

@patient_Blueprint.route('/doctor_date', methods = ['GET', 'POST'])
def doctor_handler():
    subdata = find_timetable(find_doctors(request.form.get('specialization')))
    return render_template('timetable.html',
                           doctors=[i for i in subdata],
                           timetable=subdata,
                           )

@patient_Blueprint.route('/confirmation', methods = ['GET', 'POST'])
def confirmation_handler():
    if request.form.get('confim', '')== '':
        data_from_bd = checking_data(request.form.get('id_shedule'))
        return render_template('confirmation.html',
                               data = data_from_bd[0],
                               person = session
                               )
    else:
        change_shedule(session['id_inside'], request.form.get('id'))
        return render_template('result.html')
