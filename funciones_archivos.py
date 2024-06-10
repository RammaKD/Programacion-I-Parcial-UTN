import re
from pacientes import *
import json

def leer_csv(path: str, lista: list) -> bool:
    """Lee los datos de un archivo CSV y lo utiliza para crear un diccionario y agregarlo a la lista. 
    Para crear el diccionario llama a la funcion crear_paciente.
    Args:
        path (str): recibe el path del archivo CSV
        lista (list): recibe la lista de diccionarios

    Returns:
        bool: retorna True si se completó con éxito la lectura, 
        sino False en caso de haber un error
    """
    exito = True
    try: 
        with open(path, "r", encoding="utf8") as archivo:
            for linea in archivo:
                registro = re.split(",|\n", linea)
                if registro[0] != "id":
                    diccionario = crear_paciente(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7])
                    lista.append(diccionario)
    except:
        exito = False

    return exito

def actualizar_csv(path: str, lista: list[dict]) -> bool:
    """Añade los cambios y modificaciones hechas en la lista al archivo CSV.

    Args:
        path (str): recibe el path del archivo CSV
        lista (list[dict]): recibe la lista de diccionarios

    Returns:
        bool: retorna True si se completó con éxito la escritura,
        sino False en caso de haber un error
    """
    exito = True
    try:
        with open(path, "w", encoding="utf8") as archivo:
            cabecera = "id,nombre,apellido,edad,altura,peso,dni,grupo sanguineo\n"
            archivo.write(cabecera)

            for paciente in lista:
                linea = f'{paciente["id"]},{paciente["nombre"]},{paciente["apellido"]},{paciente["edad"]},{paciente["altura"]},{paciente["peso"]},{paciente["dni"]},{paciente["grupo sanguineo"]}\n'
                archivo.write(linea)
    except:
        exito = False

    return exito

def leer_json(path: str, lista_pacientes_eliminados: list[dict]) -> bool:
    """Lee los datos de un archivo JSON y agrega los datos a la lista de eliminados.

    Args:
        path (str): recibe path del archivo JSON
        lista_pacientes_eliminados (list[dict]): recibe lista de eliminados

    Returns:
        bool: retorna True si se completó con éxito la lectura,
        sino False en caso de haber un error
    """
    exito = True
    try:
        with open(path, "r") as archivo:
            empleados_eliminados = json.load(archivo)
            for empleado in empleados_eliminados:
                lista_pacientes_eliminados.append(empleado)
    except:
        exito = False
    return exito

def actualizar_json(path: str, lista: list[dict]) -> bool:
    """Añade los eliminados al archivo JSON si es que los hay.

    Args:
        path (str): recibe el path del arhivo JSON
        lista (list[dict]): recibe la lista de eliminados

    Returns:
        bool: retorna True si se completó con exito la escritura,
        sino False en caso de haber un error
    """
    exito = True
    try:
        with open(path, "w") as archivo:
            json.dump(lista, archivo, indent=4)
    except:
        exito = False
    return exito