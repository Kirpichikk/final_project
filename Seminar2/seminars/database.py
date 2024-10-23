import pymysql

config = {
    'host' : '127.0.0.1',
    'port' : 3306,
    'user' : 'root',
    'password' : 'Aniretake105',
    'db' : 'new_schema'
}
def select_from_database(config, sql):
    connection = pymysql.connect(**config)
    '''
    connection = pymysql.connect(
        host = config['host'],
        port = config['port'],
        user = config['user'],
        password = config['password'],
        db = config['db']
    )
    '''
    cursor = connection.cursor()

    cursor.execute(sql)
    result = cursor.fetchall()

    for i in cursor.description:
        print(i)
    print("\n")
    for i in result:
        print(i)

    schema = [info[0] for info in cursor.description]

    output = []
    for row in result:
        output.append(
            dict(zip(schema, row))
        )

    print("\n")
    for i in output:
        print(i)

    cursor.close()
    connection.close() #очень важная строчка, не надо про неё забывать
    return output

result = select_from_database(config, 'select * from department')
print(result)