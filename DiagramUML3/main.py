from biblioteca import *

def f_bool(valor):
    return "Si" if valor else "No"

def ejecutar_sistema():
    libros = [
        Libro(1, "Don Quijote", 1605, True, "Cervantes", "ISBN-01", "Novela"),
        Libro(2, "Cien años de soledad", 1967, True, "García Márquez", "ISBN-02", "Realismo"),
        Libro(3, "Rayuela", 1963, True, "Cortázar", "ISBN-03", "Novela"),
        Libro(4, "Ficciones", 1944, True, "Borges", "ISBN-04", "Cuento"),
        Libro(5, "Pedro Páramo", 1955, True, "Rulfo", "ISBN-05", "Novela"),
        Libro(6, "La ciudad y los perros", 1963, True, "Vargas Llosa", "ISBN-06", "Novela"),
        Libro(7, "El Aleph", 1949, True, "Borges", "ISBN-07", "Cuento"),
        Libro(8, "La tregua", 1960, True, "Benedetti", "ISBN-08", "Novela"),
        Libro(9, "Desolación", 1922, True, "Mistral", "ISBN-09", "Poesía"),
        Libro(10, "Aura", 1962, True, "Fuentes", "ISBN-10", "Fantástico")
    ]

    revistas = [
        Revista(11, "National Geographic", 2023, True, 145, "Mensual"),
        Revista(12, "Scientific American", 2023, True, 320, "Mensual"),
        Revista(13, "Time", 2024, True, 10, "Semanal"),
        Revista(14, "Forbes", 2024, True, 5, "Quincenal"),
        Revista(15, "Vogue", 2023, True, 88, "Mensual"),
        Revista(16, "Nature", 2024, True, 502, "Semanal"),
        Revista(17, "The Economist", 2024, True, 12, "Semanal"),
        Revista(18, "Wired", 2023, True, 25, "Mensual"),
        Revista(19, "Rolling Stone", 2023, True, 112, "Mensual"),
        Revista(20, "Cosmopolitan", 2024, True, 45, "Mensual")
    ]

    digitales = [
        MaterialDigital(21, "Python para Todos", 2022, True, "PDF", "url.com/py", 15.5),
        MaterialDigital(22, "Java Avanzado", 2021, True, "EPUB", "url.com/java", 12.0),
        MaterialDigital(23, "C++ Guía", 2023, True, "PDF", "url.com/cpp", 20.1),
        MaterialDigital(24, "SQL Master", 2020, True, "PDF", "url.com/sql", 5.4),
        MaterialDigital(25, "React Doc", 2024, True, "HTML", "url.com/react", 2.2),
        MaterialDigital(26, "Docker Guide", 2023, True, "PDF", "url.com/dk", 18.0),
        MaterialDigital(27, "AWS Cloud", 2022, True, "EPUB", "url.com/aws", 25.6),
        MaterialDigital(28, "Linux Kernel", 2021, True, "PDF", "url.com/lin", 30.0),
        MaterialDigital(29, "Git Pro", 2024, True, "PDF", "url.com/git", 10.8),
        MaterialDigital(30, "Swift Basics", 2023, True, "EPUB", "url.com/sw", 9.9)
    ]

    usuarios = [
        Usuario("Ana Garcia", 3), Usuario("Luis Lopez", 2), 
        Usuario("Maria Perez", 5), Usuario("Jose Rodriguez", 1),
        Usuario("Lucia Fernandez", 4), Usuario("Carlos Ruiz", 3),
        Usuario("Elena Gomez", 2), Usuario("Pedro Sanchez", 5),
        Usuario("Sofia Diaz", 1), Usuario("Diego Torres", 4)
    ]

    sucursales = [
        Sucursal(1, "Sede Central"), Sucursal(2, "Sede Norte"),
        Sucursal(3, "Sede Sur"), Sucursal(4, "Sede Este"),
        Sucursal(5, "Sede Oeste"), Sucursal(6, "Sede Centro"),
        Sucursal(7, "Sede Chapultepec"), Sucursal(8, "Sede Reforma"),
        Sucursal(9, "Sede Insurgentes"), Sucursal(10, "Sede Polanco")
    ]

    bibliotecarios = [
        Bibliotecario("Marta Gomez"), Bibliotecario("Roberto Sanchez"),
        Bibliotecario("Laura Torres"), Bibliotecario("David Luna"),
        Bibliotecario("Sofia Rios"), Bibliotecario("Juan Soler"),
        Bibliotecario("Ana Belen"), Bibliotecario("Pedro Juan"),
        Bibliotecario("Clara Luz"), Bibliotecario("Mario Bros")
    ]

    buscador = Catalogo()
    admin = bibliotecarios[0]

    sucursales[0].catalogoLocal.extend([libros[1], revistas[0]])
    sucursales[1].catalogoLocal.append(digitales[0])

    print("=== BIENVENIDOS A NUESTRA BIBLIOTECA ===")
    print("\n--- SECCIÓN: LIBROS FÍSICOS ---")
    for l in libros:
        print(f"ID: {l.idMaterial} | Título: {l.titulo} | Autor: {l.autor} | Género: {l.genero}")

    print("\n--- SECCIÓN: REVISTAS ---")
    for r in revistas:
        print(f"ID: {r.idMaterial} | Título: {r.titulo} | Edición: {r.edicion} | Frecuencia: {r.periodicidad}")

    print("\n--- SECCIÓN: MATERIAL DIGITAL ---")
    for d in digitales:
        print(f"ID: {d.idMaterial} | Título: {d.titulo} | Formato: {d.tipoArchivo} | Tamaño: {d.tamañoMB}MB")

    print("\n=== SISTEMA ===")

    casos = [
        (usuarios[0], libros[1], "Libro", 10),
        (usuarios[1], revistas[0], "Revista", 3),
        (usuarios[2], digitales[0], "Digital", 0),
        (usuarios[3], libros[4], "Libro", 15),
        (usuarios[4], revistas[2], "Revista", 0)
    ]

    for i, (usuario_activo, mat_solicitado, tipo, dias_retraso) in enumerate(casos):
        print(f"--- USUARIO {i+1}: {usuario_activo.nombre} ---")
        
        print(f">>> PASO 1: BÚSQUEDA")
        print(f"Usuario {usuario_activo.nombre} busca {tipo}: '{mat_solicitado.titulo}'")
        print(buscador.buscarEnTodasSucursales(mat_solicitado.titulo, sucursales))

        print(f"\n>>> PASO 2: GESTIÓN DE PRÉSTAMO")
        resultado = admin.gestionarPrestamo(usuario_activo, mat_solicitado, 5000 + i, "2024-03-01", "2024-03-15")
        if resultado:
            print(f"PROCESO: {admin.nombre} creó Préstamo ID {resultado.idPrestamo}")
            print(f"Estado del material: ¿Disponible? {f_bool(mat_solicitado.disponible)}")

        print(f"\n>>> PASO 3: CONTROL DE PENALIZACIONES")
        multa = Penalizacion(0.0, "Retraso de entrega", False)
        
        if dias_retraso > 0:
            multa.calcularMulta(dias_retraso)
            print(f"Días de retraso detectados: {dias_retraso}")
            print(f"Monto calculado: ${multa.monto}")
            print(f"¿Multa pagada actualmente?: {f_bool(multa.pagada)}")
            print("\n[MENSAJE DEL SISTEMA]:")
            print(multa.bloquearUsuario(usuario_activo))
        else:
            print("Resultado: No se detectaron retrasos.")
            print("\n[MENSAJE DEL SISTEMA]:")
            print(f"ESTADO: {usuario_activo.nombre} tiene su cuenta activa.")

        print("-" * 50 + "\n")

    print(">>> REPORTE ADMINISTRATIVO")
    print(admin.transferirMaterial(libros[0], sucursales[9]))

    print("\n=== FIN DE LA EVIDENCIA ===")

if __name__ == "__main__":
    ejecutar_sistema()