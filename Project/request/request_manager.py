from flask import Blueprint, request, render_template
from request.request_model import find_names, find_time, find_floor, find_specialization, find_doctors

request_Blueprint = Blueprint(
    'request_bp',
    __name__,
    template_folder= 'templates'
)

@request_Blueprint.route('/findFreeTime', methods=['GET', 'POST'])
def time_handler():
    if request.method == 'GET':
        names = find_names()
        return render_template('form.html',
                               request = 'time',
                               names = names
                               )
    else:
        result = find_time(
            request.form.get('names'),
            request.form.get('date')
        )
        print(result)
        state = False if result is None else True

        return render_template('output.html',
                               data = result,
                               boolValue = state,
                               request='time'
                               )

@request_Blueprint.route('/findFloor', methods=['GET', 'POST'])
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
def specialization_handler():
    if request.method == 'GET':
        specialization = find_specialization()
        return render_template('form.html',
                               request = 'specialization',
                               names = specialization
                               )
    else:
        result = find_doctors(request.form.get('names'))
        state = False if result is None else True

        return render_template('output.html',
                               data=result,
                               request='specialization'
                               )