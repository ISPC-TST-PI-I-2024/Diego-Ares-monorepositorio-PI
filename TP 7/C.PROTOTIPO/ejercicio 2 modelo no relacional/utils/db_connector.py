import mysql.connector
from mysql.connector import Error

def create_connection():
    """Crea y retorna una conexión a la base de datos MySQL."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='tu_usuario',
            password='tu_contraseña',
            database='IoTDevices'
        )
        return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def close_connection(connection):
    """Cierra la conexión a la base de datos."""
    if connection:
        connection.close()