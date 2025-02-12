#Sistema de gestión de inventario y ventas para Dulce Hogar
import json

inventario = []
ventas = []
articulos_vendidos = []

# --- Carga y guardado de datos. ---
def guardar_datos():
    with open("inventario.json", "w") as archivo:
        json.dump(inventario, archivo)
    with open("ventas.json", "w") as archivo:
        json.dump(ventas, archivo)
    with open("articulos_vendidos.json", "w") as archivo:
        json.dump(articulos_vendidos, archivo)
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
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    inventario.append(producto)
    print("Producto registrado con éxito.")


# --- Sistema TPV ---

# Genera la nueva venta y le asigna un ID
def nueva_venta():
    nombre_cliente = input("Nombre del cliente: ")
    total_productos = 0
    total = 0.0
    id_venta = len(ventas) + 1
    venta = {"nombre_cliente": nombre_cliente, "total_productos": total_productos, "total": total, "id" : id_venta}
    ventas.append(venta)
    print("Venta creada: ", id_venta)
    venta_producto(id_venta)

# Agrega un producto a la venta con el id
def agregar_producto_venta(id_venta, producto, cantidad, precio):
    nombre = producto ["nombre"]
    id_venta = id_venta
    cantidad = cantidad
    precio = precio
    subtotal = precio * cantidad
    producto = {"id": id_venta, "cantidad": cantidad, "nombre": nombre, "precio": precio, "subtotal": subtotal}
    articulos_vendidos.append(producto) 

# Cierra la venta y la totaliza
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

# Menu TPV
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
                if producto["nombre"] == nombre:
                    encontrado = True
                    print(f"Existencia: {producto['cantidad']}")
                    cantidad = int(input("Cantidad a vender: "))
                    if cantidad <= producto["cantidad"] :
                            precio = producto["precio"]
                            agregar_producto_venta(id_venta, producto, cantidad, precio)
                            producto["cantidad"]-= cantidad
                            print(f"Producto agregado correctamente. Stock restante: {producto['cantidad']}")
                            print(articulos_vendidos)
                            break
                    else:
                        print("No hay suficiente stock disponible.")
            if not encontrado:
                print("El producto no existe")
        elif opcion == "2":
            totalizar_venta(id_venta)
            break


# --- Reportes ---
# Muestra los productos en stock
def mostrar_inventario():
    print("\n-- Inventario --")
    for producto in inventario:
        print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']} ")

# Muestra todas las ventas 
def mostrar_ventas():
    print("\n-- Ventas del dia --")
    for venta in ventas:
        print(f"Nombre de Cliente: {venta['nombre_cliente']}, Articulos: {venta['total_productos']}, Total Venta: ${venta['total']} ")

# --- Menu principal ----

cargar_datos()
while True:
    print("\n-- Menú --")
    print("1. Registrar producto")
    print("2. Mostrar inventario")
    print("3. Nueva Venta")
    print("4. Reporte de Ventas")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        nueva_venta()
    elif opcion == "4":
        mostrar_ventas()
    elif opcion == "5":
        guardar_datos()
        break
    else:
        print("Opcion invalidad. Intente de nuevo.")


    