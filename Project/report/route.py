
from flask import Blueprint, request, render_template
from pyexpat.errors import messages

from access import role_required
from report.model import find_date, count_report, create_report, button_patient, button_visits, button_doctor, \
    select_report_for_patient, select_report_for_visits, select_report_for_doctor, find_date_doctor, find_date_patient, \
    count_report_visits, count_report_doctor

report_Blueprint = Blueprint(
    'report_bp',
    __name__,
    template_folder= 'templates'
)

@report_Blueprint.route('/check', methods = ['GET','POST'])
@role_required
def check_handler():
    if request.method == 'GET':
        return  render_template('choice.html')
    else:
        action = request.form.get('action')
        if action == 'patient':
            res = button_patient()
            message = True if res is None else False
            return render_template('find_report.html',data = res, action = action, message = message)
        elif action == 'visits':
            res = button_visits()
            message = True if res is None else False
            return render_template('find_report.html',data = res, action = action, message = message)
        else:
            res = button_doctor()
            message = True if res is None else False
            return render_template('find_report.html',data = res, action = action, message = message)

@report_Blueprint.route('/result', methods=['POST'])
def result_handler():
    action = request.form.get('action')
    if action == 'patient':
        res = select_report_for_patient(request.form.get('year'))
        return render_template('report_patient.html',data = res, action = action)
    elif action == 'visits':
        print(request.form.get('year'), request.form.get('month'))
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
            if action != "patient": month = request.form.get('month')
            if action == 'patient':
                if count_report(year) is None:
                    create_report('report_1', year)
                    message = "отчёт создан"
                else:
                    message = "отчёт уже существует"
                return render_template('result_report.html', message=message, action = action)
            elif action == 'visits':
                if count_report_visits(year, month) is None:
                    create_report('report_2', year, month)
                    message = "отчёт создан"
                else:
                    message = "отчёт уже существует"
                return render_template('result_report.html', message=message, action = action)
            else:
                if count_report_doctor(year, month) is None:
                    create_report('report_3', year, month)
                    message = "отчёт создан"
                else:
                    message = "отчёт уже существует"
                return render_template('result_report.html', message=message, action = action)