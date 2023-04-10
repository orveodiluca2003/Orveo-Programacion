class Producto: 
    def __init__(self,id,titulo,artista,ano_publicacion,costo,precio_ventana,stock,genero, cantidad, discos_vendidos):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.ano_publicacion = ano_publicacion
        self.costo = costo 
        self.precio_venta = precio_ventana
        self.stock = stock
        self.genero = genero
        self.cantidad = cantidad
        self.discos_vendidos = discos_vendidos


    def mostrar(self): 
        print(f"ID: {self.id} ,\nTitulo: {self.titulo} ,\nArtista: {self.artista} ,\nAno: {self.ano_publicacion} ,\nCosto: {self.costo} ,\nPrecio: {self.precio_venta} ,\nStock: {self.stock} ,\nGenero: {self.genero}\n")
    


    #Para mostrar los albunes a los clientes
    def mostrar_cliente(self): 
        print(f"ID: {self.id} ,\nTitulo: {self.titulo} ,\nArtista: {self.artista} ,\nAno: {self.ano_publicacion} ,\nPrecio: {self.precio_venta} ,\nStock: {self.stock} ,\nGenero: {self.genero}\n")
    
    def obtenerStock(self):
        return (self.stock)
    
    def obtenerid(self): 
        return (self.id)

