from flask import Blueprint, session, render_template, request

from patient.patient_model import get_personal_data, get_previous_visits, find_specialization, find_doctors, \
    find_timetable

patient_Blueprint = Blueprint(
    'patient_bp',
    __name__,
    template_folder= 'templates'
)

@patient_Blueprint.route('/')
def main_office_handler():
    result = get_personal_data(session['id_inside'])
    visits = get_previous_visits(session['id_inside'])
    print(visits)
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

@patient_Blueprint.route('/doctor_date', methods = ['GET','POST'])
def doctor_handler():
    category = request.form.get('category', '')
    subcategory = request.form.get('subcategory', '')
    subdata = find_timetable(find_doctors(request.form.get('specialization')))
    data = [i for i in subdata]
    return render_template('timetable.html',
                           categories=data,
                           subcategories=subdata,
                           category=category,
                           subcategory=subcategory
                           )

@patient_Blueprint.route('/confirmation')
def confirmation_handler():
    pass