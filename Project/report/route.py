import calendar

from flask import Blueprint, request, render_template
from pyexpat.errors import messages

from access import role_required
from report.model import find_date, count_report, create_report, button_patient, button_visits, button_doctor, \
    select_report_for_patient, select_report_for_visits, select_report_for_doctor, find_date_doctor, find_date_patient, \
    count_report_visits, count_report_doctor, bool_dates, bool_dates_doctor, create_report_for_some_action, \
    find_report_for_some_action

report_Blueprint = Blueprint(
    'report_bp',
    __name__,
    template_folder= 'templates'
)

@report_Blueprint.app_template_filter('month_name')
def month_name(month_number):
    return calendar.month_name[month_number]

@report_Blueprint.route('/check', methods = ['GET','POST'])
@role_required
def check_handler():
    if request.method == 'GET':
        return  render_template('choice.html')
    else:
        action = request.form.get('action')
        res, message = find_report_for_some_action(action)
        return render_template('find_report.html', data=res, action=action, message=message)

@report_Blueprint.route('/result', methods=['POST'])
@role_required
def result_handler():
    action = request.form.get('action')
    if action == 'patient':
        res = select_report_for_patient(request.form.get('year'))
        return render_template('report_patient.html',data = res, action = action)
    elif action == 'visits':
        res = select_report_for_visits(request.form.get('year'), request.form.get('month'))
        return render_template('report_visits.html',data = res, action = action)
    else:
        res = select_report_for_doctor(request.form.get('year'), request.form.get('month'))
        return render_template('report_doctor.html',data = res, action = action)

@report_Blueprint.route('/create', methods = ['GET', 'POST'])
@role_required
def create_handler():
    if request.method == 'GET':
        return  render_template('choice.html')
    else:
        if len(request.form) == 1:
            action = request.form.get('action')
            if action == 'patient':
                year = find_date_patient()
                return render_template('create_report.html', year = year, action=action)
            elif action == 'visits':
                year, month = find_date()
                return render_template('create_report.html', year=year, months=month, action=action)
            else:
                year, month = find_date_doctor()
                return render_template('create_report.html', year=year, months=month, action=action)
        else:
            year = request.form.get('year')
            action = request.form.get('action')
            month = request.form.get('month', '')
            message = create_report_for_some_action(year, month, action)

            return render_template('result_report.html', message=message, action=action)