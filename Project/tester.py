import os
from datetime import datetime

from connection import DBConnection
from sql_provider import SqlProvider

db_config = {
    "host" : "127.0.0.1",
    "port" : 3306,
    "user" : "root",
    "password" : "Aniretake105",
    "db" : "new_schema"
}

provider = SqlProvider(
    os.path.join(os.path.dirname(__file__), 'sql')
)

def find_data_in_db(db_config, sql):
    with DBConnection(db_config) as cursor:
        if cursor.execute(sql) is None:
            return None
        else:
            result = {}
            schema = [column[0] for column in cursor.description]
            result = [dict(zip(schema, row)) for row in cursor.fetchall()]
            return result

sql_statement = provider.get(
    'schedule_for_today.sql',
    {
                'date': datetime.strftime(datetime.now(), "%Y-%m-%d"),
                'id_doctor': 6
        }
)
result = find_data_in_db(db_config, sql_statement)
print(result)