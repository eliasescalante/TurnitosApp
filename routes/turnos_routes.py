from flask import Blueprint, request, jsonify
from controllers.turnos_controller import (
    get_turnos_medico_controller,
    crear_turno_controller
)

turnos_bp = Blueprint("turnos", __name__)

@turnos_bp.get("/turnos/<int:medico_id>")
def get_turnos(medico_id):
    """
    Endpoint GET que retorna los turnos de un médico específico.

    Args:
        medico_id (int): ID del médico.

    Returns:
        Response: JSON con lista de turnos.
    """
    response, status = get_turnos_medico_controller(medico_id)
    return jsonify(response), status


@turnos_bp.post("/turnos")
def post_turno():
    """
    Endpoint POST que permite reservar un turno.

    Espera un JSON con:
        - medico_id (int)
        - fecha_hora (str)
        - paciente (str)

    Returns:
        Response: JSON con mensaje de éxito o error y código HTTP correspondiente.
    """
    response, status = crear_turno_controller(request.get_json())
    return jsonify(response), status
