
from flask import Blueprint, request, render_template

from access import role_required
from report.model import find_date, count_report, create_report, button_date, select_report

report_Blueprint = Blueprint(
    'report_bp',
    __name__,
    template_folder= 'templates'
)

@report_Blueprint.route('/check', methods = ['GET', 'POST'])
@role_required
def check_handler():
    if request.method == 'GET':
        res = button_date()
        return render_template('find_report.html',
                               data = res
                               )
    else:
        data = select_report(request.form.get('year'), request.form.get('month'))
        return render_template('report.html', data = data)

@report_Blueprint.route('/create', methods = ['GET', 'POST'])
@role_required
def create_handler():
    if request.method == 'GET':
        year, month = find_date()
        return  render_template('create_report.html',
                                 year = year,
                                 months = month
                                )
    else:
        year = request.form.get('year')
        month = request.form.get('month')
        if count_report(year, month) is None:
            create_report(year, month)
            message = "отчёт создан"
        else:
            message = "отчёт уже существует"
        return render_template('result.html', message = message)