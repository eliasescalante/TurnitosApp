CREATE DATABASE clinica;
USE clinica;

CREATE TABLE medicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    especialidad VARCHAR(100)
);

CREATE TABLE turnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha_hora DATETIME,
    nombre_paciente VARCHAR(100),
    medico_id INT
);

INSERT INTO medicos (nombre, especialidad)
VALUES
('Dr. House', 'Diagnóstico'),
('Dra. Grey', 'Cirugía');
