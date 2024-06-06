from os import system
from inputs import *
from generales import *


#region Create
def crear_paciente(id: int,nombre: str,apellido: str, edad: int, altura: int, peso: float, dni: int, grupo_sanguineo: str) -> dict:
    diccionario_empleado = {
        "id" : id,
        "nombre" : nombre,
        "apellido" : apellido,
        "edad" : edad,
        "altura" : altura,
        "peso" : peso,
        "dni" : dni,
        "grupo sanguineo" : grupo_sanguineo
    }
    return diccionario_empleado

def ingresar_paciente(lista_pacientes: list[dict], lista_grupos_sanguineos: list):
    retorno = "Ingreso exitoso."
    
    while True:
        # nombre = get_str_len("Ingrese nombre: ", "Error. Reingrese nombre: ", 1, 20, 3)
        # if not nombre:
        #     retorno = "Se agotaron los intentos para ingresar datos."
        #     break
        # apellido = get_str_len("Ingrese apellido: ", "Error. Reingrese apellido: ", 1, 20, 3)
        # if not apellido:
        #     retorno = "Se agotaron los intentos para ingresar datos."
        #     break
        # edad = get_int("Ingrese edad: ", "Error. Reingrese edad: ", 1, 120, 3)
        # if not edad:
        #     retorno = "Se agotaron los intentos para ingresar datos."
        #     break
        # altura = get_int("Ingrese altura: ", "Error. Reingrese altura: ", 30, 230, 3)
        # if not altura:
        #     retorno = "Se agotaron los intentos para ingresar datos."
        #     break
        # peso = get_float("Ingrese peso: ", "Error. Reingrese peso: ", 10, 300, 3)
        # if not peso:
        #     retorno = "Se agotaron los intentos para ingresar datos."
        # dni = get_int("Ingrese DNI: ", "Error. Reingrese DNI: ", 4000000, 99999999, 3)
        # if not dni:
        #     retorno = "Se agotaron los intentos para ingresar datos."
        #     break
        # grupo_sanguineo = get_str_find("Ingrese grupo sanguíneo: ", "Error. Reingrese grupo sanguíneo: ",
        #                                 lista_grupos_sanguineos, 3)
        # if not grupo_sanguineo:
        #     retorno = "Se agotaron los intentos para ingresar datos."
        #     break

        id = incrementar_id(lista_pacientes)
        diccionario_paciente = crear_paciente(id, "pepe", "argento", 60, 170, 80.0, 50000000, "A+")
        lista_pacientes.append(diccionario_paciente)
        
        if not desea_continuar("Desea seguir cargando? (SI/NO): ", "Error. Ingrese SI/NO: "):
            break
   
    return retorno
#endregion

#region Read
def mostrar_lista_pacientes(lista_pacientes: list[dict]) -> str:
    if comprobar_len_lista(lista_pacientes):
        print("***************************************************************************************************************************")
        print("|       Nombre       |      Apellido      |     Edad      |   Altura(cm)  |    Peso(KG)   |      DNI      |Grupo sanguíneo|")
        print("---------------------------------------------------------------------------------------------------------------------------")
        for paciente in lista_pacientes:
            mostrar_paciente(paciente)
        print("***************************************************************************************************************************")
        retorno = "Paciente/s mostrados con éxito."
    else:
        retorno = "La lista está vacía, ingrese pacientes."
    
    return retorno

def mostrar_paciente(un_paciente: dict) -> dict:
    print(f"|{un_paciente['nombre']:<20}|{un_paciente['apellido']:<20}|{un_paciente['edad']:<15}|{un_paciente['altura']:<15}|{un_paciente['peso']:<15}|{un_paciente['dni']:<15}|{un_paciente['grupo sanguineo']:<15}|")
    return un_paciente

