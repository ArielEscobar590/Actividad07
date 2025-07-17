students = {}
cursos = {}
op = 0
while op != 4:
    try:
        print("--- Menú ")
        print("1. Registrar Estudiantes")
        print("2. Mostrar Estudiantes y sus cursos")
        print("3. Buscar Estudiantes por Carne")
        print("4. Salir")
        op = int(input("Ingrese una opción: "))
        if op == 1:
            cont = int(input("Registrar Estudiantes"))
            for x in range(cont):
                name = input("Ingrese el nombre: ")




    except:
        print("Hubo un problema")