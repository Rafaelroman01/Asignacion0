# Definicion de la clase:
class Clientes():
   
    # Atributos de Clase:
    pais ="Argentina" 
    
     
    # Constructor de la clase: 
    def __init__(self, nombre, email, edad, productos):
        
        # Atributos de Instancia
        # Decorar Objeto:
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.productos = productos
        
    # Metodos Propios:
    def registrar(self, registro):
        self.registro = registro
        return("Se ha registrado el cliente: ")
    
    def comprar(self, productos, tienda):
        self.productos = productos
        self.tienda = tienda
        
    def mostrar_pedido(self):
        return (f"Su pedido es: {self.productos}: ")
        
    #Uso el metodo Str para qe me retorne un string:
    
    def __str__(self):
        # Debe retornar si o si un string:
        return (f"El cliente {self.nombre}, ha comprado {self.productos}, en la tienda {self.tienda}.\n Se le ha mandado un correo con su factura a: {self.email}")


# Instanciamos el objeto(crear):
cliente1 = Clientes("Juan", "Profecoder.com", "30", ["Tecnologia", "Moda", "Farmacia"])
cliente2 = Clientes("Carlos Perez", "carlosperez0365@gmail.com", "35", ["Tecnologia", "Moda", "Farmacia"])
cliente3 = Clientes("Luis Suarez", "luissuarez2345@gmail.com", "38", ["Tecnologia", "Moda", "Farmacia"])
cliente4 = Clientes("Marta Sanchez", "martasanchez0934@gmail.com", "61", ["Tecnologia", "Moda", "Farmacia"])

cliente1.comprar("Lapto", "Walmart")

print(cliente1)



#print(cliente1.nombre, cliente1.email, cliente1.edad, cliente1.productos)       

#return ("Nombre: {self.nombre} - Email: {self.email} - Edad: {self.edad} - Productos: {self.productos}")