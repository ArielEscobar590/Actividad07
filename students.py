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
                    students[carne]={
                        "name": name,
                        "age": age,
                        "carrera": carrera,
                        "codigocurse":{
                            "curso": curso,
                            "notework": notework,
                            "notepar": notepar,
                            "exam": exam,
                        }
                    }
        elif op == 2:
            conteo = 1
            for carne,valor in students.items():
                print(f"Estudiante No. {conteo}")
                print(f"CARNE: {carne}")
                print(f"Nombre: {valor['name']}")
                print(f"Age: {valor['age']}")
                print(f"Carrera: {valor['carrera']}")

                for codigocurse,valor in valor["codigocurse"].items():
                    print(f"Curso: {valor['codigocurse']['curso']}")
                    print(f"Nota Tareas: {valor['codigocurse']['notework']}")
                    print(f"Nota Parcial: {valor['codigocurse']['notepar']}")
                    print(f"Nota Examen: {valor['codigocurse']['exam']}")
                    suma = valor['codigocurse']['notework'] + valor['codigocurse']['notepar'] + valor['codigocurse']['exam']
                    prom = suma / 3
                    print(f"Promedio Curso: {prom}")


        elif op == 3:
            buscar = int(input("Ingrese el carne del Estudiante: "))
            if buscar in students:
                print(f"Nombre del Estudiante ")




    except:
        print("Hubo un problema")