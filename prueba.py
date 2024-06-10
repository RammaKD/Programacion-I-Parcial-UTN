import json
from generales import *
from pacientes import *

lista_pacientes = [
    {"id": 1, "nombre": "Juan", "apellido": "Pérez", "edad": 30, "altura": 175, "peso": 70.5, "dni": 52345678, "grupo sanguineo": "+"},
    {"id": 2, "nombre": "María", "apellido": "González", "edad": 25, "altura": 160, "peso": 55.0, "dni": 73456789, "grupo sanguineo": "-"},
    {"id": 3, "nombre": "Carlos", "apellido": "Rodríguez", "edad": 45, "altura": 180, "peso": 85.3, "dni": 84567890, "grupo sanguineo": "+"},
    {"id": 4, "nombre": "Lucía", "apellido": "Fernández", "edad": 35, "altura": 165, "peso": 62.5, "dni": 95678901, "grupo sanguineo": "+"},
    {"id": 5, "nombre": "Miguel", "apellido": "Martínez", "edad": 28, "altura": 170, "peso": 68.0, "dni": 56789012, "grupo sanguineo": "-"}
]

lista_diccionarios_compatibilidad = [{"grupo sanguineo" : [("A+"), ("A+", "AB+"), ("O+", "O-", "A+", "A-")]},
                                     {"grupo sanguineo" : [("A-"), ("A+", "A-", "AB+", "AB-"), ("O-", "A-")]},
                                     {"grupo sanguineo" : [("B+"), ("B+", "AB+"), ("O+", "O-", "B+", "B-")]},
                                     {"grupo sanguineo" : [("B-"), ("B+", "B-", "AB+", "AB-"), ("O-", "B-")]},
                                     {"grupo sanguineo" : [("AB+"), ("AB+"), ("A+","B+","AB+","O+","A-","B-","AB-","O-")]},
                                     {"grupo sanguineo" : [("AB-"), ("AB+", "AB-"), ("AB-", "O-", "A-", "B-")]},
                                     {"grupo sanguineo" : [("O+"), ("A+", "B+", "AB+", "O+"), ("O+", "O-")]},
                                     {"grupo sanguineo" : [("O-"), ("A+","B+","AB+","O+","A-","B-","AB-","O-"), ("O-")]},]


def determinar_donantes(lista_pacientes: list[dict], posibles_grupos_sanguineos):
    lista_donantes = []
    contador_donantes_maximos = 0

    for paciente in lista_pacientes:
        if paciente["grupo sanguineo"] in posibles_grupos_sanguineos[0][1] and contador_donantes_maximos < 3:
            contador_donantes_maximos += 1
            lista_donantes.append(paciente)
    if len(lista_donantes) > 0:
        mostrar_lista_pacientes(lista_donantes)
        print("Posibles donantes mostrados.")
    else:
        print("No hay donantes")

    return lista_donantes

def determinar_posibles_grupos_sanguineos_donantes(lista_diccionarios_compatibilidad: list[dict], un_paciente: list[dict]):
    grupo_sanguineo_paciente = un_paciente[0]["grupo sanguineo"]
    posibles_grupos_sanguineo = []
    for diccionario in lista_diccionarios_compatibilidad:
        if diccionario["grupo sanguineo"][0] == grupo_sanguineo_paciente:
            grupos_compatibles = diccionario["grupo sanguineo"][1], diccionario["grupo sanguineo"][2]
            posibles_grupos_sanguineo.append(grupos_compatibles)

    return posibles_grupos_sanguineo

def mostrar_compatibilidades(un_paciente: dict, lista_diccionarios_compatibilidad: dict):
    grupo_sanguineo_paciente = un_paciente[0]["grupo sanguineo"]
    for diccionario in lista_diccionarios_compatibilidad:
        if diccionario["grupo sanguineo"][0] == grupo_sanguineo_paciente:
            print(f"Puede donar a: {diccionario['grupo sanguineo'][1]}")
            print(f"Puede recibir de: {diccionario['grupo sanguineo'][2]}")
            break
    return un_paciente


paciente_encontrado = [{"id": 1, "nombre": "Juan", "apellido": "Pérez", "edad": 30, "altura": 175, "peso": 70.5, "dni": 52345678, "grupo sanguineo": "A+"}]
if not paciente_encontrado:
    print("Paciente no encontrado.")
else:
    posibles_grupos_sanguineos = determinar_posibles_grupos_sanguineos_donantes(lista_diccionarios_compatibilidad, paciente_encontrado)
    print(posibles_grupos_sanguineos)
    if len(posibles_grupos_sanguineos) != 0:
        mostrar_compatibilidades(paciente_encontrado, lista_diccionarios_compatibilidad)
        determinar_donantes(lista_pacientes, posibles_grupos_sanguineos)
    else:
        print("Lista de posibles grupos vacia.")









