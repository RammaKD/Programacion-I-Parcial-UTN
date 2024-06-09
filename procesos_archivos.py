import re

def leer_csv(path: str, lista_pacientes: list, crear_paciente) -> bool:
    exito = True
    try: 
        with open(path, "r", encoding="utf8") as archivo:
            for linea in archivo:
                registro = re.split(",|\n", linea)
                if registro[0] != "id":
                    diccionario_empleado = crear_paciente(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7])
                    lista_pacientes.append(diccionario_empleado)
    except:
        exito = False

    return exito

def actualizar_csv(path: str, lista: list):
    exito = True
    try:
        with open(path, "w", encoding="utf8") as archivo:
            for paciente in lista:
                linea = f"{paciente["id"]},{paciente["nombre"]},{paciente["apellido"]},{paciente["edad"]},{paciente["altura"]},{paciente["peso"]},{paciente["dni"]},{paciente["grupo sanguineo"]}"
                archivo.write(linea)
    except:
        exito = False

    return exito