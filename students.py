students = {}
op = 0
while op != 4:
    try:
        print("\n--- Menú ---")
        print("1. Registrar Estudiantes")
        print("2. Mostrar Estudiantes y sus cursos")
        print("3. Buscar Estudiantes por Carne")
        print("4. Salir")
        op = int(input("Ingrese una opción: "))
        if op == 1:
            cont = int(input("\n¿Cuantos Estudiantes va a registrar Estudiantes?"))
            for x in range(cont):
                carne = int(input("Ingrese el carne del Estudiante: "))
                name = input("Ingrese el nombre completo del Estudiante: ")
                age = int(input("Ingrese el edad del Estudiante: "))
                carrera = input("Ingrese el carrera del Estudiante: ")
                cursoscont = int(input("Ingrese el número de curso al que esta inscrito el Estudiante: "))
                for y in range(cursoscont):
                    codigocurse = int(input("Ingrese el codigo del curso: "))
                    curso = input("Ingrese el curso del Estudiante: ")
                    notework = int(input("Ingrese la nota de tareas del Estudiante: "))
                    notepar = input("Ingrese la nota del examen parcial del Estudiante: ")
                    exam = int(input("Ingrese la nota del examen del Estudiante: "))
        elif op == 2:
            conteo = 1
            for carne,valor in students.items():
                print(f"Estudiante No. {conteo}")
                print(f"CARNE: {carne}")
                print(f"Nombre: {valor["name"]}")
                print(f"Age: {valor['age']}")
        elif op == 3:
            buscar = int(input("Ingrese el carne del Estudiante: "))
            if buscar in students:
                print(f"Nombre del Estudiante ")




    except:
        print("Hubo un problema")