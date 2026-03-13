from cafeteria import *

def probar_sistema():
    print("=== BIENVENDIO A NUESTRA CAFETERIA ===\n")

    print("--- CLIENTES ---")
    c1 = Cliente(1, "Ana Garcia", "ana@mail.com", 10)
    c2 = Cliente(2, "Luis Lopez", "luis@mail.com", 20)
    c3 = Cliente(3, "Maria Perez", "maria@mail.com", 30)
    c4 = Cliente(4, "Jose Rodriguez", "jose@mail.com", 40)
    c5 = Cliente(5, "Lucia Fernandez", "lucia@mail.com", 50)
    c6 = Cliente(6, "Carlos Ruiz", "carlos@mail.com", 60)
    c7 = Cliente(7, "Elena Gomez", "elena@mail.com", 70)
    c8 = Cliente(8, "Pedro Sanchez", "pedro@mail.com", 80)
    c9 = Cliente(9, "Sofia Diaz", "sofia@mail.com", 90)
    c10 = Cliente(10, "Diego Torres", "diego@mail.com", 100)

    print(f"1. {c1.nombre}, Puntos: {c1.puntosFidelidad}")
    print(f"2. {c2.nombre}, Puntos: {c2.puntosFidelidad}")
    print(f"3. {c3.nombre}, Puntos: {c3.puntosFidelidad}")
    print(f"4. {c4.nombre}, Puntos: {c4.puntosFidelidad}")
    print(f"5. {c5.nombre}, Puntos: {c5.puntosFidelidad}")
    print(f"6. {c6.nombre}, Puntos: {c6.puntosFidelidad}")
    print(f"7. {c7.nombre}, Puntos: {c7.puntosFidelidad}")
    print(f"8. {c8.nombre}, Puntos: {c8.puntosFidelidad}")
    print(f"9. {c9.nombre}, Puntos: {c9.puntosFidelidad}")
    print(f"10. {c10.nombre}, Puntos: {c10.puntosFidelidad}")

    print(f"\nProbando métodos de {c1.nombre}:")
    print(f"  Login: {c1.login()}")
    print(f"  Realizar pedido: {c1.realizarPedido()}")
    print(f"  Historial: {c1.consultarHistorial()}")
    print("-" * 30)

    print("\n--- EMPLEADOS ---")
    e1 = Empleado(101, "Roberto", "rob@cafe.com", "E01", "BARISTA")
    e2 = Empleado(102, "Marta", "mar@cafe.com", "E02", "MESERO")
    e3 = Empleado(103, "Kevin", "kev@cafe.com", "E03", "GERENTE")
    e4 = Empleado(104, "Laura", "lau@cafe.com", "E04", "BARISTA")
    e5 = Empleado(105, "Julian", "jul@cafe.com", "E05", "MESERO")
    e6 = Empleado(106, "Sara", "sar@cafe.com", "E06", "BARISTA")
    e7 = Empleado(107, "Tomas", "tom@cafe.com", "E07", "GERENTE")
    e8 = Empleado(108, "Paula", "pau@cafe.com", "E08", "MESERO")
    e9 = Empleado(109, "Hugo", "hug@cafe.com", "E09", "BARISTA")
    e10 = Empleado(110, "Irene", "ire@cafe.com", "E10", "MESERO")

    print(f"1. {e1.nombre}, Rol: {e1.rol}")
    print(f"2. {e2.nombre}, Rol: {e2.rol}")
    print(f"3. {e3.nombre}, Rol: {e3.rol}")
    print(f"4. {e4.nombre}, Rol: {e4.rol}")
    print(f"5. {e5.nombre}, Rol: {e5.rol}")
    print(f"6. {e6.nombre}, Rol: {e6.rol}")
    print(f"7. {e7.nombre}, Rol: {e7.rol}")
    print(f"8. {e8.nombre}, Rol: {e8.rol}")
    print(f"9. {e9.nombre}, Rol: {e9.rol}")
    print(f"10. {e10.nombre}, Rol: {e10.rol}")
    
    print(f"\nProbando métodos de {e1.nombre} | Rol: {e1.rol}:")
    print(f"  Actualizar inventario: {e1.actualizarInventario()}")
    print(f"  Cambiar estado pedido: {e1.cambiarEstadoPedido()}")
    print("-" * 30)

    print("\n--- SECCIÓN: BEBIDAS ---")
    b1 = Bebida(201, "Americano", 35.00, "M", "CALIENTE")
    b2 = Bebida(202, "Cappuccino", 48.00, "G", "CALIENTE")
    b3 = Bebida(203, "Frappé", 62.00, "G", "FRIA")
    b4 = Bebida(204, "Espresso", 30.00, "S", "CALIENTE")
    b5 = Bebida(205, "Té Verde", 42.00, "M", "CALIENTE")
    b6 = Bebida(206, "Latte", 52.00, "G", "CALIENTE")
    b7 = Bebida(207, "Mocha", 55.00, "M", "CALIENTE")
    b8 = Bebida(208, "Jugo Naranja", 45.00, "M", "FRIA")
    b9 = Bebida(209, "Chocolate Caliente", 48.00, "G", "CALIENTE")
    b10 = Bebida(210, "Té Helado", 42.00, "G", "FRIA")

    print(f"1. {b1.nombre}, Precio: ${b1.precioBase:.2f} MXN")
    print(f"2. {b2.nombre}, Precio: ${b2.precioBase:.2f} MXN")
    print(f"3. {b3.nombre}, Precio: ${b3.precioBase:.2f} MXN")
    print(f"4. {b4.nombre}, Precio: ${b4.precioBase:.2f} MXN")
    print(f"5. {b5.nombre}, Precio: ${b5.precioBase:.2f} MXN")
    print(f"6. {b6.nombre}, Precio: ${b6.precioBase:.2f} MXN")
    print(f"7. {b7.nombre}, Precio: ${b7.precioBase:.2f} MXN")
    print(f"8. {b8.nombre}, Precio: ${b8.precioBase:.2f} MXN")
    print(f"9. {b9.nombre}, Precio: ${b9.precioBase:.2f} MXN")
    print(f"10. {b10.nombre}, Precio: ${b10.precioBase:.2f} MXN")

    print(f"\nProbando métodos de {b1.nombre}:")
    print(f"  Agregar extra: {b1.agregarExtra()}")
    precio = b1.calcularPrecioFinal()
    print(f"  Precio Final: ${precio:.2f} MXN")
    print("-" * 30)

    print("\n--- SECCIÓN: POSTRES ---")
    p1 = Postre(301, "Galleta", 18.00, False, False)
    p2 = Postre(302, "Brownie Vegano", 42.00, True, False)
    p3 = Postre(303, "Cheesecake", 65.00, False, True)
    p4 = Postre(304, "Muffin", 28.00, False, False)
    p5 = Postre(305, "Donut", 22.00, True, False)
    p6 = Postre(306, "Pastel Chocolate", 75.00, False, False)
    p7 = Postre(307, "Galleta Gluten Free", 25.00, False, True)
    p8 = Postre(308, "Tarta Frutas", 70.00, True, True)
    p9 = Postre(309, "Croissant", 32.00, False, False)
    p10 = Postre(310, "Alfajor", 38.00, False, False)

    print(f"1. {p1.nombre}, Precio: ${p1.precioBase:.2f} MXN")
    print(f"2. {p2.nombre}, Precio: ${p2.precioBase:.2f} MXN")
    print(f"3. {p3.nombre}, Precio: ${p3.precioBase:.2f} MXN")
    print(f"4. {p4.nombre}, Precio: ${p4.precioBase:.2f} MXN")
    print(f"5. {p5.nombre}, Precio: ${p5.precioBase:.2f} MXN")
    print(f"6. {p6.nombre}, Precio: ${p6.precioBase:.2f} MXN")
    print(f"7. {p7.nombre}, Precio: ${p7.precioBase:.2f} MXN")
    print(f"8. {p8.nombre}, Precio: ${p8.precioBase:.2f} MXN")
    print(f"9. {p9.nombre}, Precio: ${p9.precioBase:.2f} MXN")
    print(f"10. {p10.nombre}, Precio: ${p10.precioBase:.2f} MXN")


    def formatear_boolean(valor):
        return "Sí" if valor else "No"

    print(f"\nInformación detallada de postres:")
    print(f"Postre 1: ${p1.precioBase:.2f} MXN")
    print(f"  ¿Es Vegano?: {formatear_boolean(p1.esVegano)}")
    print(f"  ¿Sin Gluten?: {formatear_boolean(p1.sinGluten)}")
    
    print(f"\nPostre 2: ${p2.precioBase:.2f} MXN")
    print(f"  ¿Es Vegano?: {formatear_boolean(p2.esVegano)}")
    print(f"  ¿Sin Gluten?: {formatear_boolean(p2.sinGluten)}")

    print(f"\nPostre 3: {p3.nombre} - ${p3.precioBase:.2f} MXN")
    print(f"  ¿Es Vegano?: {formatear_boolean(p3.esVegano)}")
    print(f"  ¿Sin Gluten?: {formatear_boolean(p3.sinGluten)}")
    print("-" * 30)

    
    print("\n=== COMPRAS DE CLIENTES ===\n")

    
    print(f"Cliente: {c1.nombre} (Puntos actuales: {c1.puntosFidelidad})")
    print(f"Producto comprado: {b1.nombre} - ${b1.precioBase}")
    
    compra1 = f"{b1.nombre} - ${b1.precioBase}"
    c1.historialPedidos.append(compra1)
    
    puntos_ganados = int(b1.precioBase)
    c1.puntosFidelidad += puntos_ganados
    
    print(f"  - Compra registrada: {compra1}")
    print(f"  - Puntos ganados: +{puntos_ganados}")
    print(f"  - Puntos totales actualizados: {c1.puntosFidelidad}")
    print(f"  - Historial actualizado: {c1.consultarHistorial()}")
    print()

    print(f"Cliente: {c2.nombre} (Puntos actuales: {c2.puntosFidelidad})")
    print(f"Productos comprados:")
    print(f"  - {b2.nombre} - ${b2.precioBase}")
    print(f"  - {p1.nombre} - ${p1.precioBase}")
    
    compra2_1 = f"{b2.nombre} - ${b2.precioBase}"
    compra2_2 = f"{p1.nombre} - ${p1.precioBase}"
    c2.historialPedidos.append(compra2_1)
    c2.historialPedidos.append(compra2_2)
    
    total_compra2 = b2.precioBase + p1.precioBase
    puntos_ganados2 = int(total_compra2)
    c2.puntosFidelidad += puntos_ganados2
    
    print(f"  - Compra registrada: {compra2_1}, {compra2_2}")
    print(f"  - Total de la compra: ${total_compra2}")
    print(f"  - Puntos ganados: +{puntos_ganados2}")
    print(f"  - Puntos totales actualizados: {c2.puntosFidelidad}")
    print(f"  - Historial actualizado: {c2.consultarHistorial()}")
    print()

    print(f"Cliente: {c3.nombre} (Puntos actuales: {c3.puntosFidelidad})")
    print(f"Producto comprado: {b3.nombre} - ${b3.precioBase}")
    
    b3.agregarExtra()
    b3.modificadores.append("Crema extra") 
    
    precio_final_b3 = b3.precioBase + 5.00
    
    compra3 = f"{b3.nombre} con extra - ${precio_final_b3}"
    c3.historialPedidos.append(compra3)
    
    puntos_ganados3 = int(precio_final_b3)
    c3.puntosFidelidad += puntos_ganados3
    
    print(f"  - Extra agregado: Crema extra")
    print(f"  - Precio final: ${precio_final_b3}")
    print(f"  - Compra registrada: {compra3}")
    print(f"  - Puntos ganados: +{puntos_ganados3}")
    print(f"  - Puntos totales actualizados: {c3.puntosFidelidad}")
    print(f"  - Historial actualizado: {c3.consultarHistorial()}")
    print()

    print(f"Cliente: {c4.nombre} (Puntos actuales: {c4.puntosFidelidad})")
    print(f"Producto comprado: {b4.nombre} - ${b4.precioBase}")
    
    puntos_usados = 20  
    descuento = puntos_usados / 10  
    precio_con_descuento = max(0, b4.precioBase - descuento)
    
    compra4 = f"{b4.nombre} con canje - ${precio_con_descuento} (ahorró ${descuento})"
    c4.historialPedidos.append(compra4)
    
    c4.puntosFidelidad -= puntos_usados
    puntos_ganados4 = int(precio_con_descuento)
    c4.puntosFidelidad += puntos_ganados4
    
    print(f"  - Canje aplicado: {puntos_usados} puntos = ${descuento} descuento")
    print(f"  - Precio final con descuento: ${precio_con_descuento}")
    print(f"  - Compra registrada: {compra4}")
    print(f"  - Puntos canjeados: -{puntos_usados}")
    print(f"  - Puntos ganados por compra: +{puntos_ganados4}")
    print(f"  - Puntos totales actualizados: {c4.puntosFidelidad}")
    print(f"  - Historial actualizado: {c4.consultarHistorial()}")
    print()

    print("--- LISTA DE COMPRAS ---")
    print(f"Cliente {c1.nombre}: {len(c1.historialPedidos)} compra(s) - Puntos: {c1.puntosFidelidad}")
    print(f"Cliente {c2.nombre}: {len(c2.historialPedidos)} compra(s) - Puntos: {c2.puntosFidelidad}")
    print(f"Cliente {c3.nombre}: {len(c3.historialPedidos)} compra(s) - Puntos: {c3.puntosFidelidad}")
    print(f"Cliente {c4.nombre}: {len(c4.historialPedidos)} compra(s) - Puntos: {c4.puntosFidelidad}")

    print("\n--- PEDIDOS ---")
    ped1 = Pedido(501, "PENDIENTE", 50.0)
    
    print(f"Pedido ID: {ped1.idPedido}")
    print(f"  Total calculado: ${ped1.calcularTotal()}")
    stock_ok = formatear_boolean(ped1.validarStock())
    print(f"  ¿Hay Stock?: {stock_ok}")

    print("\n=== PRUEBA COMPLETADA ===")

if __name__ == "__main__":
    probar_sistema()