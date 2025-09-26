'''
PODEROSISIMO SISTEMA DE VACUNACIONN 
POR: ALEXANDER WING ROJAS 
Taller de Programación - Semestre II 2025

'''

def mostrar_menu(): #menu principal | depende el input printea las funciones 
    print("=================================")
    print("     Sistema de Vacunación")
    print("=================================")
    print("1. Administración")
    print("2. Registro de Vacunación")
    print("3. Consultas")
    print("4. Estadísticas")
    print("5. Alerta de Seguimiento")
    print("6. Salir")
    print("=================================")

def cargar_vacunas(): #actualiza la lista vacunas con la info de todas las vacunas de vacunas.txt
    vacunas = []

    try:
        with open('vacunas.txt', 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(';') #PREGUNTAR
                vacuna = {
                "id": int(datos[0]),
                "nombre": datos[1],
                "dosis": int(datos[2]),
                "edad_minima": int(datos[3])
            }
            vacunas.append(vacuna)
    except FileNotFoundError: #valida si en verdad existe "vacunas.txt"
        print("Archivo vacunas.txt no encontrado")

def main(): #función principal 
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ") #toma el input del menu principal

        if opcion == "1":
            print("Entrando a Administración...")
        elif opcion == "2":
            print("Entrando a Registro de Vacunación...")
        elif opcion == "3":
            print("Entrando a Consultas...")
        elif opcion == "4":
            print("Entrando a Estadísticas...")
        elif opcion == "5":
            print("Entrando a Alerta de Seguimiento...")
        elif opcion == "6":
            print("Saliendo del sistema... ¡Adiós!")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()