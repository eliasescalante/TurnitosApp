from repositories.turnos_repo import (
    obtener_turnos_por_medico,
    existe_turno,
    crear_turno
)

def listar_turnos_medico(medico_id):
    return obtener_turnos_por_medico(medico_id)


def reservar_turno(medico_id, fecha_hora, paciente):
    if existe_turno(medico_id, fecha_hora):
        return {"error": "Turno no disponible"}, 400

    crear_turno(medico_id, fecha_hora, paciente)
    return {"message": "Turno confirmado"}, 201
