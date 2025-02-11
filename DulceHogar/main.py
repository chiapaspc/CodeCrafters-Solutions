#Sistema de gestión de inventario y ventas para Dulce Hogar

inventario = []

def registrar_producto():
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    inventario.append(producto)
    print("Producto registrado con éxito.")

def mostrar_inventario():
    print("\n-- Inventario --")
    for producto in inventario:
        print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']} ")

while True:
    print("\n-- Menú --")
    print("1. Registrar producto")
    print("2. Mostrar inventario")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        break
    else:
        print("Opcion invalidad. Intente de nuevo.")


    