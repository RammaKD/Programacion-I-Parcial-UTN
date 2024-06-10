from os import system
from pacientes import *
from data import *

def ejecutar_menu_principal(lista_pacientes: list[dict], lista_pacientes_eliminados: list[dict], 
                            lista_grupos_sanguineos: list, path_csv: str, path_json: str, 
                            path_json_ultimo_id: str):
    """Ejecuta el menu principal, con sus opciones.

    Args:
        lista_pacientes (list[dict]): recibe la lista de pacientes 
        lista_pacientes_eliminados (list[dict]): recibe la lista de pacientes eliminados
        lista_grupos_sanguineos (list): recibe la lista de posibles grupos sanguineos
    """
    leer_csv(path_csv, lista_pacientes, crear_paciente)
    leer_json(path_json, lista_pacientes_eliminados)
    continuar = True
    system("cls")
    while continuar:
        mostrar_opciones_menu_principal()
        opcion = seleccionar_opcion_menu("Seleccione una opción: ")
        match opcion:
            case 1:
                print(gestionar_ingreso(lista_pacientes, lista_grupos_sanguineos, path_json_ultimo_id))
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
                    actualizar_json(path_json, lista_pacientes_eliminados)
                    continuar = False
                    break
            case _:
                system("cls")
                print("Entrada no válida. Ingrese una opción del Menú.")

ejecutar_menu_principal(lista_pacientes, lista_pacientes_eliminados, lista_grupos_sanguineos, path_csv, path_json, path_json_ultimo_id)

