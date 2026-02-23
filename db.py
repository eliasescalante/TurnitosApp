import mysql.connector
import os

def get_connection():
    """
    Crea y retorna una conexión activa a la base de datos MySQL
    utilizando variables de entorno.

    Returns:
        mysql.connector.connection.MySQLConnection: Conexión a la base de datos.
    """
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT", 3306))
    )
