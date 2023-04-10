import pickle
from Productos import *
import random as rd
from Persona import * 
from Factura import *
import collections

#--------------------------------------------------------PRODUCTOS (DISCOS)------------------------------------------------------------------
#ESTE MODULO SOLO PUEDEN ENTRAR LOS EMPLEADOS Y LOS DUEÑOS.
def agregar_productos(productos): 
    #esta función nos permite agregar los productos que vayan llegando a la tienda
    id = rd.randint(1,999)
    cantidad = 0
    discos_vendidos=0
    titulo = input("Introduce el titulo del albúm : ").title()
    while titulo.isnumeric(): 
        print("Invalido ingrese nuevamente el titulo (solo caracteres)")
        titulo = input("Introduce el titulo del albúm  : ").title()

    artista = input("Introduce el artista : ").title()
    while artista.isnumeric(): 
        print("Invalido ingrese nuevamente el artista (solo caracteres)")
        artista = input("Introduce el artista : ").title()
    
    ano_publicacion = input("Introduce el año de publicacion : ")
    while ano_publicacion.isalpha(): 
        print("Invalido ingrese nuevamente el año de publicacion (solo numeros)")
        ano_publicacion = input("Introduce el año de publicacion : ")
    
    costo = input("Introduce el costo : ")
    while costo.isalpha(): 
        print("Invalido ingrese nuevamente el costo (solo numeros)")
        costo = input("Introduce el costo : ")
    costo = float(costo)

    precio_venta = input("Introduce el precio de venta : ")
    while precio_venta.isalpha(): 
        print("Invalido ingrese nuevamente el precio de venta (solo numeros)")
        precio_venta = input("Introduce el precio de venta : ")
    precio_venta = float(precio_venta)

    stock = input("Ingrese el stock del producto : ")
    while stock.isalpha(): 
        print("Invalido ingrese nuevamente el stock (solo numeros)")
        stock = input("Ingrese el stock del producto : ")
    stock = int(stock)

    genero = input("Introduce el genero del disco : ").title()
    while genero.isnumeric(): 
        print("Invalido ingrese nuevamente el genero (solo caracteres)")
        genero = input("Introduce el artista : ").title()

    nuevo_disco = Producto(id,titulo,artista,ano_publicacion,costo,precio_venta,stock,genero, cantidad, discos_vendidos)
    productos.append(nuevo_disco)
    
    print("-----Nuevo disco generado-----")

    nuevo_disco.mostrar()
    return productos

def actualizarstock(productos,nuevo_stock,id): 
    #esta función tiene una utilidad de actualizar el stock de los discos, cuándo el stock sea 0 elimina ese disco
    vaciar_txt('BDDPRODUCTOS.txt')
    for product in productos: 
        if id == product.id:
            if nuevo_stock == 0:
                    productos.remove(product)
                    
            else:
                product.stock = nuevo_stock
            
    añadir_txt(productos)

def mostrar_disco(productos): 
    #esta funcion permite recorrer la lista de discos que tenemos guardada en el txt.
    for producto in productos: 
        print("==================================")
        producto.mostrar()

def eliminar_disco(productos, id_eliminar): 
    #esta funcion elimina el disco que introduce el dueño o el empleado. 
    vaciar_txt('BDDPRODUCTOS.txt')
    counterA = 0
    counterB = 0
    for producto in productos:
        counterA += 1
        counterB += 1

    for producto in productos:
        if id_eliminar == producto.id:
            productos.remove(producto)
            counterA -= 1
            print("Se ha eliminado el disco.")
        
    if counterA == counterB:
        print("No se encontro el id ingresado.")
            
    añadir_txt(productos)    

def escribir_txt(datos): 
    #esta función nos permite escribir en el archivo txt que se estará guardando los discos
    archivo = open("BDDPRODUCTOS.txt","wb") 
    pickle.dump(datos,archivo)
    archivo.close()

def vaciar_txt(nombre_txt):
    #esta funcion permite vaciar el txt commpleto. 
    archivo = open(nombre_txt,"w") 
    archivo.write('')
    archivo.close()

def añadir_txt(datos):
    #esta funcion permite añadir los objetos al txt.
    archivo = open("BDDPRODUCTOS.txt","ab") 
    pickle.dump(datos,archivo)
    archivo.close()

def leer_stock():
    #esta funcion nos permite leer los discos que se encuentran en el txt.
    archivo = open("BDDPRODUCTOS.txt", 'rb')
    datos = pickle.load(archivo)
    return datos

