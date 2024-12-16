from flask import Blueprint, request, render_template, session, redirect, url_for

from access import role_required
from doctor.model import insert_reception_notes, find_patient, change_app_mark

doctor_Blueprint = Blueprint(
    'doctor_bp',
    __name__,
    template_folder= 'templates'
)

@doctor_Blueprint.route('/', methods=['GET', 'POST'])
@role_required
def reception_handler():
    if len(request.form) == 3:
        return render_template('reception.html',
                           data = request.form
                           )
    else:
        insert_reception_notes(request.form)
        return redirect(url_for('privateOffice_bp.main_office_handler'))
