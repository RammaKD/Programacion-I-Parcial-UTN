import json

lista_pacientes = [
    {"id": 1, "nombre": "Juan", "apellido": "Pérez", "edad": 30, "altura": 175, "peso": 70.5, "dni": 52345678, "grupo sanguineo": "A+"},
    {"id": 2, "nombre": "María", "apellido": "González", "edad": 25, "altura": 160, "peso": 55.0, "dni": 73456789, "grupo sanguineo": "O-"},
    {"id": 3, "nombre": "Carlos", "apellido": "Rodríguez", "edad": 45, "altura": 180, "peso": 85.3, "dni": 84567890, "grupo sanguineo": "B+"},
    {"id": 4, "nombre": "Lucía", "apellido": "Fernández", "edad": 35, "altura": 165, "peso": 62.5, "dni": 95678901, "grupo sanguineo": "AB-"},
    {"id": 5, "nombre": "Miguel", "apellido": "Martínez", "edad": 28, "altura": 170, "peso": 68.0, "dni": 56789012, "grupo sanguineo": "A-"}
]

def leer_json_ultimo_id(path: str):
    with open(path, "r") as archivo:
        contenido = json.load(archivo)

    return contenido

def actualizar_json_ultimo_id(path: str, id_incrementado: int):
    with open(path, "w") as archivo:
        nuevo_diccionario = [{"id" : id_incrementado}]
        json.dump(nuevo_diccionario, archivo, indent=2)


path = "ultimo_id.json"
ultimo_id = leer_json_ultimo_id(path)
id_incrementado = ultimo_id[0]["id"] + 1
actualizar_json_ultimo_id(path, id_incrementado)