#Sistema de gestión de enrenamientos para FitLife
import json
from datetime import date
from tabulate import tabulate

usuarios = []
entrenamientos = []
progreso = []

def registro_usuarios():
    id_usuario = len(usuarios) + 1
    nombre = input("Nombre: ")
    edad = int(input("Edad: ")) 
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    usuario =  {"id_usuario": id_usuario, "nombre":nombre, "edad":edad, "peso":peso, "altura":altura}
    try:
        usuarios.append(usuario)
        print("Usuario registrado correctamente")
    except:
        print("Error al registrar usuario")

def mostrar_usuarios():
    for usuario in usuarios:
        print(usuario)


def crear_entrenamiento(): 
    id_entrenamiento = len(entrenamientos) + 1
    tipo = input("Tipo de entrenamiento (cardio, pesas): ")
    duracion = float(input("Duración (minutos): "))
    calorias = float(input("Calorías quemadas (kilocalorias): "))
    entrenamiento = {"id_entrenamiento": id_entrenamiento, "tipo":tipo, "duracion":duracion, "calorias":calorias}
    try:
        entrenamientos.append(entrenamiento)
        print("Entrenamiento registrado correctamente")     
    except:
        print("Error al registrar entrenamiento")

def mostrar_entrenamientos():
    for entrenamiento in entrenamientos:
        print(entrenamiento)

def asignar_entrenamiento():
    id_usuario = int(input("Ingrese el id del usuario: "))
    for usuario in usuarios:
        if usuario["id_usuario"] == id_usuario:
            id_entrenamiento = int(input("Ingrese el id del entrenamiento: "))
            for entrenamiento in entrenamientos:
                if entrenamiento["id_entrenamiento"] == id_entrenamiento:
                    fecha = str(date.today())
                    progreso.append({"id_usuario":id_usuario, "id_entrenamiento":id_entrenamiento, "fecha": fecha})
                    print("Entrenamiento asignado correctamente")
            break
    else:
        print("Usuario no encontrado")
        return

def mostrar_avances(id_usuario):
    for avance in progreso:
        if avance["id_usuario"] == id_usuario:
            print(avance)


while True:
    print("\n Menu de opciones")    
    print("1. Registrar usuario")
    print("2. Mostrar usuarios")    
    print("3. Crear entrenamiento")
    print("4. Mostrar entrenamientos")
    print("5. Asignar entrenamiento")
    print("6. Mostrar avances")
    print("7. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        registro_usuarios()
    elif opcion == 2:
        mostrar_usuarios()   
    elif opcion == 3:
        crear_entrenamiento()
    elif opcion == 4:
        mostrar_entrenamientos()
    elif opcion == 5:
        asignar_entrenamiento()
    elif opcion == 6:
        id_usuario = int(input("Ingrese el id del usuario: "))
        mostrar_avances(id_usuario)
    elif opcion == 7:
        break
    else:
        print("Opción incorrecta")
