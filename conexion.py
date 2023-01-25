import mysql.connector

def conexion():
    try:
        conexion = mysql.connector.connect(
            database = 'test_db',
            host = 'localhost',
            user = 'root',
            password = 'admin',
            port = 3306
        )
        print('Conexion a base de datos exitosa')
        return conexion
    except Exception as e:
        print(f'Error al conectar a la base de datos. Error {e}')
    
# def cursor():
#     cursor = conexion().cursor()
#     print('Conexion al cursor exitosa')
#     return cursor

# def close():
#     close = conexion().close()
#     print('Cierre de la conexion exitosa')
#     return close