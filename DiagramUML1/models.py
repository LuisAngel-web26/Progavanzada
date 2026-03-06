import datetime

class Persona:
    def __init__(self, id_p, nom, mail, telf):
        self.idPersona = id_p
        self.nombre = nom
        self.email = mail
        self.telefono = telf

class Usuario(Persona):
    def __init__(self, id_p, nom, mail, telf, pts=0):
        Persona.__init__(self, id_p, nom, mail, telf)
        self.puntosFidelidad = pts
        self.historial = []

    def __str__(self):
        return f"ID: {self.idPersona} | {self.nombre} (Puntos: {self.puntosFidelidad})"

class Pelicula:
    def __init__(self, titulo, duracion, clasif):
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasif

    def __str__(self):
        return f"Peli: {self.titulo} ({self.duracion} min) - Clas: {self.clasificacion}"

class Sala:
    def __init__(self, id_s, tipo, cap):
        self.idSala = id_s
        self.tipo = tipo
        self.capacidad = cap
        self.asientos_ocupados = ["A2"] 

    def verificar_disponibilidad(self, asientos):
        """Verifica si algún asiento está ocupado"""
        ocupados = []
        for asiento in asientos:
            if asiento in self.asientos_ocupados:
                ocupados.append(asiento)
        return ocupados
    
    def __str__(self):
        return f"Sala: {self.idSala} | {self.tipo} | Capacidad: {self.capacidad}"

class Funcion:
    def __init__(self, id_f, peli, sala, hora, precio):
        self.id_func = id_f
        self.pelicula = peli
        self.sala = sala
        self.horario = hora
        self.precioBase = precio

    def __str__(self):
        return f"Función {self.id_func}: {self.pelicula.titulo} - Sala {self.sala.idSala} {self.horario} hrs ${self.precioBase:.2f}"

class Promocion:
    def __init__(self, codigo, descuento):
        self.cod = codigo
        self.porcentaje = descuento

    def __str__(self):
        return f"Promo: {self.cod} ({self.porcentaje}% descuento)"

class Reserva:
    def __init__(self, id_r, usuario, funcion, asientos):
        self.idReserva = id_r
        self.user = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.monto = funcion.precioBase * len(asientos)
        self.estado = "PENDIENTE"

    def aplicar_promo(self, codigo_ingresado, promo_obj):
        if codigo_ingresado == promo_obj.cod:
            ahorro = self.monto * (promo_obj.porcentaje / 100)
            self.monto -= ahorro
            return ahorro
        return 0

    def __str__(self):
        return f"Reserva #{self.idReserva}: {self.user.nombre} - {len(self.asientos)} asientos - ${self.monto:.2f} - {self.estado}"
