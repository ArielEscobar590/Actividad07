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
                carne =input("Ingrese el carne del Estudiante: ")
                name = input("Ingrese el nombre completo del Estudiante: ")
                age = int(input("Ingrese el edad del Estudiante: "))
                carrera = input("Ingrese el carrera del Estudiante: ")
                cursoscont = int(input("Ingrese el número de curso al que esta inscrito el Estudiante: "))
                for y in range(cursoscont):
                    curso = input("Ingrese el curso del Estudiante: ")
                    notework = int(input("Ingrese la nota de tareas del Estudiante: "))
                    notepar = input("Ingrese la nota del examen parcial del Estudiante: ")
                    exam = int(input("Ingrese la nota del examen del Estudiante: "))






    except:
        print("Hubo un problema")