class Persona: 
    def __init__(self,nombre,rol,correo,cedula,cantidad_compra, super_total, compro, tiene_descuento):
        self.nombre= nombre
        self.rol = rol 
        self.correo = correo 
        self.cedula = cedula
        self.cantidad_compra = cantidad_compra
        self.super_total = super_total
        self.compro = compro
        self.tiene_descuento = tiene_descuento
    
    def mostrar(self):
        print (f"""
        Nombre: {self.nombre}
        Cantidad de compras: {self.cantidad_compra}
        Correo: {self.correo}
        Cedula: {self.cedula}
        Acumulado de compras: {self.super_total}$
        """)
    
    def obtenerStock(self):
        return (self.stock)
    
    def obtenerid(self): 
        return (self.id)


