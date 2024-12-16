from datetime import datetime
from dateutil.relativedelta import relativedelta
from flask import Blueprint, render_template, url_for, redirect, request
from access import role_required
from schedule.model import find_start_schedule, create_name_id, find_names, \
    create_office_doctor, add_data_in_cache, edit_data_in_cache, del_data_in_cache, finish_operations

schedule_Blueprint = Blueprint(
    'schedule_bp',
    __name__,
    template_folder= 'templates'
)

@schedule_Blueprint.route('/')
@role_required
def init_handler():
    param = request.args.get('start', '')
    global start
    global names
    if param != 'again':
        start = find_start_schedule()
        create_name_id()
        create_office_doctor()
        names = find_names()
    minn = datetime.now().date().isoformat()
    maxx = (datetime.now() + relativedelta(months=1)).date().isoformat()
    return render_template('start_page.html', data=start, names=names, min=minn, max=maxx)

@schedule_Blueprint.route('/add', methods=['GET', 'POST'])
@role_required
def add_handler():
    global start
    start = add_data_in_cache(start, request.form)
    return redirect(url_for('schedule_bp.init_handler', start='again'))

@schedule_Blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
@role_required
def edit_handler(id):
    global start
    start = edit_data_in_cache(start, request.form, id)
    return redirect(url_for('schedule_bp.init_handler', start='again'))

@schedule_Blueprint.route('/del/<int:id>', methods=['GET', 'POST'])
@role_required
def delete_handler(id):
    global start
    start = del_data_in_cache(id, start)
    return redirect(url_for('schedule_bp.init_handler', start='again'))

@schedule_Blueprint.route('/end')
@role_required
def end_handler():
    finish_operations()
    return redirect(url_for('privateOffice_bp.main_office_handler'))