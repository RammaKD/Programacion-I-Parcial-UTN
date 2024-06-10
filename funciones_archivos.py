import re
import json

def leer_csv(path: str, lista: list, crear_paciente) -> bool:
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

def leer_json_ultimo_id(path: str):
    """Lee el valor de la clave ID del archivo JSON.

    Args:
        path (str): recibe el path del archivo JSON

    Returns:
        _type_: retorna el valor de la clave, si hubo error False
    """
    try: 
        with open(path, "r") as archivo:
            contenido = json.load(archivo)
            exito = contenido
    except:
        exito = False

    return exito

def actualizar_json_ultimo_id(path: str, id_incrementado: int):
    """Actualiza el archivo JSON con el id incrementado

    Args:
        path (str): recibe el path del archivo JSON
        id_incrementado (int): recibe el id incrementado

    Returns:
        _type_: retorna False en caso de error, sino True
    """
    exito = True
    try:
        with open(path, "w") as archivo:
            nuevo_diccionario = [{"id" : id_incrementado}]
            json.dump(nuevo_diccionario, archivo, indent=2)
    except:
        exito = False

    return exito

def incrementar_id(path: str) -> int:
    """Suma 1 al último ID del archivo JSON
    De esta forma lo hace autoincremental
    Args:
        path (str): recibe el path del archivo JSON

    Returns:
        int: retorna el id incrementado
    """
    ultimo_id = leer_json_ultimo_id(path)
    id_incrementado = ultimo_id[0]["id"] + 1
    actualizar_json_ultimo_id(path, id_incrementado)
    return id_incrementado
