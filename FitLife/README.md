# Sistema de gestión de usuarios y entrenamientos

Este proyecto es un sistema básico para gestionar usuarios y entrenamientos para "FitLife".

# Funcionalidades

- Usuarios.
    -- id_usuario(automatico), nombre, edad, peso y altura.
    -- Registro
    -- Mostrar
- Entrenamientos. 
    -- id_entrenamiento (automatico), tipo de entrenamiento (cardio o pesas), duracion (minutos), calorias quemadas (kilocalorias)
    -- Registro
    -- Mostrar
- Registro entrenamientos.
    -- id_usuario (solicitado), id_entrenamiento (solicitado), fecha (automatico)
    -- Solicita id del usuario e id_entrenamiento y los agrega a la lista.
    -- Mostrar, solicita el id_usuario y muestra todos los entrenamientos registrados, asi como da un Total de Calorias y Total de Minutos de entrenamiento.
- Guardar y cargar datos
    -- Guarda los datos del usuario y entrenamientos en archivos JSON