def obtener(txt_name):
    #Esta función nor sirve para obtener los nombres de los artistas. 
    archivo = open(txt_name, 'rb')
    line= pickle.load(archivo)
    archivo.close()
    return line

def precio_menor_mayor(productos):
    #esta funcion permite ordenar los discos por su precio de venta. 
    productos.sort(key = lambda x:x.precio_venta) 
    mostrar_disco_clientes(productos)

def año_nuevo_viejo(productos):
    #esta funcion sirve para ordenar los discos por año de publicacion
    productos.sort(key = lambda x:x.ano_publicacion)
    mostrar_disco_clientes(productos)

def alfabeticamente(productos):
    #esta funcion permite ordenar los discos por el titulo. 
    productos.sort(key = lambda x:x.titulo)
    mostrar_disco_clientes(productos)

def mostrar_genero(productos):
    #esta funcion sirve para buscar el genero deseado introducido por el usuario.
    genero = input("Introduce el genero que desea buscar.\n ==> ").title()
    for producto in productos: 
        if genero == producto.genero: 
            producto.mostrar_cliente() 


#--------------------------------------------------------VENTA (CARRITO,PERSONA)-------------------------------------------------------------------------------

def registrar_persona(correo, personas):
    #esta función permite registrar a la persona. 
        super_total = 0
        cantidad_compra = 0
        compro = False
        tiene_descuento = False
        nombre = input("Ingrese su nombre: ").title()
        while not nombre.isalpha():
            nombre = input("Utilice solo letras: ").title()
        
        rol = "Cliente"

        cedula = input("Ingrese su numero de cedula: ")
        while not cedula.isnumeric():
            cedula = input("Utilice solo numeros: ")

        nueva_persona = Persona(nombre,rol,correo,cedula, cantidad_compra, super_total, compro, tiene_descuento)
        personas.append(nueva_persona)
        print("-----Se ha registrado exitosamente-----")

        nueva_persona.mostrar()
        escribir_txt_personas(personas)
        return personas

def iniciar_sesion(personas,correo):
    #esta funcion sirve para cuándo la persona esté iniciando sesión  
    for persona in personas: 
        if correo == persona.correo: 
            return personas
             
    print("Usted no está registrado.")
    correo = (input("Ingrese su correo electronico: "))
    while not "@" in correo:
        correo = input("Su correo no es valido: ")
    registrar_persona(correo,personas)
    return personas
        
def mostrar_persona(personas):
    # esta funcion sirve para mostrar a las personas registradas.
    for persona in personas: 
        print("==================================")
        persona.mostrar()

def escribir_txt_personas(datos): 
    #esta función nos permite escribir en el archivo txt que se estará guardando los discos
    archivo = open("BDDPERSONAS.txt","wb") 
    pickle.dump(datos,archivo)
    archivo.close()

def leer_persona():
    #esta funcion nos permite leer a las personas que se encuentran en el txt.
    archivo = open("BDDPERSONAS.txt", 'rb')
    datos = pickle.load(archivo)
    return datos

def agregar_carrito(carrito,productos): 
    #esta funcion permite agregar los objetos a la lista carrito. 
    id = int(input("Introduce el Id del disco que desea comprar.\n ==> "))
    contador1 = contador2 = 0
    for producto in productos:
        contador1+=1
        contador2+=1
        if id == producto.id: 
            cantidad = int(input("Introduce la cantidad que deseas llevar.\n ==> "))
            contador1-=1
            
            while cantidad > producto.stock:
                cantidad = int(input("Cantidad insuficiente, por favor coloca una cantidad menor. \n ==> "))
            producto.cantidad = cantidad
            carrito.append(producto)
    if contador1==contador2:
        print("No se encontro el ID ingresado.")

def ver_carrito(carrito):
    #esta funcion permite ver el carrito. 
    for carritos in carrito: 
        carritos.mostrar()
    
def eliminar_carrito(carrito,productos):
    # esta funcion sirve por si el cliente quiere eliminar algun disco de su carrito. 
    id = int(input("Introduzca el Id que desea eliminar. \n ==> "))
    contador1 = contador2 = 0
    for producto in productos:
        contador1 += 1
        contador2 += 1
        if id == producto.id:
            contador1-=1
            carrito.remove(producto)
            print("Se ha eliminado del carrito")
    if contador1 == contador2:
        print("No se encontro el ID ingresado.")

