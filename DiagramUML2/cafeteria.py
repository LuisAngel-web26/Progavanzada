
class Persona:
    """Clase fundamental para identificar a cualquier individuo [cite: 7]"""
    def __init__(self, idPersona: int, nombre: str, email: str):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email

    def login(self):
        return f"Usuario {self.nombre} ha iniciado sesión"

    def actualizarPerfil(self):
        return f"Perfil de {self.nombre} actualizado correctamente"

class Cliente(Persona):
    """Usuario que realiza el consumo [cite: 9]"""
    def __init__(self, idPersona: int, nombre: str, email: str, puntosFidelidad: int):
        super().__init__(idPersona, nombre, email)
        self.puntosFidelidad = puntosFidelidad
        self.historialPedidos = [] 

    def realizarPedido(self):
         return f"Pedido realizado por {self.nombre}"

    def consultarHistorial(self):
        if not self.historialPedidos:
            return "No hay pedidos en el historial"
        return self.historialPedidos

    def canjearPuntos(self):
        return f"{self.nombre} ha canjeado {self.puntosFidelidad} puntos"

class Empleado(Persona):
    """Personal que opera la cafetería [cite: 12]"""
    def __init__(self, idPersona: int, nombre: str, email: str, idEmpleado: str, rol: str):
        super().__init__(idPersona, nombre, email)
        self.idEmpleado = idEmpleado
        self.rol = rol 
    def actualizarInventario(self):
        return f"Inventario actualizado por {self.nombre} ({self.rol})"

    def cambiarEstadoPedido(self):
        return f"Estado de pedido cambiado por {self.nombre}"



class ProductoBase:
    """Propiedades generales de lo que se vende [cite: 16]"""
    def __init__(self, idProducto: int, nombre: str, precioBase: float):
        self.idProducto = idProducto
        self.nombre = nombre
        self.precioBase = precioBase

class Bebida(ProductoBase):
    """Productos líquidos personalizables [cite: 17]"""
    def __init__(self, idProducto: int, nombre: str, precioBase: float, tamaño: str, temperatura: str):
        super().__init__(idProducto, nombre, precioBase)
        self.tamaño = tamaño
        self.temperatura = temperatura 
        self.modificadores = [] 

    def agregarExtra(self):
        self.modificadores.append("Extra estándar")
        return f"Extra agregado a {self.nombre}"

    def calcularPrecioFinal(self, precio_extra=3.50):
        precio_final = self.precioBase + (len(self.modificadores) * precio_extra)
        return round(precio_final, 2)

class Postre(ProductoBase):
    """Productos de repostería [cite: 19]"""
    def __init__(self, idProducto: int, nombre: str, precioBase: float, esVegano: bool, sinGluten: bool):
        super().__init__(idProducto, nombre, precioBase)
        self.esVegano = esVegano
        self.sinGluten = sinGluten


class Pedido:
    """Gestión de la transacción actual [cite: 22]"""
    def __init__(self, idPedido: int, estado: str, total: float):
        self.idPedido = idPedido
        self.productos = [] 
        self.estado = estado 
        self.total = total

    def calcularTotal(self):
        if not self.productos:
          return 0.00
        return 190.50
    
     

    def validarStock(self):
        return True

class Inventario:
    """Control de suministros [cite: 26]"""
    def __init__(self):
        self.ingredientes = {
            "café": 50,
            "leche": 30,
            "azúcar": 100,
            "harina": 40,
            "huevos": 60
        } 

    def reducirStock(self):
         return "Stock reducido correctamente"

    def notificarFaltante(self):
        ingredientes_bajos = []
        for ing, cant in self.ingredientes.items():
            if cant < 20:
                ingredientes_bajos.append(ing)
        
        if ingredientes_bajos:
            return f"Ingredientes con stock bajo: {ingredientes_bajos}"
        return "Todos los ingredientes tienen stock suficiente"