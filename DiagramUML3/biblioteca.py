class Material:
    def __init__(self, idMaterial: int, titulo: str, añoPublicacion: int, disponible: bool):
        self.idMaterial = idMaterial
        self.titulo = titulo
        self.añoPublicacion = añoPublicacion
        self.disponible = disponible

class Libro(Material):
    def __init__(self, idMaterial, titulo, año, disponible, autor, isbn, genero):
        super().__init__(idMaterial, titulo, año, disponible)
        self.autor = autor
        self.isbn = isbn
        self.genero = genero

class Revista(Material):
    def __init__(self, idMaterial, titulo, año, disponible, edicion, periodicidad):
        super().__init__(idMaterial, titulo, año, disponible)
        self.edicion = edicion
        self.periodicidad = periodicidad

class MaterialDigital(Material):
    def __init__(self, idMaterial, titulo, año, disponible, tipoArchivo, urlDescarga, tamañoMB):
        super().__init__(idMaterial, titulo, año, disponible)
        self.tipoArchivo = tipoArchivo
        self.urlDescarga = urlDescarga
        self.tamañoMB = tamañoMB


class Persona:
    def __init__(self, nombre: str):
        self.nombre = nombre

class Usuario(Persona):
    def __init__(self, nombre: str, limitePrestamos: int):
        super().__init__(nombre)
        self.limitePrestamos = limitePrestamos
        self.listaActiva = [] 

class Bibliotecario(Persona):
    def __init__(self, nombre: str):
        super().__init__(nombre)

    def gestionarPrestamo(self, usuario, material, id_p, f_inicio, f_fin):
        if material.disponible:
            material.disponible = False
            nuevo_p = Prestamo(id_p, f_inicio, f_fin, usuario, material)
            usuario.listaActiva.append(nuevo_p)
            return nuevo_p
        return None

    def transferirMaterial(self, material, sucursalDestino):
        return f" El material '{material.titulo}' ha sido movido a la sede: {sucursalDestino.nombre}"

class Sucursal:
    def __init__(self, idSucursal: int, nombre: str):
        self.idSucursal = idSucursal
        self.nombre = nombre
        self.catalogoLocal = [] 


class Prestamo:
    def __init__(self, idPrestamo: int, fechaInicio, fechaDevolucion, usuario, material):
        self.idPrestamo = idPrestamo
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.usuario = usuario
        self.material = material

class Penalizacion:
    def __init__(self, monto: float, motivo: str, pagada: bool):
        self.monto = monto
        self.motivo = motivo
        self.pagada = pagada

    def calcularMulta(self, dias_retraso):
        self.monto = dias_retraso * 15.0
        return self.monto

    def bloquearUsuario(self, usuario):
        if not self.pagada:
            return f"SEGURIDAD: El usuario {usuario.nombre} ha sido BLOQUEADO por falta de pago."
        return f"SEGURIDAD: El usuario {usuario.nombre} está al día."

class Catalogo:
    def buscarEnTodasSucursales(self, titulo_buscado, lista_sedes):
        for sede in lista_sedes:
            for material in sede.catalogoLocal:
                if material.titulo.lower() == titulo_buscado.lower():
                    return f"ENCONTRADO: '{material.titulo}' está en la sede '{sede.nombre}'."
        return "RESULTADO: No se encontró el material en ninguna sucursal."