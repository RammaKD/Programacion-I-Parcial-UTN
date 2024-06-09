lista_pacientes = [
    {"id": 1, "nombre": "Juan", "apellido": "Pérez", "edad": 30, "altura": 175, "peso": 70.5, "dni": 52345678, "grupo sanguineo": "A+"},
    {"id": 2, "nombre": "María", "apellido": "González", "edad": 25, "altura": 160, "peso": 55.0, "dni": 73456789, "grupo sanguineo": "O-"},
    {"id": 3, "nombre": "Carlos", "apellido": "Rodríguez", "edad": 45, "altura": 180, "peso": 85.3, "dni": 84567890, "grupo sanguineo": "B+"},
    {"id": 4, "nombre": "Lucía", "apellido": "Fernández", "edad": 35, "altura": 165, "peso": 62.5, "dni": 95678901, "grupo sanguineo": "AB-"},
    {"id": 5, "nombre": "Miguel", "apellido": "Martínez", "edad": 28, "altura": 170, "peso": 68.0, "dni": 56789012, "grupo sanguineo": "A-"}
]

def find_last_value_in_list_dict(lista_diccionarios, key):
    value = 0
    for diccionario in lista_diccionarios:
        posible_valor = diccionario[key]
        if posible_valor != 0:
            value = posible_valor
            
    return value


# def incrementar_id (lista_diccionarios:list[dict]) -> int:
#     ultimo_id = find_last_value_in_list_dict(lista_diccionarios, "id")
#     id_incrementado = ultimo_id + 1
#     return id_incrementado

def crear_lista_keys(lista_diccionarios: list[dict]) -> list:
    claves_unicas = set()
    for empleado in lista_diccionarios:
        claves_unicas.update(empleado.keys())
    lista_parametros = list(claves_unicas)

    return lista_parametros


lista_keys = crear_lista_keys(lista_pacientes)
key = input("Ingrese una key: ")
if key in lista_keys:
    ultimo_valor = find_last_value_in_list_dict(lista_pacientes, key)
    print(ultimo_valor)
else:
    print("Key no encontrada.")

