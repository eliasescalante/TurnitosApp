from flask import Blueprint, jsonify
from services.medicos_service import listar_medicos

medicos_bp = Blueprint("medicos", __name__)

@medicos_bp.get("/medicos")
def get_medicos():
    return jsonify(listar_medicos())
