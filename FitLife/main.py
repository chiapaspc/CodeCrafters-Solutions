#Sistema de gestión de enrenamientos para FitLife
import json
from datetime import date
from tabulate import tabulate

usuarios = []
entrenamientos = []
progreso = []

# --- Carga y guardado de datos. ---
def guardar_datos():
    archivos = ["usuarios.json", "entrenamientos.json", "progreso.json"]
    datos = [usuarios, entrenamientos, progreso]

    for archivo, contenido in zip(archivos, datos):
        with open(archivo, "w") as f:
            json.dump(contenido, f)
    print("Datos guardados correctamente")

def cargar_datos():
    try:
        with open("usuarios.json", "r") as archivo:
            usuarios.extend(json.load(archivo))
        with open("entrenamientos.json", "r") as archivo:
            entrenamientos.extend(json.load(archivo))
        with open("progreso.json", "r") as archivo:
            progreso.extend(json.load(archivo))
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("No se encontraron los archivos de datos. Se iniciara con datos vacios.")

# --- Usuarios ---
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
    print("\n-- Usuarios --")
    headers = ["Id", "Nombre", "Edad", "Pesos", "Altura"]
    rows = [[u["id_usuario"], u["nombre"], u["edad"], u["peso"], u["altura"]] for u in usuarios]
    print(tabulate(rows, headers=headers, tablefmt="grid"))
    print("Total de usuarios: ", len(usuarios))

# --- Entrenamientos ---
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
    print("\n-- Entrenamientos --")
    headers = ["Id", "Tipo de Entrenamiento", "Duración (mins)", "Calorias Quemadas (kcal)"]
    rows = [[e["id_entrenamiento"], e["tipo"], e["duracion"], e["calorias"]] for e in entrenamientos]
    print(tabulate(rows, headers=headers, tablefmt="grid"))
    print("Total de entrenamientos: ", len(entrenamientos))

# --- Progreso ---

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

cargar_datos()
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
        guardar_datos()
        break
    else:
        print("Opción incorrecta")
