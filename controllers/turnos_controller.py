from services.turnos_service import listar_turnos_medico, reservar_turno

def get_turnos_medico_controller(medico_id):
    """
    Controlador encargado de obtener los turnos asociados
    a un médico específico.

    Args:
        medico_id (int): ID del médico.

    Returns:
        tuple:
            - list[dict]: Lista de turnos.
            - int: Código HTTP 200 (OK).
    """
    turnos = listar_turnos_medico(medico_id)
    return turnos, 200


def crear_turno_controller(data):
    """
    Controlador encargado de gestionar la creación de un nuevo turno.

    Valida la información recibida desde la capa HTTP antes de delegar
    la lógica de negocio al service correspondiente.

    Args:
        data (dict): Datos recibidos desde el request JSON que deben contener:
            - medico_id (int)
            - fecha_hora (str)
            - paciente (str)

    Returns:
        tuple:
            - dict: Mensaje de éxito o error.
            - int: Código HTTP correspondiente (400 o 201).
    """
    medico_id = data.get("medico_id")
    fecha_hora = data.get("fecha_hora")
    paciente = data.get("paciente")

    if not medico_id or not fecha_hora or not paciente:
        return {"error": "Datos incompletos"}, 400

    return reservar_turno(medico_id, fecha_hora, paciente)