def mostrar_carrito_cliente(carrito): 
    # esta funcion permite visualizar el carrito del cliente. 
    if (not esListaVacia(carrito)):
        for carritos in carrito: 
            print(f"Titulo: {carritos.titulo}\nPrecio por unidad: {carritos.precio_venta} \nCantidad: {carritos.cantidad}")
    else:
        print("No tienes discos agregados al carrito.")

def arreglar(facturas): 
    #esta funcion nos ayudo a arreglar el txt, para agregarle el atributo cantidad a todos los objeto. 
    vaciar_txt('BDDFACTURA.txt') #vacia el txt y crea una nueva lista. 
    producta=[]
    for  factura in facturas:  
        factura.tiene_descuento = False
        nuevoAlbum = Factura(factura.listaProductos, factura.nombre, factura.correo, factura.subtotal, factura.igtf, factura.total, factura.tiene_descuento)
        producta.append(nuevoAlbum)
            
    escribir_en_txt(producta, "BDDFACTURA.txt")

def mostrar_disco_clientes(productos):
    #esta funcion permite recorrer la lista de discos que tenemos guardada en el txt.
    for producto in productos: 
        print("==================================")
        producto.mostrar_cliente()

def checkout(carrito,productos, clienteActual, factura, personas, genero_mas_vendido, artistas_mas_vendidos):
    #esta funcion permite que cuando la persona quiere hacer el checkout muestre la factura. 
    if (not esListaVacia(carrito)):
        print("==============================")
        print("****FACTURA****")
        subtotal = 0
        listaProductos= []
        for carritos in carrito:
            listaProductos.append(carritos)
            top_3_generos_vendidos(carritos, genero_mas_vendido)
            top_5_artistas_vendidos(carritos, artistas_mas_vendidos)
            if(tieneDescuento(carritos)):
                subtotal=0
                clienteActual.tiene_descuento = True
                print("Felicidades acabas de obtener un desecuento del 100%.")
                break
            else: 
                subtotal += carritos.cantidad * carritos.precio_venta
            actualizarstock(productos,carritos.stock - carritos.cantidad, carritos.id)
        vaciar_txt("generosMasVendidos.txt")
        vaciar_txt("artistaMasVendido.txt")
        escribir_en_txt(genero_mas_vendido, "generosMasVendidos.txt")
        escribir_en_txt(artistas_mas_vendidos, "artistaMasVendido.txt")
        print("Cliente:", clienteActual.nombre)
        print("Correo:", clienteActual.correo)
        mostrar_carrito_cliente(carrito)
        print("Subtotal:", subtotal)
        igtf = round(subtotal * 0.03,2)
        print("3% IGTF:", igtf)
        total = round(igtf + subtotal,2)
        print("TOTAL:", total)
        
        print("==============================")

        #Creacion y almacenamiento de objetos facturas en el txt
        clienteActual.cantidad_compra+=1
        clienteActual.super_total += total
        clienteActual.compro = True
        for persona in personas:
            if persona.nombre == clienteActual.nombre:
                persona = clienteActual
        
        vaciar_txt("BDDPERSONAS.txt")
        escribir_en_txt(personas, "BDDPERSONAS.txt")


        nuevaFactura = Factura(listaProductos, clienteActual.nombre, clienteActual.correo, subtotal, igtf, total, clienteActual.tiene_descuento)
        factura.append(nuevaFactura)
        escribir_en_txt(factura, "BDDFACTURA.txt")
        carrito.clear()
    else:
        print("No tienes agregados discos a tu carrito.")

def obtenerCliente(correo, personas):
    #esta funcion nos sirve para obtener los correos de los clientes.
    for persona in personas:
        if correo == str(persona.correo):
            return persona

def tieneDescuento(carritos):
    #Esta funcion sirve para sumar los id y si su resultado del id es igual a 7 tiene descuento.
    listaID= [ch for ch in str(carritos.id)]
    print(listaID)
    suma = 0
    for x in listaID:
        x = x.replace("'","")
        suma += int(x)
    if(suma == 7):
        return True
    return False

def escribir_en_txt(datos, ubicacion): 
    #esta función nos permite escribir en el archivo txt que se estará guardando los discos
    archivo = open(ubicacion,"wb") 
    pickle.dump(datos,archivo)
    archivo.close()

def leer(ubicacion):
    #esta funcion nos permite leer los discos que se encuentran en el txt.
    archivo = open(ubicacion, 'rb')
    datos = pickle.load(archivo)
    return datos

def leer_cliente(datos,ubicacion): 
    #esta funcion permite leer los clientes que se encuentran en el txt. 
    archivo = open(ubicacion,"rb") 
    pickle.dump(datos,archivo)
    archivo.close()

