'''
PODEROSISIMO SISTEMA DE VACUNACIONN 
POR: ALEXANDER WING ROJAS 
Taller de Programación - Semestre II 2025

    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠝⡄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⡀⠀⠀⠀⠀⣘⡴⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡄⠡⣀⣤⣶⣿⣿⣷⡱⡀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠚⢉⠈⡄⢹⣿⣿⠿⠛⠉⠑⡡⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⢴⢺⡿⠋⢭⠀⡘⡄⠘⡀⢫⠀⠀⠀⠀⠀⠑⠃
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⡀⠁⢣⠐⡈⢆⡱⠜⠊⠑⣀⡆⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣠⢊⣇⠀⠱⣘⡤⠗⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣀⠠⠐⠉⠀⠁⠈⠓⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

'''

##=============================================== AUXILIARES / UTILIDADES ==============================================================

import os #importo os para poder usar "cls" y limpiar la terminal luego de cada print de menus
import datetime #importo datetime para sacar la fecha y usarla en registros de vacunacion

#=============================================== MENU PRINCIPAL ==============================================================

def mostrar_menu(): #menu principal | depende el input printea las funciones 
    os.system("cls")
    print("===================================")
    print("    ✙ Sistema de Vacunación ✙")
    print("===================================")
    print("1. Administración")
    print("2. Registro de Vacunación")
    print("3. Consultas")
    print("4. Estadísticas")
    print("5. Alerta de Seguimiento")
    print("6. Salir")
    print("===================================")

#=============================================== FUNC. DE ADMINISTRACION ==============================================================

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
        os.system("cls")
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

#=============================================== REGISTRO DE VACUNACION ==============================================================

def cargar_registros(): 
    registros = []
    try:
        with open("registros.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")
                registro = {
                    "cedula": datos[0],
                    "nombre": datos[1],
                    "edad": int(datos[2]),
                    "sexo": datos[3],
                    "id_vacuna": int(datos[4]),
                    "fecha": datos[5],
                    "dosis": int(datos[6])
                }

                registros.append(registro)
    except FileNotFoundError:
        print("Archivo registros.txt no encontrado")
    return registros

def guardar_registro(registro):
    with open("registros.txt", "a") as archivo:  # "a" para añadir al final
        archivo.write(f"{registro['cedula']};{registro['nombre']};{registro['edad']};{registro['sexo']};{registro['id_vacuna']};{registro['fecha']};{registro['dosis']}\n")

def registrar_vacunacion(vacunas, registros):
    os.system("cls")
    print("=== Registro de Vacunación ===")

    # Cédula
    while True:
        cedula = input("Ingrese la cédula (9 dígitos): ")
        if len(cedula) == 9 and cedula.isdigit():
            break
        else:
            print("Cédula inválida. DEBE tener 9 dígitos.")

    #Nombre
    nombre = input("Ingrese el nombre completo: ")

    # edad
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            if edad > 0:
                break
            else:
                print("La edad debe ser mayor a 0")
        except ValueError:
            print("Ingrese un número válido")

    # Sexo
    while True:
        sexo = input("Ingrese el sexo (M/F): ").upper() #modifica los "m" o "f" para forzar que sea M o F
        if sexo in ["M", "F"]:
            break
        else:
            print("Sexo inválido. Ingrese sí o sí 'M' o 'F'.")

    # Mostrar vacunas disponibles
    mostrar_vacunas(vacunas)

    # Vacuna aplicada
    while True:
        try:
            id_vacuna = int(input("Ingrese el ID de la vacuna aplicada: "))
            vacuna_elegida = None
            for v in vacunas:
                if v["id"] == id_vacuna:
                    vacuna_elegida = v
                    break
            if vacuna_elegida:
                if edad >= vacuna_elegida["edad_minima"]:
                    break
                else:
                    print(f"La edad mínima para esta vacuna es {vacuna_elegida['edad_minima']}")
            else:
                print("ID de vacuna inválido.")
        except ValueError:
            print("Ingrese un número válido.")

    # Dosis
    while True:
        try:
            dosis = int(input(f"Ingrese número de dosis aplicadas (max {vacuna_elegida['dosis']}): "))
            if 1 <= dosis <= vacuna_elegida["dosis"]:
                # Validar que no se repita una dosis de la misma vacuna
                existe = False
                for r in registros:
                    if r["cedula"] == cedula and r["id_vacuna"] == id_vacuna and r["dosis"] == dosis:
                        existe = True
                        break
                if not existe:
                    break
                else:
                    print("Esta dosis ya fue registrada para esta persona.")
            else:
                print(f"Dosis inválida. Debe estar entre 1 y {vacuna_elegida['dosis']}.")
        except ValueError:
            print("Ingrese un número válido.")

    # Fecha automática
    fecha = datetime.date.today().isoformat()

    # Crear registro
    registro = {
        "cedula": cedula,
        "nombre": nombre,
        "edad": edad,
        "sexo": sexo,
        "id_vacuna": id_vacuna,
        "fecha": fecha,
        "dosis": dosis
    }

    # Guardar registro
    guardar_registro(registro)
    registros.append(registro)
    print(f"\nRegistro de vacunación de {nombre} agregado correctamente")
    input("\nPresione Enter para continuar...")

#=============================================== FUNC. DE CONSULTA ==============================================================

def consultar_por_cedula(registros, cedula):
    encontrados = [r for r in registros if r["cedula"] == cedula]
    if encontrados:
        print(f"\nRegistros para cédula {cedula}:")
        for r in encontrados:
            print(f"{r['nombre']} - Vacuna ID {r['id_vacuna']} - Dosis {r['dosis']} - Fecha {r['fecha']}")
    else:
        print("No se encontraron registros para esa cédula.")
    input("Presione Enter para continuar...")

def consultar_por_vacuna(registros, id_vacuna):
    encontrados = [r for r in registros if r["id_vacuna"] == id_vacuna]
    if encontrados:
        print(f"\nPersonas vacunadas con ID de vacuna {id_vacuna}:")
        for r in encontrados:
            print(f"{r['nombre']} - Cédula {r['cedula']} - Dosis {r['dosis']} - Fecha {r['fecha']}")
    else:
        print("No se encontraron registros para esa vacuna.")
    input("Presione Enter para continuar...")

def consultar_por_rango_edad(registros, edad_min, edad_max):
    encontrados = [r for r in registros if edad_min <= r["edad"] <= edad_max]
    if encontrados:
        print(f"\nPersonas con edades entre {edad_min} y {edad_max}:")
        for r in encontrados:
            print(f"{r['nombre']} - Cédula {r['cedula']} - Vacuna ID {r['id_vacuna']} - Dosis {r['dosis']}")
    else:
        print("No se encontraron registros en ese rango de edad.")
    input("Presione Enter para continuar...")

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