def buscar_paciente(lista_pacientes: list[dict], clave: str, valor: int|str) -> dict|bool:
    retorno = True
    for paciente in lista_pacientes:
        if paciente[clave] == valor:
            mostrar_paciente(paciente)
            retorno = paciente
            break
        else:
            retorno = False
    
    return retorno
#endregion

#region Update
def modificar_empleado(lista_grupos_sanguineos: list, un_paciente: dict, dato_modificar: str) -> str:
    nuevo_dato = determinar_tipo_dato_modificar(lista_grupos_sanguineos, dato_modificar)
    estado_anterior = un_paciente[dato_modificar]
    if not nuevo_dato:
        retorno = "Se agotaron los intentos para ingresar nuevo dato."
    elif desea_continuar("¿Desea efectuar el cambio? (SI/NO): ", "Error. Ingrese (SI/NO): "):
        un_paciente[dato_modificar] = nuevo_dato
        mostrar_paciente(un_paciente)
        retorno = "Paciente modificado."
        if desea_continuar("¿Desea deshacer el cambio? (SI/NO): ", "Error. Ingrese (SI/NO): "):
            un_paciente[dato_modificar] = estado_anterior
            mostrar_paciente(un_paciente)
            retorno = "Se deshicieron los cambios."
        else:
            retorno = "Cambio confirmado con éxito."
    else:
        retorno = "Cambio deshecho."

    return retorno

def menu_modificacion(lista_grupos_sanguineos: list, paciente_encontrado: dict) -> bool:
    print("Paciente encontrado.")
    continuar_modificacion = True
    while continuar_modificacion:
                print("\nMenú modificación")
                print("1. Nombre")
                print("2. Apellido")
                print("3. Edad")
                print("4. Altura")
                print("5. Peso")
                print("6. Dni")
                print("7. Grupo sanguíneo")
                print("8. Salir")
                opcion_modificacion = seleccionar_opcion_menu("Seleccione una opción")

                match opcion_modificacion:
                        case 1:
                            system("cls")
                            print(modificar_empleado(lista_grupos_sanguineos, paciente_encontrado, "nombre"))
                        case 2:
                            system("cls")
                            print(modificar_empleado(lista_grupos_sanguineos, paciente_encontrado, "apellido"))
                        case 3:
                            system("cls")
                            print(modificar_empleado(lista_grupos_sanguineos, paciente_encontrado, "edad"))
                        case 4:
                            system("cls")
                            print(modificar_empleado(lista_grupos_sanguineos, paciente_encontrado, "altura"))
                        case 5:
                            system("cls")
                            print(modificar_empleado(lista_grupos_sanguineos, paciente_encontrado, "peso"))
                        case 6:
                            system("cls")
                            print(modificar_empleado(lista_grupos_sanguineos, paciente_encontrado, "dni"))
                        case 7:
                            system("cls")
                            print(modificar_empleado(lista_grupos_sanguineos, paciente_encontrado, "grupo sanguineo"))
                        case 8:
                            system("cls")
                            if desea_continuar("Desea salir? (SI/NO): ", "Error. Ingrese SI/NO: "):
                                continuar_modificacion = False
                                break
                        case _:
                            system("cls")
                            print("Entrada no válida. Ingrese una opción del Menú.")
    return continuar_modificacion

def gestionar_modificacion(lista_pacientes: list[dict], lista_grupos_sanguineos: list) -> str|tuple|bool:
    if comprobar_len_lista(lista_pacientes):
        retorno_id = buscar_por_dni(lista_pacientes)
        if type(retorno_id) == tuple:
            empleado_encontrado = retorno_id[1]
            gestion = "Modificación finalizada."
            menu_modificacion(lista_grupos_sanguineos, empleado_encontrado)
        else:
            gestion = retorno_id
    else:
        gestion = "La lista está vacía, ingrese pacientes."
    
    return gestion
#endregion

