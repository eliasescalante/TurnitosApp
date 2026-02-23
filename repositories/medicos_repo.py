from db import get_connection

def obtener_medicos():
    """
    Obtiene todos los médicos registrados en la base de datos.

    Returns:
        list[dict]: Lista de médicos con sus respectivos datos.
    """"""
    Obtiene todos los médicos registrados en la base de datos.

    Returns:
        list[dict]: Lista de médicos con sus respectivos datos.
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM medicos")
    medicos = cursor.fetchall()

    cursor.close()
    conn.close()
    return medicos
