from models import *

print("--- REGISTRO MANUAL DE OBJETOS (EVIDENCIA 10 OBJETOS POR CLASE) ---")


print("\n--- REGISTRO MANUAL DE USUARIOS (10 OBJETOS) ---")
usuarios = [
    Usuario(1, "Carlos88", "charles@mail.com", "555-01", 150),
    Usuario(2, "Ana_G", "ana@mail.com", "555-02", 0),
    Usuario(3, "Roberto", "rober@mail.com", "555-03", 50),
    Usuario(4, "Lucia", "lu@mail.com", "555-04", 200),
    Usuario(5, "Admin_User", "admin@cine.com", "555-05", 10),
    Usuario(6, "Maria22", "maria@mail.com", "555-06", 80),
    Usuario(7, "Jose_L", "jose@mail.com", "555-07", 30),
    Usuario(8, "Karla_V", "karla@mail.com", "555-08", 120),
    Usuario(9, "Fer_H", "fer@mail.com", "555-09", 0),
    Usuario(10, "User_Final", "last@mail.com", "555-10", 5)
]

for u in usuarios:
    print(u)


print("\n--- REGISTRO MANUAL DE PELÍCULAS (10 OBJETOS) ---")
peliculas = [
    Pelicula("Dune: Part Two", 166, "B"),
    Pelicula("Oppenheimer", 180, "C"),
    Pelicula("Barbie", 114, "A"),
    Pelicula("Kung Fu Panda 4", 94, "A"),
    Pelicula("Civil War", 109, "C"),
    Pelicula("Godzilla x Kong", 115, "B"),
    Pelicula("Ghostbusters", 115, "B"),
    Pelicula("Poor Things", 141, "C"),
    Pelicula("The Fall Guy", 126, "B"),
    Pelicula("Furiosa", 148, "C")
]

for p in peliculas:
    print(p)


print("\n--- REGISTRO MANUAL DE SALAS (10 OBJETOS) ---")
salas = [
    Sala("01", "IMAX", 100),
    Sala("02", "3D", 80),
    Sala("03", "2D", 120),
    Sala("04", "IMAX", 100),
    Sala("05", "VIP", 50),
    Sala("06", "4DX", 60),
    Sala("07", "2D", 90),
    Sala("08", "3D", 85),
    Sala("09", "IMAX", 100),
    Sala("10", "Estándar", 150)
]

for s in salas:
    print(s)


print("\n--- REGISTRO MANUAL DE FUNCIONES (10 OBJETOS) ---")
funciones = [
    Funcion(101, peliculas[0], salas[0], "20:00", 150.0),
    Funcion(102, peliculas[1], salas[1], "18:30", 140.0),
    Funcion(103, peliculas[2], salas[2], "16:15", 120.0),
    Funcion(104, peliculas[3], salas[3], "14:00", 110.0),
    Funcion(105, peliculas[4], salas[4], "21:45", 160.0),
    Funcion(106, peliculas[5], salas[5], "19:20", 155.0),
    Funcion(107, peliculas[6], salas[6], "22:10", 135.0),
    Funcion(108, peliculas[7], salas[7], "17:00", 145.0),
    Funcion(109, peliculas[8], salas[8], "15:30", 125.0),
    Funcion(110, peliculas[9], salas[9], "23:00", 140.0)
]

for f in funciones:
    print(f)

print("\n--- REGISTRO DE PROMOCIONES DISPONIBLES ---")
promociones = [
    Promocion("PROMO_ESTUDIANTE", 20),
    Promocion("PROMO_FAMILIA", 15),
    Promocion("PROMO_MARTES", 25),
    Promocion("PROMO_VIP", 30),
    Promocion("PROMO_CINE", 10)
]

for promo in promociones:
    print(promo)

print("\n--- VALIDACIÓN DE DATOS FINALIZADA ---")


print("\n>>> INICIANDO PROCESO DE RESERVA...")


u_actual = usuarios[1]
peli = peliculas[0]
sala = salas[0]
func = funciones[0]

print(f"Usuario: {u_actual.nombre} (Puntos: {u_actual.puntosFidelidad})")
print(f"Película: '{peli.titulo}' | Sala: {sala.idSala} ({sala.tipo})")


print("Seleccione sus asientos (separados por coma): A1, A2, B5")
print("\n[SISTEMA]: Verificando disponibilidad...")


lista_asientos = ["A1", "A2", "B5"]
asientos_ocupados = sala.verificar_disponibilidad(lista_asientos)

if asientos_ocupados:
    for asiento in asientos_ocupados:
        print(f"[ERROR]: El asiento {asiento} ya está ocupado por la Reserva #882.")
    
    print("[SISTEMA]: Por favor, seleccione asientos disponibles.")
    
    
    print("Seleccione sus asientos: A1, A3, B5")
    lista_asientos = ["A1", "A3", "B5"]
    asientos_ocupados = sala.verificar_disponibilidad(lista_asientos)
    
    if not asientos_ocupados:
        print(f"[OK]: Asientos {', '.join(lista_asientos)} bloqueados con éxito.")
    else:
        print("[ERROR]: Algunos asientos siguen ocupados. Cancelando reserva.")
        exit()


res = Reserva(995, u_actual, func, lista_asientos)
print(f"Monto base: ${res.monto:.2f}")


print("\n>>> APLICANDO GESTIÓN COMERCIAL...")
print("¿Cuenta con código de promoción?: SI")
codigo = "PROMO_ESTUDIANTE"
print(f"Código: {codigo}")


promo = Promocion.buscar_por_codigo(codigo, promociones)

if promo:
    ahorro = res.aplicar_promo(codigo, promo)
    if ahorro > 0:
        print(f"[SISTEMA]: Validando código... ¡ÉXITO! (Descuento del {promo.porcentaje}% aplicado).")
else:
    print("[SISTEMA]: Código no válido.")
    ahorro = 0

res.estado = "PAGADA"

print(f"\nResumen de Reserva #{res.idReserva}:")
print("----------------------------------")
print(f"Usuario: {res.user.nombre}")
print(f"Función: {res.funcion.pelicula.titulo} ({res.funcion.horario} hrs)")
print(f"Asientos: [{', '.join(res.asientos)}]")
print(f"Total Final: ${res.monto:.2f} (Ahorraste ${ahorro:.2f})")
print("--------------------------------------")
print(f"Estado: {res.estado}. Ticket generado en PDF.")