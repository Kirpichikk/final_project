from flask import Blueprint

schedule_Blueprint = Blueprint(
    'schedule_bp',
    __name__,
    template_folder= 'templates'
)

@schedule_Blueprint.route('/')
def init_handler():
    pass

@schedule_Blueprint.route('/add')
def add_handler():
    pass

@schedule_Blueprint.route('/edit')
def edit_handler():
    pass

@schedule_Blueprint.route('/del')
def delete_handler():
    pass

@schedule_Blueprint.route('/end')
def end_handler():
    pass