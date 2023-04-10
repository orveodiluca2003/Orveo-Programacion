class Factura:
    def __init__(self, listaProductos, nombre, correo, subtotal, igtf, total,tiene_descuento):
        self.listaProductos = listaProductos
        self.nombre = nombre
        self.correo = correo
        self.subtotal = subtotal
        self.igtf = igtf
        self.total = total
        self.tiene_descuento = tiene_descuento
    
    def mostrar_factura(self): 
        print(f"""
Nombre: {self.nombre},
Correo: {self.correo},""")
        for producto in self.listaProductos: 
            print(f"Titulo: {producto.titulo} ,\nPrecio: {producto.precio_venta},")
        print(f"Total: {self.total}.\n")
    
