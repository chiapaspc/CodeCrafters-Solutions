#Sistema de gestión de inventario y ventas para Dulce Hogar
import json
from datetime import date
from tabulate import tabulate



inventario = []
ventas = []
articulos_vendidos = []

# --- Carga y guardado de datos. ---
def guardar_datos():
    archivos = ["inventario.json", "ventas.json", "articulos_vendidos.json"]
    datos = [inventario, ventas, articulos_vendidos]

    for archivo, contenido in zip(archivos, datos):
        with open(archivo, "w") as f:
            json.dump(contenido, f)
    print("Datos guardados correctamente")

def cargar_datos():
    try:
        with open("inventario.json", "r") as archivo:
            inventario.extend(json.load(archivo))
        with open("ventas.json", "r") as archivo:
            ventas.extend(json.load(archivo))
        with open("articulos_vendidos.json", "r") as archivo:
            articulos_vendidos.extend(json.load(archivo))
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("No se encontraron los archivos de datos. Se iniciara con datos vacios.")

# --- Inventario ---
def registrar_producto():
    while True:
        try:
            nombre = input("Nombre del producto: ")
            if not nombre:
                print("El nombre no puede estar vacio")
                continue
            cantidad = int(input("Cantidad: "))
            if not cantidad or cantidad < 0:
                print("La cantidad no puede estar vacio o ser un numero negativo")
                continue
            precio = float(input("Precio: "))
            if not precio or cantidad < 0:
                print("Precio no puede estar vacio o ser numero negativo")
                continue
            id_producto = len(inventario) + 1
            producto = {"id_producto": id_producto, "nombre": nombre, "cantidad": cantidad, "precio": precio, "activo": 1}
            inventario.append(producto)
            print("Producto registrado con éxito.")
            break
        except ValueError:
            print("Entrada invalidad, intente de nuevo.")

def modificar_producto():
    nombre = input("Nombre del producto a modificar: ")
    for producto in inventario:
        if producto["nombre"] == nombre:
            print(f"Producto actual: {producto}")

            #Modificar nombre
            nuevo_nombre = input("Nuevo nombre (dejar en blanco para no modificar): ")
            if nuevo_nombre.strip(): #Verifica si la cadena no esta vacia
                 producto["nombre"] =  nuevo_nombre
            
            #Modificar cantidad
            nueva_cantidad = input("Nueva cantidad (dejar en blanco para no modificar): ")
            if nueva_cantidad.strip():
                try:
                    producto["cantidad"] = int(nueva_cantidad)
                except ValueError:
                    print("Cantidad invalida, debe de ser un numero, reintente")

            #Modificar precio
            nuevo_precio = input("Nuevo precio (dejar en blanco para no modificar): ")
            if nuevo_precio.strip():
                try:
                    producto["precio"] = float(nuevo_precio)
                except ValueError:
                    print("Precio invalido, debe de ser un numero con decimales, reintente")
            
            #Modificar estado
            if producto["activo"] == 0:
                res = input("¿Desea activar el producto? (si o no): ").strip().lower()
                if res == "si" :
                    producto["activo"] = 1
                if res == "no":
                    producto["activo"] = 0
                else :
                    print("Opcion invalida, reintente")
            elif producto["activo"] == 1:
                res = input("¿Desea desactivar el producto? (si o no): ").strip().lower()
                if res == "si" :
                    producto["activo"] = 0
                if res == "no":
                    producto["activo"] = 1
                else :
                    print("Opcion invalida, reintente")
            print("Producto modificado con exito")
            return
    print("Producto no encontrado")

# --- Sistema TPV ---
def nueva_venta():
    nombre_cliente = input("Nombre del cliente: ")
    total_productos = 0
    total = 0.0
    id_venta = len(ventas) + 1
    #se convierte la fecha a Str porque Json no admite formatos date o datetime
    fecha = str(date.today())
    venta = {"id" : id_venta, "nombre_cliente": nombre_cliente, "total_productos": total_productos, "total": total, "fecha": fecha}
    ventas.append(venta)
    print("Venta creada: ", id_venta)
    venta_producto(id_venta)

