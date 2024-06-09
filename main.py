from os import system
from pacientes import *
from procesos_archivos import *

lista_pacientes = [
    # {"id": 1, "nombre": "Juan", "apellido": "Pérez", "edad": 30, "altura": 175, "peso": 70.5, "dni": 52345678, "grupo sanguineo": "A+"},
    # {"id": 2, "nombre": "María", "apellido": "González", "edad": 25, "altura": 160, "peso": 55.0, "dni": 73456789, "grupo sanguineo": "O-"},
    # {"id": 3, "nombre": "Carlos", "apellido": "Rodríguez", "edad": 45, "altura": 180, "peso": 85.3, "dni": 84567890, "grupo sanguineo": "B+"},
    # {"id": 4, "nombre": "Lucía", "apellido": "Fernández", "edad": 35, "altura": 165, "peso": 62.5, "dni": 95678901, "grupo sanguineo": "AB-"},
    # {"id": 5, "nombre": "Miguel", "apellido": "Martínez", "edad": 28, "altura": 170, "peso": 68.0, "dni": 56789012, "grupo sanguineo": "A-"}
]
lista_pacientes_eliminados = []
lista_grupos_sanguineos = ["A","B","AB","A+","B+","AB+","O","O+","A-","B-","AB-","O-"]
path_csv = "Paciente.csv"


def ejecutar_menu_principal(lista_pacientes: list[dict], lista_pacientes_eliminados: list[dict], lista_grupos_sanguineos: list, path_csv: str):
    """Ejecuta el menu principal, con sus opciones.

    Args:
        lista_pacientes (list[dict]): recibe la lista de pacientes 
        lista_pacientes_eliminados (list[dict]): recibe la lista de pacientes eliminados
        lista_grupos_sanguineos (list): recibe la lista de posibles grupos sanguineos
    """
    leer_csv(path_csv, lista_pacientes, crear_paciente)
    continuar = True
    system("cls")
    while continuar:
        mostrar_opciones_menu_principal()
        opcion = seleccionar_opcion_menu("Seleccione una opción: ")
        match opcion:
            case 1:
                print(ingresar_paciente(lista_pacientes, lista_grupos_sanguineos))
            case 2:
                print(gestionar_modificacion(lista_pacientes, lista_grupos_sanguineos, 4000000, 99999999, 5))
            case 3:
                print(gestionar_eliminacion(lista_pacientes, lista_pacientes_eliminados, 4000000, 99999999, 5))
            case 4:
                print(mostrar_lista_pacientes(lista_pacientes))
            case 5:
                print(gestionar_ordenamiento(lista_pacientes))
            case 6:
                print(gestionar_busqueda_por_dni(lista_pacientes, 4000000, 99999999, 5))
            case 7:
                print(gestionar_promedio(lista_pacientes))
            case 8:
                system("cls")
                if desea_continuar("Desea salir del programa (SI/NO)?: ", "Error. Ingrese SI/NO: "):
                    actualizar_csv(path_csv, lista_pacientes)
                    continuar = False
                    break
            case _:
                system("cls")
                print("Entrada no válida. Ingrese una opción del Menú.")

ejecutar_menu_principal(lista_pacientes, lista_pacientes_eliminados, lista_grupos_sanguineos, path_csv)

