from connection import DBConnection

def select(db_config, db_statement):
    result = []
    with DBConnection(db_config) as cursor:
        cursor.execute(db_statement)
        schema = [column[0] for column in cursor.description]
        result = [dict(zip(schema, row)) for row in cursor.fetchall()]

    return result