def esListaVacia(lista):
    #esta funcion retorna true si la lista está vacia.
    if (len(lista) == 0):
        return True
    return False

def mostrar_clientes(personas): 
    #esta funcion permite mostrar los clientes. 
    for persona in personas: 
        persona.mostrar()

#--------------------------------------------------------MODULO DE ESTADISTICAS--------------------------------------------------------
#EN ESTE MODULO SOLO PUEDE ENTRAR LOS DUEÑOS DE LA TIENDA.
def top_3_clientes_fieles(personas):
    #esta funcion permite visualizar los 3 clientes mas fieles de la tienda. 
    personas.sort(key = lambda x:x.cantidad_compra)
    personas.reverse()
    contador=0
    for persona in personas:
        contador+=1
        if contador <=3:
            persona.mostrar()
        else:
            break

def top_3_clientes_gastar(personas):
    #esta funcion permite ver los clientes que mas han gastado. 
    personas.sort(key = lambda x:x.super_total)
    personas.reverse()
    contador = 0 
    for persona in personas:
        contador += 1
        if contador <= 3: 
            persona.mostrar()
        else: 
            break

def top_3_generos_vendidos(carritos, genero_mas_vendido):
    # esta función permite visualizar los 3 generos mas vendidos. 
    for genero,cantidad in genero_mas_vendido.items():
        cantida=int(cantidad)+int(carritos.cantidad)
        if (genero).title() == (carritos.genero).title():
            genero_mas_vendido[genero]=cantida
            return genero_mas_vendido
    genero_mas_vendido[carritos.genero]=carritos.cantidad
    return genero_mas_vendido

def imprimir_generos_venidos(genero_mas_vendido):
    #esta funcion permite imprimir los generos mas vendidos. 
    diccionario_ordenado = collections.OrderedDict(sorted(genero_mas_vendido.items(), key=lambda x:x[1],reverse=True))
    
    contador = 0
    for key, value in diccionario_ordenado.items():
        contador +=1
        if contador<=3:
            print(key, value)
        else:
            break
   
def top_5_artistas_vendidos(carritos, artistas_mas_vendidos):
    #esta funcion permite ver los 5 artistas mas vendidos. 
    for artista,cantidad in artistas_mas_vendidos.items():
        cantida=int(cantidad)+int(carritos.cantidad)
        if (artista).title() == (carritos.artista).title():
            artistas_mas_vendidos[artista]=cantida
            return artistas_mas_vendidos
    artistas_mas_vendidos[carritos.artista]=carritos.cantidad
    return artistas_mas_vendidos

def imprimir_artistas_venidos(artistas_mas_vendidos):
    #Esta funcion imprime los artistas vendidos. 
    diccionario_ordenado = collections.OrderedDict(sorted(artistas_mas_vendidos.items(), key=lambda x:x[1],reverse=True))
    contador = 0
    for key, value in diccionario_ordenado.items():
        contador +=1
        if contador<=5:
            print(key, value)
        else:
            break
    
def porcentaje_clientes(personas):
    #esta funcion calcula e imprime el porcentaje de los clientes que se registraron pero no compraron. 
    contador_comprado = 0
    total_contador = 0
    for persona in personas:
        total_contador += 1
        if persona.compro:
            contador_comprado += 1
    print("El porcentaje de personas que se registro y no compro es", round((1-(contador_comprado/total_contador))*100,2), "%")

def ingreso_bruto (facturas):
    #esta función calcula y muestra el ingreso bruto de la tienda. 
    ingreso_total = 0
    for factura in facturas:
            ingreso_total += factura.total
    print(f"El ingreso bruto es: {ingreso_total} $")
    return ingreso_total
    
def ganancia_neta(facturas):
    #esta función permite calcular y visualizar la ganancia neta. 
    ingreso_total = 0
    for factura in facturas:
            ingreso_total += factura.total
    costo_total = 0
    for factura in facturas:
        for disco in factura.listaProductos:
            costo_total += disco.costo
    print(f"La ganancia neta de la tienda es de:", round(ingreso_total-costo_total,2))

def ordenes_con_descuento(facturas):
    #esta función calcula las ordenes de los clientes con el descuento. 
    contador_ordenes_con_descuento = 0
    for factura in facturas:
        if factura.tiene_descuento:
            contador_ordenes_con_descuento+=1
    print(f"La cantidad de ordenes que se regalaron son: : {contador_ordenes_con_descuento}")

