from funciones import *
def main(): 
    generos_mas_vendidos = leer("generosMasVendidos.txt")
    artistas_mas_vendidos = leer("artistaMasVendido.txt")
    productos = leer("BDDPRODUCTOS.txt")
    personas = leer_persona()
    carrito = []
    factura = leer("BDDFACTURA.txt")
    
    while True:
        print("***BIENVENIDO***")
        opcion = input("Identifiquese \n 1. Dueño y/o Empleado \n 2. Cliente\n 3. Salir. \n ==> ")
        while not opcion in ["1", "2", "3"]:
            opcion = input("Ingrese una opcion valida: \n 1. Dueño y/o Empleado. \n 2. Cliente. \n 3. Salir. \n ==> ")

#DUEÑO
        if opcion == "1":
            contraseña = input("Ingrese la contraseña.  \n ==> ")
            while not contraseña == ("contraseña"):
                contraseña = input("Contraseña incorrecta, acceso denegado. \n ==> ")
            while (True):
                opcion_1 = input("Que desea hacer? \n 1. Mostrar productos. \n 2. Agregar producto nuevo. \n 3. Actualizar producto. \n 4. Eliminar producto. \n 5. Ver Estadisticas. \n 6. Salir. \n ==> ")
                while not opcion_1 in ["1", "2", "3", "4", "5", "6"]:
                    opcion_1 = input("Ingrese una opcion valida: \n 1. Mostrar productos. \n 2. Agregar producto nuevo. \n 3. Actualizar producto. \n 4. Eliminar producto. \n 5. Ver Estadisticas.\n 6. Salir \n ==> ")

                if opcion_1 == "1":
                    mostrar_disco(productos)
                    

                if opcion_1 == "2":
                    productos = agregar_productos(productos)
                    escribir_txt(productos)

                if opcion_1 == "3":
                    
                    id = int(input("Introduce el id del producto. \n ==> "))
                    nuevoStock = int(input("Introduce la nueva cantidad. \n ==> "))
                    actualizarstock(productos, nuevoStock, id)
                    

                if opcion_1 == "4":
                    id_eliminar = int(input("Introduce el id del producto. \n ==> "))
                    eliminar_disco(productos, id_eliminar)

                if opcion_1 == "5":
                    contraseña_1 = input("Ingrese la contraseña: ")
                    while not contraseña_1 == ("password"):
                        contraseña_1 = input("Contraseña incorrecta, acceso denegado. \n ==> ")
                    while (True):
                        opcion_1_1 = input("Que desea ver? \n 1. Ver Clientes \n 2. Top 3 clientes mas fieles. \n 3. Top 3 clientes que mas han gastado. \n 4. Top 3 generos mas vendidos. \n 5. Top 5 artistas mas vendidos. \n 6. Porcentaje de clientes registrados que no han completado una compra. \n 7. Ingreso bruto. \n 8. Ganancia neta. \n 9. Cantidad de ordenes regaladas. \n 10. Regresar. \n ==> ")
                        while not opcion_1_1 in ["1","2","3","4","5","6","7","8","9","10"]:
                            opcion_1_1 = input("Ingrese una opcion valida: \n 1. Ver Clientes \n 2. Top 3 clientes mas fieles. \n 3. Top 3 clientes que mas han gastado. \n 4. Top 3 generos mas vendidos. \n 5. Top 5 artistas mas vendidos. \n 6. Porcentaje de clientes registrados que no han completado una compra. \n 7. Ingreso bruto. \n 8. Ganancia neta. \n 9. Cantidad de ordenes regaladas. \n 10. Regresar. \n ==> ")

                        if opcion_1_1 == "1":
                            mostrar_persona(personas)

                        if opcion_1_1 == "2":
                            top_3_clientes_fieles(personas)

                        if opcion_1_1 == "3":
                            top_3_clientes_gastar(personas)

                        if opcion_1_1 == "4":
                            imprimir_generos_venidos(generos_mas_vendidos)

                        if opcion_1_1 == "5":
                            imprimir_artistas_venidos(artistas_mas_vendidos)

                        if opcion_1_1 == "6":
                            porcentaje_clientes(personas)

                        if opcion_1_1 == "7":
                            ingreso_bruto(factura)

                        if opcion_1_1 == "8":
                            ganancia_neta(factura)

                        if opcion_1_1 == "9":
                            ordenes_con_descuento(factura)

                        if opcion_1_1 == "10":
                            break

                if opcion_1 == "6":
                    break

            
#CLIENTE
        if opcion == "2": 

            opcion_2 = input("Ya tiene una cuenta? \n 1. Iniciar sesion. \n 2. Registrarse. \n ==> ")
            while not opcion_2 in ["1","2"]:
                opcion_2 = input("Ingrese una opcion valida: \n 1. Iniciar sesion. \n 2. Registrarse. \n ==> ")

            if opcion_2 == "1":
        
                correo = (input("Ingrese su correo electronico: "))
                personas = iniciar_sesion(personas,correo)
                clienteActual = obtenerCliente(correo, personas)
                
            if opcion_2 == "2":
                correo = (input("Ingrese su correo electronico: "))
                while not "@" in correo:
                    correo = input("Su correo no es valido: ")
                personas = registrar_persona(correo, personas)
                clienteActual = obtenerCliente(correo, personas)
                
                
            while (True):
                opcion_2_2 = input("Que desea hacer? \n 1. Ver Productos. \n 2. Agregar al carrito. \n 3. Eliminar del carrito. \n 4. Ver Carrito. \n 5. Checkout. \n 6. Cerrar Sesion. \n ==> ")
                while not opcion_2_2 in ["1","2","3","4","5","6"]:
                    opcion_2_2 = input("Ingrese una opcion valida: \n 1. Ver Productos. \n 2. Agregar al carrito. \n 3. Eliminar del carrito. \n 4. Ver Carrito. \n 5. Checkout. \n 6. Cerrar Sesion. \n ==> ")

                if opcion_2_2 == "1":
                    mostrar_disco_clientes(productos)
                    
                    opcion_2_2_1 = input("Filtrar por orden. \n 1. Alfabetico. \n 2. Precio (Mayor a menor) \n 3. Año (Mas reciente) \n 4. Por género \n 5. Regresar. \n ==> ")
                    while not opcion_2_2_1 in ["1","2","3","4","5"]:
                        opcion_2_2_1 = input("Ingrese una opcion valida: \n 1. Alfabeticamente. \n 2. Precio (Mayor a menor) \n 3. Año (Mas reciente) \n 4. Por género \n 5. Regresar. \n ==> ")

                    if opcion_2_2_1 == "1":
                        alfabeticamente(productos)

                    if opcion_2_2_1 == "2":
                        precio_menor_mayor(productos)

                    if opcion_2_2_1 == "3":
                        año_nuevo_viejo(productos)
                    
                    if opcion_2_2_1 == "4": 
                        mostrar_genero(productos)

                    if opcion_2_2_1 == "5":
                        pass

                if opcion_2_2 == "2":
                    agregar_carrito(carrito, productos)
                    
                if opcion_2_2 == "3":
                    eliminar_carrito(carrito, productos)
                
                if opcion_2_2 == "4":
                    mostrar_carrito_cliente(carrito)
                    
                if opcion_2_2 == "5":
                    checkout(carrito, productos, clienteActual, factura, personas, generos_mas_vendidos, artistas_mas_vendidos)
                    
                if opcion_2_2 == "6":
                    break
 
        if opcion == '3':
            print("Saliendo.....") 
            break
        else: 
            continue

main()
