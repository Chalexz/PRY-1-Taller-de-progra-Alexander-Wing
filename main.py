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
                datos = linea.strip().split(';') 
                vacuna = {
                "id": int(datos[0]),
                "nombre": datos[1],
                "dosis": int(datos[2]),
                "edad_minima": int(datos[3])
            }
                vacunas.append(vacuna)
    except FileNotFoundError: #valida si en verdad existe "vacunas.txt"
        print("Archivo vacunas.txt no encontrado")
    
    return vacunas

def guardar_vacunas(vacunas):
    with open("vacunas.txt" , "w") as archivo:
        for vacuna in vacunas:
            archivo.write(f"{vacuna['id']};{vacuna['nombre']};{vacuna['dosis']};{vacuna['edad_minima']}\n")

def agregar_vacunas(vacunas, nombre, dosis, edad_minima):
    id_vacuna = len(vacunas) + 1
    vacuna = {
        "id": id_vacuna,
        "nombre": nombre,
        "dosis": dosis,
        "edad_minima": edad_minima
    }
    vacunas.append(vacuna)
    guardar_vacunas(vacunas)
    print(f"La vacuna '{nombre}' añadida exitosamente ˙ ͜ʟ˙")

def eliminar_vacuna(vacunas, id_vacuna):
    vacuna_eliminar = None
    for vacuna in vacunas:
        if vacuna['id'] == id_vacuna:
            vacuna_eliminar = vacuna
            break
    
    if vacuna_eliminar:
        vacunas.remove(vacuna_eliminar)
        guardar_vacunas(vacunas)
        print(f"Vacuna con ID {id_vacuna} eliminada exitosamente")
    else:
        print(f"No se encontró una vacuna con el ID {id_vacuna}")

def mostrar_vacunas(vacunas):
    print("Lista de vacunas disponibles:")
    for vacuna in vacunas:
        print(f"ID: {vacuna['id']} - Nombre: {vacuna['nombre']} - Dosis: {vacuna['dosis']} - Edad mínima: {vacuna['edad_minima']}")

def menu_administracion(vacunas):
    while True: 
        print('\n Menu Administración')
        print("1. Agregar Vacuna")
        print("2. Eliminar Vacuna")
        print("3. Mostrar Vacuna")
        print("4. Volver al Menú Principal")
        opcion = input("Favor seleccionar una de las opciones. Digite el número:  ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la vacuna a agregar: ")
            dosis = int(input("Ingrese la dosis requerida (1 o 2): "))
            edad_minima = int(input("Ingrese la edad mínima recomendada para la vacuna en cuestión: "))
            agregar_vacunas(vacunas, nombre, dosis, edad_minima)
        elif opcion == "2":
            id_vacuna = int(input("Ingrese el ID de la vacuna a eliminar: "))
            eliminar_vacuna(vacunas, id_vacuna)
        elif opcion == "3":
            mostrar_vacunas(vacunas)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def main():
    vacunas = cargar_vacunas() 
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ") 

        if opcion == "1":
            menu_administracion(vacunas) 
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
            guardar_vacunas(vacunas)  
            break
        else:
            print("Opción no válida, intente de nuevo.")



if __name__ == "__main__":
    main()