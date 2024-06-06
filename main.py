from os import system
from pacientes import *
from pacientes import *

lista_pacientes = [
    {"id": 1, "nombre": "Juan", "apellido": "Pérez", "edad": 30, "altura": 175, "peso": 70.5, "dni": 52345678, "grupo sanguineo": "A+"},
    {"id": 2, "nombre": "María", "apellido": "González", "edad": 25, "altura": 160, "peso": 55.0, "dni": 73456789, "grupo sanguineo": "O-"},
    {"id": 3, "nombre": "Carlos", "apellido": "Rodríguez", "edad": 45, "altura": 180, "peso": 85.3, "dni": 84567890, "grupo sanguineo": "B+"},
    {"id": 4, "nombre": "Lucía", "apellido": "Fernández", "edad": 35, "altura": 165, "peso": 62.5, "dni": 95678901, "grupo sanguineo": "AB-"},
    {"id": 5, "nombre": "Miguel", "apellido": "Martínez", "edad": 28, "altura": 170, "peso": 68.0, "dni": 56789012, "grupo sanguineo": "A-"}
]
lista_pacientes_eliminados = []
lista_grupos_sanguineos = ["A","B","AB","A+","B+","AB+","O","O+","A-","B-","AB-","O-"]


def menu_principal(lista_pacientes, lista_pacientes_eliminados, lista_grupos_sanguineos):
    continuar = True
    system("cls")
    while continuar:
        print("\nMenú")
        print("1. Dar de alta")
        print("2. Modificar")
        print("3. Eliminar")
        print("4. Mostrar todos")
        print("5. Ordenar pacientes")
        print("6. Buscar paciente por DNI")
        print("7. Calcular promedio")
        print("8. Salir")
        opcion = seleccionar_opcion_menu("Seleccione una opción: ")

        match opcion:
            case 1:
                print(ingresar_paciente(lista_pacientes, lista_grupos_sanguineos))
            case 2:
                print(gestionar_modificacion(lista_pacientes, lista_grupos_sanguineos))
            case 3:
                print(gestionar_eliminacion(lista_pacientes, lista_pacientes_eliminados))
            case 4:
                print(mostrar_lista_pacientes(lista_pacientes))
            case 5:
                pass
            case 6:
                pass
                print(buscar_por_dni(lista_pacientes))
            case 7:
                pass
            case 8:
                system("cls")
                if desea_continuar("Desea salir (SI/NO?: ", "Error. Ingrese SI/NO: "):
                    continuar = False
                    break
            case _:
                system("cls")
                print("Entrada no válida. Ingrese una opción del Menú.")

menu_principal(lista_pacientes, lista_pacientes_eliminados, lista_grupos_sanguineos)