def agregar_producto_venta(id_venta, producto, cantidad, precio):
    nombre = producto ["nombre"]
    id_venta = id_venta
    cantidad = cantidad
    precio = precio
    subtotal = precio * cantidad
    producto = {"id": id_venta, "cantidad": cantidad, "nombre": nombre, "precio": precio, "subtotal": subtotal}
    articulos_vendidos.append(producto) 

def totalizar_venta(id_venta):
    id_venta = id_venta
    articulos = 0
    total = 0
    for producto in articulos_vendidos:
        if producto["id"] == id_venta:
            articulos += producto["cantidad"]
            total = total + producto['subtotal']
            for venta in ventas:
                if id_venta == venta["id"]:
                    venta["total"] = total
                    venta["total_productos"] = articulos
    print("Venta finalizada total: ", total)
    print("Numero de Articulos: ", articulos)

def venta_producto(id):
    while True:
        id_venta = id
        print("\n-- Venta ", id_venta, "--")
        print("1. Agregar Producto")
        print("2. Cerrar Venta")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            encontrado = False
            for producto in inventario:
                if producto["nombre"] == nombre and producto["activo"] == 1:
                    encontrado = True
                    print(f"Existencia: {producto['cantidad']}")
                    cantidad = int(input("Cantidad a vender: "))
                    if cantidad <= producto["cantidad"] :
                            precio = producto["precio"]
                            agregar_producto_venta(id_venta, producto, cantidad, precio)
                            producto["cantidad"]-= cantidad
                            print(f"Producto agregado correctamente. Stock restante: {producto['cantidad']}")
                            #Agregamos una alerta si el inventario es menor a 5
                            alerta_inventario_bajo(nombre)
                            #debug
                            #print(articulos_vendidos)
                            break
                    else:
                        print("No hay suficiente stock disponible.")
            if not encontrado:
                print("El producto no existe")
        elif opcion == "2":
            totalizar_venta(id_venta)
            break

# --- Reportes ---
def mostrar_inventario():
    print("\n-- Inventario --")
    headers = ["Nombre", "Cantidad", "Precio", "Estado"]
    rows = [[p["nombre"], p["cantidad"], p["precio"], "Activo" if p["activo"] else "Inactivo"] for p in inventario]
    print(tabulate(rows, headers=headers, tablefmt="grid"))
    print("Total de productos: ", len(inventario))

def mostrar_ventas():
    print("\n-- Ventas del dia --")
    cantidad_ventas = 0
    producto_mas_vendido = ""
    for venta in ventas:
        print(f"Nombre de Cliente: {venta['nombre_cliente']}, Articulos: {venta['total_productos']}, Total Venta: ${venta['total']}, Fecha de compra: {venta['fecha']} ")
        cantidad_ventas += 1
    print(f"Total de ventas: {cantidad_ventas}")

def alerta_inventario_bajo(nombre=None):
    if nombre is None:
        for producto in inventario:
            if producto["cantidad"] < 5:
                print(f"¡Atención! {producto['nombre']} tiene solo {producto['cantidad']} unidades en stock.")
    else :
        for producto in inventario:
            if nombre == producto["nombre"] and producto["cantidad"] < 5:
                print(f"¡Atención! {producto['nombre']} tiene solo {producto['cantidad']} unidades en stock.")

# --- Menu principal ---
cargar_datos()
while True:
    print("\n-- Menú --")
    print("1. Agregar producto")
    print("MP. Modificar Producto")
    print("2. Mostrar inventario")
    print("3. Nueva Venta")
    print("4. Reporte de Ventas")
    print("5. Mostrar productos con inventario bajo")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_producto()
    elif opcion == "MP":
        modificar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        nueva_venta()
    elif opcion == "4":
        mostrar_ventas()
    elif opcion == "5":
        alerta_inventario_bajo()
    elif opcion == "6":
        guardar_datos()
        break
    else:
        print("Opcion invalidad. Intente de nuevo.")


