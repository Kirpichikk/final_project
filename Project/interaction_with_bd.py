from connection import DBConnection


def find_user_in_db(db_config, sql):
    with DBConnection(db_config) as cursor:
        if cursor.execute(sql) is None:
            return None
        else:
            schema = [column[0] for column in cursor.description]
            for row in cursor.fetchall():
                result = dict(zip(schema, row))
            return result

def find_data_in_db(db_config, sql):
    with DBConnection(db_config) as cursor:
        if cursor.execute(sql) is None:
            return None
        else:
            schema = [column[0] for column in cursor.description]
            result = [dict(zip(schema, row)) for row in cursor.fetchall()]
            return result

def update_data_in_db(db_config, sql):
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

def call_proc(db_config, proc_name, *args):
    with DBConnection(db_config) as cursor:
        if cursor is None:
            return None
        param_list = []
        for arg in args:
            param_list.append(arg)
        res = cursor.callproc(proc_name, param_list)
    return res