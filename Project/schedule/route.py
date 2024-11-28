from datetime import datetime

from dateutil.relativedelta import relativedelta
from flask import Blueprint, render_template, url_for, redirect, request
from schedule.model import find_start_schedule, create_name_id, find_names, add_in_delete_cache, \
    create_office_doctor, get_from_name_id, get_from_office_id, change_edit_cache, change_local_table, \
    add_in_local_table, remove_local_data_to_bd, change_add_cache, delete_in_bd, add_in_bd, edit_in_bd

schedule_Blueprint = Blueprint(
    'schedule_bp',
    __name__,
    template_folder= 'templates'
)

@schedule_Blueprint.route('/')
def init_handler():
    param = request.args.get('start', '')
    global start
    global names
    if param != 'again':
        start = find_start_schedule()
        create_name_id()
        create_office_doctor()
        names = find_names()
        min = datetime.now().date().isoformat()
        max = (datetime.now() + relativedelta(months=1)).date().isoformat()
    return render_template('start_page.html', data=start, names=names, min=min, max=max)

@schedule_Blueprint.route('/add', methods=['POST'])
def add_handler():
    global start
    start = add_in_local_table(start, request.form.get('date'), request.form.get('time'), request.form.get('name'))

    id_doctor = get_from_name_id(request.form.get('name'))
    id_office = get_from_office_id(id_doctor)
    id = start[-1]['id_shedule']
    data = [id_office, request.form.get('date'), request.form.get('time'), id_doctor]
    change_add_cache(id,data)

    return redirect(url_for('schedule_bp.init_handler', start='again'))

@schedule_Blueprint.route('/edit/<int:id>', methods=['POST'])
def edit_handler(id):
    id_doctor = get_from_name_id(request.form.get('name'))
    id_office = get_from_office_id(id_doctor)
    data = [id_office, request.form.get('date'), request.form.get('time'), id_doctor]
    change_edit_cache(id, data)

    global start
    start = change_local_table(start, id, request.form.get('date'), request.form.get('time'), request.form.get('name'))

    return redirect(url_for('schedule_bp.init_handler', start='again'))

@schedule_Blueprint.route('/del/<int:id>', methods=['POST'])
def delete_handler(id):
    global start
    res = [i for i in start if i['id_shedule']!=id]
    start = res
    add_in_delete_cache(id)
    return redirect(url_for('schedule_bp.init_handler', start='again'))

@schedule_Blueprint.route('/end')
def end_handler():
    delete, edit, add = remove_local_data_to_bd()
    if delete:
        delete_in_bd(delete)

    if add:
        add_in_bd(add)

    if edit:
        edit_in_bd(edit)
    return redirect(url_for('privateOffice_bp.main_office_handler'))