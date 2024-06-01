# Definición de los productos disponibles y sus precios
productos = {
    "Leche": 50,
    "Galletas": 35,
    "Gaseosa": 87,
    "Huevos": 66,
    "Aceite": 110,
    "Pan": 20
}

# Carrito de compras inicialmente vacío
carrito = {}

def mostrar_productos_disponibles():
    print("Productos disponibles y sus precios:")
    for producto, precio in productos.items():
        print(f"{producto}: ${precio}")

def agregar_producto():
    producto = input("Ingrese el nombre del producto a agregar: ")
    if producto in productos:
        cantidad = int(input(f"Ingrese la cantidad de {producto} a agregar: "))
        carrito[producto] = carrito.get(producto, 0) + cantidad
        print(f"{cantidad} de {producto} agregado(s) al carrito.")
    else:
        print("Producto no disponible.")

def eliminar_producto():
    producto = input("Ingrese el nombre del producto a eliminar: ")
    if producto in carrito:
        del carrito[producto]
        print(f"{producto} eliminado del carrito.")
    else:
        print("Producto no encontrado en el carrito.")

def ver_lista_de_compras():
    print("Lista de compras:")
    for producto, cantidad in carrito.items():
        print(f"{producto}: {cantidad}")

def finalizar_compra():
    total = sum(productos[producto] * cantidad for producto, cantidad in carrito.items())
    print("Ticket de compra:")
    ver_lista_de_compras()
    print(f"Total a pagar: ${total}")
    carrito.clear()

def salir():
    print("Gracias por su compra. Vuelva pronto!")

# Menú principal, donde me gusto la idea de agregar una seccion que muestre los productos disponibles.
def menu():
    while True:
        print("\nMenú:")
        print("1. Productos disponibles")
        print("2. Agregar producto")
        print("3. Eliminar producto")
        print("4. Ver lista de compras")
        print("5. Finalizar compra")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_productos_disponibles()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            ver_lista_de_compras()
        elif opcion == "5":
            finalizar_compra()
            break
        elif opcion == "6":
            salir()
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()
