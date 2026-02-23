from repositories.medicos_repo import obtener_medicos

def listar_medicos():
    """
    Devuelve la lista de médicos disponibles.

    Returns:
        list[dict]: Lista de médicos.
    """
    return obtener_medicos()
