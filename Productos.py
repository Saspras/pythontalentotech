import sqlite3

conexion = sqlite3.connect("Productos.db")
cursor = conexion.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS PRODUCTOS 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            Nombre TEXT NOT NULL,
            Categoria TEXT NOT NULL, 
            Precio INTEGER NOT NULL,
            Stock INTEGER NOT NULL)""")
conexion.commit()

def agregar_producto (Nombre, Categoria, Precio, Stock):
    cursor.execute(
        "INSERT INTO PRODUCTOS(Nombre, Categoria, Precio, Stock) VALUES (?, ?, ?, ?)",
        (Nombre, Categoria,Precio, Stock,))
    conexion.commit()
    print(f"Producto : {Nombre} fue agregado correctamente ")

def mostrar_producto ():
    cursor.execute("SELECT * FROM PRODUCTOS")
    productos = cursor.fetchall()
    print("""\nListado de productos""")
    if not productos:
        print("No hay productos disponibles")
        return
    for producto in productos:
        print(f"ID : {producto[0]} | Nombre : {producto[1]} | Categoria : {producto[2]} | Precio : {producto[3]} | Stock : {producto[4]}")


def actualizar_precio(Id, Precio):
    cursor.execute("UPDATE PRODUCTOS SET Precio = ? WHERE id = ?", (Precio, Id))
    if cursor.rowcount == 0:
        print("No existe un producto con ese id")
        return
    conexion.commit()
    print("Precio actualizado correctamente")

def actualizar_stock(Id, Stock):
    cursor.execute("UPDATE PRODUCTOS SET Stock = ? WHERE id = ?", (Stock, Id))
    if cursor.rowcount == 0:
        print("No existe un producto con ese id")
        return
    conexion.commit()
    print("Stock actualizado correctamente")

def eliminar_producto(Id):
    cursor.execute("DELETE FROM PRODUCTOS WHERE id = ?", (Id,))
    if cursor.rowcount == 0:
        print("No existe un producto con ese id")
        return
    conexion.commit()
    print("Producto eliminado correctamente")

def reporte_de_stock(Stock):
    cursor.execute("SELECT * FROM PRODUCTOS WHERE Stock < ?", (Stock,))
    productos = cursor.fetchall()
    if not productos:
        print("No hay productos con stock menor a ese valor")
        return
    print("\n Productos con Stock Bajo")
    for producto in productos:
        print(f"ID : {producto[0]} | Nombre : {producto[1]} | Categoria : {producto[2]} | Precio : {producto[3]} | Stock : {producto[4]}")

while True:
    print("\nAlmacen")
    print("1. Agregar Producto")
    print("2. Mostrar Producto.")
    print("3. Actualizar Producto")
    print("4. Eliminar Producto")
    print("5. Reporte de stock bajo")
    print("6. Salir")


    opcion = input("Elija lo que desea realizar :  ")
    print("\n ---------------------------")
    match opcion:
        case "1":
            Nombre_Producto = input("Ingresa el nombre del articulo : ")
            Categoria_Producto = input("Ingrese a que categoria pertenece el articulo : ")
            Precio_Producto = input("Ingrese el valor de venta del articulo : ")
            if not Precio_Producto.isdigit():
                print("Ingrese un valor numerico")
                continue
            Stock_Producto = input("Ingrese el stock del articulo : ")
            if not Stock_Producto.isdigit():
                print("Ingrese un valor numerico")
                continue
            agregar_producto(Nombre_Producto,Categoria_Producto,Precio_Producto,Stock_Producto)
        case "2":
            mostrar_producto()
        case "3":
            id_producto = input("¿Cual es el ID del producto a actualizar? :")
            if not id_producto.isdigit():
                print("Ingrese un valor numerico")
                continue
            actualizar = input("¿Que desea actualizar? Precio : 1 | Stock : 2  : ")
            if actualizar == "1":
                precio_actualizado = input("Ingrese el nuevo Precio de venta : ")
                if not precio_actualizado.isdigit():
                    print("Ingrese un valor numerico")
                    continue
                actualizar_precio(id_producto, precio_actualizado)
            elif actualizar == "2":
                Stock_actualizado = input("Ingrese el nuevo stock :")
                if not Stock_actualizado.isdigit():
                    print("Ingrese un valor numerico")
                    continue
                actualizar_stock(id_producto, Stock_actualizado)
            else:
                print("Ingrese una opcion correcta")
        case "4":
            id_producto = input("Ingrese el ID del producto a Eliminar : ") 
            if not id_producto.isdigit():
                print("Ingrese un valor numerico")
                continue
            eliminar_producto(id_producto)
        case "5":
            stockaconsultar = input("Ingrese el stock a consultar : ")           
            if not stockaconsultar.isdigit():
                print("Ingrese un valor numerico")
                continue
            else:
                print("Ingrese una opcion correcta")
            reporte_de_stock(int(stockaconsultar))
        case "6":
            conexion.close()
            break
        case _:
            print("Elija una opcion correcta")