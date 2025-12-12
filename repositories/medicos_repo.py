from db import get_connection

def obtener_medicos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM medicos")
    medicos = cursor.fetchall()

    cursor.close()
    conn.close()
    return medicos
