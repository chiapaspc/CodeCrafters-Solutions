# Sistema de gestion de TI en SICT

Proyecto para gestionar varias tareas en el area de Tecnologias de Informacion en SICT, Chiapas.

# Tecnologia

Se usara Boostrap y CodeIgniter 4.

# Funcionalidades

- Usuarios
 -- id_usuario (autoinc), nombre, apellidos, area
 -- Registrar, mostrar, modificar y eliminar.
- Equipos
 -- id_equipo (autoinc), id_usuario (asignado), tipo, marca, modelo, serie, inv
 -- Registrar, asignar, mostrar, modificar y eliminar.
- Vales
 -- id_vale (folio), id_equipo, fecha_ingreso, fecha_salida, hora_ingreso, hora_salida, tipo (entrada o salida), observaciones, id_usuario_entrego, id_usuario_vobo, id_usuario_recibio
 -- Registrar, mostrar, modificar, imprimir.