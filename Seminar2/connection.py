from pymysql import connect
from pymysql import OperationalError

class DBConnection:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None
        self.cursor = None

    def __enter__(self): #as cursor
        try:
            self.connection = connect(**self.db_config)
            self.cursor = self.connection.cursor()
            return self.cursor
        except OperationalError as err:
            print("error: ", err)
            return None

    def __exit__(self, exc_type, exc_val, exc_tb): #out of context
        if self.connection and self.cursor:
            if exc_type:
                print(f"exc_type: {exc_type}")
                print(f"exc_value: {exc_val}")
                self.connection.rollback()
            else:
                self.connection.commit()
            self.connection.close()
            self.cursor.close()
        else:
            if exc_type:
                print(f"exc_type: {exc_type}")
                print(f"exc_value: {exc_val}")
        return True

db_config = {
    'host' : '127.0.0.1',
    'port' : 3306,
    'user' : 'root',
    'password' : 'Aniretake105',
    'db' : 'new_schema'
}
