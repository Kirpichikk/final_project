from flask import Blueprint, request, render_template, current_app
from connection import DBConnection
from sql_provider import SqlProvider
from access import login_required
import os

request_Blueprint = Blueprint(
    'request_bp',
    __name__,
    template_folder= 'templates'
)

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

@request_Blueprint.route('/', methods=['GET', 'POST'])
@login_required
def init_handler():
    if request.method == 'GET':
        return render_template('product_form.html')
    elif request.method == 'POST':
        name = request.form['product_name']
        sql = provider.get(
            'request.sql',
            {'prod_id': name}
        )

        with DBConnection(current_app.config['db_config']) as cursor:
            cursor.execute(sql)
            schema = [column[0] for column in cursor.description]
            result = [dict(zip(schema, row)) for row in cursor.fetchall()]

        render_data= {
            'status': True if result else False,
            'data': result
        }
        return render_template('database_output.html',
                               render_data=render_data
                               )