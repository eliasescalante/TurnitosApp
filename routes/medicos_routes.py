from flask import Blueprint, jsonify
from controllers.medicos_controller import get_medicos_controller

medicos_bp = Blueprint("medicos", __name__)

@medicos_bp.get("/medicos")
def get_medicos():
    """
    Endpoint GET que retorna la lista de médicos en formato JSON.

    Returns:
        Response: JSON con lista de médicos y status 200.
    """
    response, status = get_medicos_controller()
    return jsonify(response), status