#region Delete
def eliminar_paciente(lista_pacientes: list[dict], lista_pacientes_eliminados: list, dni: int) -> str:
    eliminado = buscar_paciente(lista_pacientes, "dni", dni)
    if not eliminado:
        retorno = f"No se encontró ningún paciente con ID {dni}."
    elif desea_continuar("¿Está seguro que desea eliminar? (SI/NO): ", "Error. Ingrese (SI/NO): "):
        lista_pacientes.remove(eliminado)
        print("Eliminación hecha.")
        if desea_continuar("¿Desea deshacer la eliminación? (SI/NO): ", "Error. Ingrese (SI/NO): "):
            lista_pacientes.append(eliminado)
            retorno = "Eliminación cancelada."
        else:
            lista_pacientes_eliminados.append(eliminado)
            retorno = "Eliminación confirmada con éxito."
    else:
        retorno = "Eliminación deshecha."

    return retorno

def gestionar_eliminacion(lista_pacientes: list[dict], lista_pacientes_eliminados: list) -> str|tuple|bool:
    if comprobar_len_lista(lista_pacientes):
        retorno_dni = buscar_por_dni(lista_pacientes)
        if type(retorno_dni) == tuple:
            dni = retorno_dni[2]
            gestion = eliminar_paciente(lista_pacientes, lista_pacientes_eliminados, dni)
        else:
            gestion = retorno_dni
    else:
        gestion = "La lista está vacía, ingrese pacientes."
    
    return gestion
#endregion 



#region Funciones auxiliares
def buscar_por_dni(lista_pacientes: list[dict]) -> str:
    if comprobar_len_lista(lista_pacientes):
        dni = get_int("Ingrese DNI del paciente: ", "Error. Reingrese DNI: ", 50000000, 99999999, 3)
        if dni:
            paciente_encontrado = buscar_paciente(lista_pacientes, "dni", dni)
            if not paciente_encontrado:
                retorno = f"No se encontró ningún paciente con DNI: {dni}"
            else:
                retorno = ("Paciente encontrado.", paciente_encontrado, dni)
        else:
            retorno = "Se agotaron los intentos para ingresar datos."
    else:    
        retorno = "La lista está vacía, ingrese pacientes."
    
    return retorno

def determinar_tipo_dato_modificar(lista_grupos_sanguineos: list, dato_modificar: str) -> str|int|bool:
    retorno = True
    match dato_modificar:
        case "nombre":
            nombre = get_str_len("Ingrese nuevo nombre: ", "Error. Reingrese nombre: ", 1, 20, 3)
            if not nombre:
                retorno = False
            else:
                retorno = nombre
        case "apellido":
            apellido = get_str_len("Ingrese nuevo apellido: ", "Error. Reingrese apellido: ", 1, 20, 3)
            if not apellido:
                retorno = False
            else:
                retorno = apellido
        case "edad":
            edad = get_int("Ingrese nuevo edad: ", "Error. Reingrese edad: ", 1, 120, 3)
            if not edad:
                retorno = False
            else:
                retorno = edad
        case "altura":
            altura = get_int("Ingrese nuevo altura: ", "Error. Reingrese altura: ", 30, 230, 3)
            if not altura:
                retorno = False
            else:
                retorno = altura
        case "peso":
            peso = get_float("Ingrese nuevo peso: ", "Error. Reingrese peso: ", 10, 300, 3)
            if not peso:
                retorno = False
            else:
                retorno = peso
        case "dni":
            dni = get_int("Ingrese nuevo dni: ", "Error. Reingrese dni: ", 4000000, 9999999999, 3)
            if not dni:
                retorno = False
            else:
                retorno = dni
        case "grupo sanguineo":
            grupo_sanguineo = get_str_find("Ingrese nuevo grupo sanguineo: ", 
                                           "Error. Reingrese grupo sanguineo: ", 
                                            lista_grupos_sanguineos, 3)
            if not grupo_sanguineo:
                retorno = False
            else:
                retorno = grupo_sanguineo

    return retorno
#endregion

