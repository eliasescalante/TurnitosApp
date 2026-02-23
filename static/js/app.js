// URL base de nuestra API REST
// Cambiar solo esto si el backend se deploya en otro servidor
const API = "http://127.0.0.1:5000"


// ======================================================
// FUNCIÓN: CARGAR MÉDICOS
// Hace una petición GET a /medicos y los muestra en pantalla
// ======================================================
async function cargarMedicos() {

    // fetch → realiza una petición HTTP
    // al no especificar method, por defecto es GET
    const res = await fetch(`${API}/medicos`)

    // Convertimos la respuesta a JSON
    const data = await res.json()

    // Seleccionamos el <ul> donde vamos a pintar los médicos
    const lista = document.getElementById("listaMedicos")

    // Limpiamos el contenido previo para no duplicar datos
    lista.innerHTML = ""

    // Recorremos el array de médicos que vino desde la API
    data.forEach(m => {

        // Insertamos cada médico dentro de la lista
        // template string → permite usar variables dentro del HTML
        lista.innerHTML += `<li>${m.id} - ${m.nombre} - ${m.especialidad}</li>`
    })
}



// ======================================================
// FUNCIÓN: CARGAR TURNOS DE UN MÉDICO
// Hace GET /turnos/<medico_id>
// ======================================================
async function cargarTurnos() {

    // Tomamos el valor que el usuario escribió en el input
    const medicoId = document.getElementById("medicoId").value

    // Petición GET dinámica usando el ID del médico
    const res = await fetch(`${API}/turnos/${medicoId}`)

    // Convertimos la respuesta a JSON
    const data = await res.json()

    // Seleccionamos el <ul> donde vamos a mostrar los turnos
    const lista = document.getElementById("listaTurnos")

    // Limpiamos la lista antes de renderizar
    lista.innerHTML = ""

    // Recorremos los turnos recibidos
    data.forEach(t => {

        // Mostramos fecha y nombre del paciente
        lista.innerHTML += `
            <li>
                ${t.fecha_hora} - ${t.nombre_paciente}
            </li>
        `
    })
}



// ======================================================
// FUNCIÓN: CREAR TURNO
// Hace POST /turnos enviando JSON al backend
// ======================================================
async function crearTurno() {

    // Capturamos los valores del formulario
    const medico_id = document.getElementById("medico_id").value
    const fecha_hora = document.getElementById("fecha_hora").value
    const paciente = document.getElementById("paciente").value

    // fetch con configuración → acá usamos POST
    const res = await fetch(`${API}/turnos`, {

        // Método HTTP
        method: "POST",

        // Cabecera obligatoria cuando enviamos JSON
        headers: {
            "Content-Type": "application/json"
        },

        // body → datos que enviamos al backend
        // JSON.stringify convierte el objeto JS a JSON válido
        body: JSON.stringify({
            medico_id,
            fecha_hora,
            paciente
        })
    })

    // Convertimos la respuesta del backend a JSON
    const data = await res.json()

    // Mostramos la respuesta del servidor en pantalla
    // Puede ser:
    // ✔ Turno confirmado
    // ❌ Turno no disponible
    document.getElementById("respuesta").innerText =
        JSON.stringify(data, null, 2)
}



// ======================================================
// EVENTO: CUANDO CARGA LA PÁGINA
// Se ejecuta automáticamente
// ======================================================

// Esto permite que apenas abrimos el front
// se carguen los médicos sin tocar ningún botón
window.onload = cargarMedicos
