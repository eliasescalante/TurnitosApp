from repositories.turnos_repo import (
    obtener_turnos_por_medico,
    existe_turno,
    crear_turno
)

def listar_turnos_medico(medico_id):
    """
    Devuelve los turnos de un médico específico.

    Args:
        medico_id (int): ID del médico.

    Returns:
        list[dict]: Lista de turnos.
    """
    return obtener_turnos_por_medico(medico_id)


def reservar_turno(medico_id, fecha_hora, paciente):
    """
    Gestiona la reserva de un turno aplicando la lógica de negocio.

    Verifica si el turno ya existe antes de crearlo.

    Args:
        medico_id (int): ID del médico.
        fecha_hora (str): Fecha y hora solicitada.
        paciente (str): Nombre del paciente.

    Returns:
        tuple: (respuesta dict, código HTTP)
    """
    if existe_turno(medico_id, fecha_hora):
        return {"error": "Turno no disponible"}, 400

    crear_turno(medico_id, fecha_hora, paciente)
    return {"message": "Turno confirmado"}, 201
