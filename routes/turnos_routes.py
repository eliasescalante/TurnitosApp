from flask import Blueprint, request, jsonify
from services.turnos_service import listar_turnos_medico, reservar_turno

turnos_bp = Blueprint("turnos", __name__)

@turnos_bp.get("/turnos/<int:medico_id>")
def get_turnos(medico_id):
    return jsonify(listar_turnos_medico(medico_id))


@turnos_bp.post("/turnos")
def post_turno():
    data = request.get_json()

    medico_id = data.get("medico_id")
    fecha_hora = data.get("fecha_hora")
    paciente = data.get("paciente")

    response, status = reservar_turno(medico_id, fecha_hora, paciente)
    return jsonify(response), status
