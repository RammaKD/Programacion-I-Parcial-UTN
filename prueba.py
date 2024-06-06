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


# print(ingresar_paciente(lista_pacientes, lista_grupos_sanguineos))

# print(mostrar_lista_pacientes(lista_pacientes))

# un_paciente = buscar_paciente(lista_pacientes, "nombre", "pepe")

# print(modificar_empleado(lista_grupos_sanguineos, un_paciente, "nombre"))

# menu_modificacion(lista_grupos_sanguineos, un_paciente)

# print(gestionar_modificacion(lista_pacientes, lista_grupos_sanguineos))

# print(gestionar_eliminacion(lista_pacientes, lista_grupos_sanguineos))

retorno_paciente_encontrado = buscar_por_dni(lista_pacientes)
if type(retorno_paciente_encontrado) == tuple:
    print(retorno_paciente_encontrado(0))
else:
    print(retorno_paciente_encontrado)