from services.medicos_service import listar_medicos

def get_medicos_controller():
    """
    Controlador encargado de gestionar la solicitud para obtener
    la lista de médicos.

    Este controlador actúa como intermediario entre la capa HTTP
    (routes) y la capa de negocio (services).

    Returns:
        tuple:
            - list[dict]: Lista de médicos.
            - int: Código HTTP 200 (OK).
    """
    medicos = listar_medicos()
    return medicos, 200
