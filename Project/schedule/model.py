import os
from datetime import datetime

from flask import current_app, json

from cache.redis_cache import RedisCache
from connection import DBConnection
from sql_provider import SqlProvider

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

def find_data_in_db(db_config, sql):
    with DBConnection(db_config) as cursor:
        if cursor.execute(sql) is None:
            return None
        else:
            schema = [column[0] for column in cursor.description]
            result = [dict(zip(schema, row)) for row in cursor.fetchall()]
            return result

def find_start_schedule():
    with open('schedule/sql/start_schedule.sql', 'r') as file:
        sql_script = file.read()
    result = find_data_in_db(current_app.config['db_config'], sql_script)
    return result

def do_something_in_db(db_config, sql):
    with DBConnection(db_config) as cursor:
        if cursor.execute(sql) is None:
            return None
        else:
            return

def find_in_db(db_config, sql):
    with DBConnection(db_config) as cursor:
        if cursor.execute(sql) is None:
            return None
        else:
            result = [row for row in cursor.fetchall()]
            if len(result) == 0:
                return None
            else:
                return result

def find_id():
    with open('schedule/sql/find_id.sql', 'r') as file:
        sql_script = file.read()
    result = find_in_db(current_app.config['db_config'], sql_script)
    return result

def find_names():
    with open('schedule/sql/names.sql', 'r') as file:
        sql_script = file.read()
    result = find_in_db(current_app.config['db_config'], sql_script)
    return result

def create_name_id():
    name_id = RedisCache(current_app.config['redis'])
    id = find_id()
    for i in id:
        name_id.create_hset('name_id', i[1], i[0])
    return

def add_in_delete_cache(value):
    delete_cache = RedisCache(current_app.config['redis'])
    delete_cache.add_list('del',value)
    return

def find_office():
    with open('schedule/sql/find_office.sql', 'r') as file:
        sql_script = file.read()
    result = find_in_db(current_app.config['db_config'], sql_script)
    return result

def create_office_doctor():
    name_id = RedisCache(current_app.config['redis'])
    id = find_office()
    for i in id:
        name_id.create_hset('office_id', i[1], i[0])
    return

def change_edit_cache(id, values):
    edit = RedisCache(current_app.config['redis'])
    values_json=json.dumps(values)
    edit.create_hset('edit', id, values_json)
    return

def get_from_name_id(name):
    res = RedisCache(current_app.config['redis'])
    return res.get_hset('name_id', name)

def get_from_office_id(id_doctor):
    res = RedisCache(current_app.config['redis'])
    return res.get_hset('office_id', id_doctor)

def change_local_table(table, id, date, time, name):
    for i in table:
        if i['id_shedule'] == id:
            i['rec_date'] = date
            i['rec_time'] = time
            i['doctor_name'] = name
            return table

def add_in_local_table(table, date, time, name):
    last_id = table[-1]['id_shedule'] + 1
    table.append({
        'id_shedule': last_id,
        'rec_date': date,
        'rec_time': time,
        'doctor_name': name
    })
    return table

def change_add_cache(id, values):
    edit = RedisCache(current_app.config['redis'])
    values_json = json.dumps(values)
    edit.create_hset('add', id, values_json)
    return

def remove_local_data_to_bd():
    cur = RedisCache(current_app.config['redis'])
    del_cache = cur.get_list('del')
    for field in del_cache:
        cur.hdel('edit', field)
        cur.hdel('add', field)

    edit = cur.get_hsetall('edit')
    add = cur.get_hsetall('add')

    cur.clean()
    return del_cache, edit, add

def delete_in_bd(delete):
    for id in delete:
        sql_statement=provider.get('delete_row_in_bd.sql',{'id': id})
        do_something_in_db(current_app.config['db_config'],sql_statement)
    return

def add_in_bd(add):
    for id in add:
        res = json.loads(add[id])
        sql_statement = provider.get('add_row_in_bd.sql', {
                'office': int(res[0]),
                'date': res[1],
                'time': datetime.strptime(res[2]+":00","%H:%M:%S"),
                'doctor': int(res[3])
            }
        )
        do_something_in_db(current_app.config['db_config'], sql_statement)
    return

def edit_in_bd(edit):
    for id in edit:
        res = json.loads(edit[id])
        sql_statement = provider.get('edit_row_in_bd.sql', {
                'office': int(res[0]),
                'date': res[1],
                'time': datetime.strptime(res[2]+":00","%H:%M:%S"),
                'doctor': int(res[3]),
                'id': int(id)
            }
        )
        do_something_in_db(current_app.config['db_config'], sql_statement)
    return