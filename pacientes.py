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

def ingresar_paciente(lista_pacientes: list[dict], lista_grupos_sanguineos: list) -> str:
    retorno = "Ingreso exitoso."
    
    while True:
        nombre = pedir_nombre(1, 20, 5)
        if not nombre:
            retorno = "Se agotaron los intentos para ingresar datos."
            break
        apellido = pedir_apellido(1, 20, 5)
        if not apellido:
            retorno = "Se agotaron los intentos para ingresar datos."
            break
        edad = pedir_edad(1, 120, 5)
        if not edad:
            retorno = "Se agotaron los intentos para ingresar datos."
            break
        altura = pedir_altura(30, 230, 5)
        if not altura:
            retorno = "Se agotaron los intentos para ingresar datos."
            break 
        peso = pedir_peso(10, 300, 5)
        if not peso:
            retorno = "Se agotaron los intentos para ingresar datos."
            break
        dni = pedir_dni(4000000, 99999999, 5)
        if not dni:
            retorno = "Se agotaron los intentos para ingresar datos."
            break
        grupo_sanguineo = pedir_grupo_sanguineo(lista_grupos_sanguineos, 5)
        if not grupo_sanguineo:
            retorno = "Se agotaron los intentos para ingresar datos."
            break

        id = incrementar_id(lista_pacientes)
        diccionario_paciente = crear_paciente(id, nombre, apellido, edad, altura, peso, dni, grupo_sanguineo)
        lista_pacientes.append(diccionario_paciente)

        if not desea_continuar("¿Desea seguir cargando? (SI/NO): ", "Error. Ingrese SI/NO: "):
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
    print(f"{un_paciente["id"]}|{un_paciente['nombre']:<20}|{un_paciente['apellido']:<20}|{un_paciente['edad']:<15}|{un_paciente['altura']:<15}|{un_paciente['peso']:<15}|{un_paciente['dni']:<15}|{un_paciente['grupo sanguineo']:<15}|")
    return un_paciente

def buscar_paciente(lista_pacientes: list[dict], clave: str, valor: int|str) -> dict|bool:
    retorno = False
    for paciente in lista_pacientes:
        if paciente[clave] == valor:
            mostrar_paciente(paciente)
            retorno = paciente
            break
    
    return retorno
#endregion

#region Update
def modificar_empleado(lista_grupos_sanguineos: list, un_paciente: dict, dato_modificar: str) -> str:
    nuevo_dato = obtener_dato_a_modificar(lista_grupos_sanguineos, dato_modificar)
    estado_anterior = un_paciente[dato_modificar]
    
    if not nuevo_dato:
        retorno = "Se agotaron los intentos para ingresar nuevo dato."
        mostrar_paciente(un_paciente)
    elif desea_continuar("¿Desea efectuar el cambio? (SI/NO): ", "Error. Ingrese (SI/NO): "):
        un_paciente[dato_modificar] = nuevo_dato
        mostrar_paciente(un_paciente)
        retorno = "Paciente modificado."
        if desea_continuar("¿Desea deshacer el cambio? (SI/NO): ", "Error. Ingrese (SI/NO): "):
            un_paciente[dato_modificar] = estado_anterior
            mostrar_paciente(un_paciente)
            retorno = "Se deshicieron los cambios."
        else:
            retorno = f"Cambio/s confirmado/s con éxito.\nNuevo dato: {nuevo_dato}\nDato antiguo: {estado_anterior}"
    else:
        mostrar_paciente(un_paciente)
        retorno = "Cambio deshecho."

    return retorno

def menu_modificacion(lista_grupos_sanguineos: list, paciente_encontrado: dict) -> bool:
    print("Paciente encontrado.")
    continuar_modificacion = True
    while continuar_modificacion:
        mostrar_opciones_menu_modificacion()
        opcion_modificacion = seleccionar_opcion_menu("Seleccione una opción: ")

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

def gestionar_modificacion(lista_pacientes: list[dict], lista_grupos_sanguineos: list) -> str:
    if comprobar_len_lista(lista_pacientes):
        resultado_busqueda = busqueda_por_dni(lista_pacientes, 4000000, 99999999, 5)
        if type(resultado_busqueda) == dict:
            empleado_encontrado = resultado_busqueda
            menu_modificacion(lista_grupos_sanguineos, empleado_encontrado)
            gestion = "Modificación finalizada."
        elif resultado_busqueda == False:
            gestion = "No se encontró ningún paciente con ese DNI."
        else:
            gestion = "Se agotaron los intentos para ingresar datos."
    else:
        gestion = "La lista está vacía, ingrese pacientes."
    
    return gestion
#endregion

#region Delete
def eliminar_paciente(lista_pacientes: list[dict], lista_pacientes_eliminados: list, eliminado: dict) -> str:
    if desea_continuar("¿Está seguro que desea eliminar? (SI/NO): ", "Error. Ingrese (SI/NO): "):
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
   
def gestionar_eliminacion(lista_pacientes: list[dict], lista_pacientes_eliminados: list) -> str:
    if comprobar_len_lista(lista_pacientes):
        retorno_dni = busqueda_por_dni(lista_pacientes, 4000000, 99999999, 5)
        if type(retorno_dni) == dict:
            paciente_a_eliminar = retorno_dni
            gestion = eliminar_paciente(lista_pacientes, lista_pacientes_eliminados, paciente_a_eliminar)
        elif retorno_dni == False:
            gestion = "No se encontró ningún paciente con ese DNI."
        else:
            gestion = "Se agotaron los intentos para ingresar datos."
    else:
        gestion = "La lista está vacía, ingrese pacientes."
    
    return gestion
#endregion 

#region Funciones auxiliares
def busqueda_por_dni(lista_pacientes: list[dict]) -> dict|bool|None:
    dni = pedir_dni(4000000, 99999999, 5)
    if dni:
        paciente_encontrado = buscar_paciente(lista_pacientes, "dni", dni)
        if not paciente_encontrado:
            retorno = False
        else:
            retorno = paciente_encontrado
    else:
        retorno = None

    
    return retorno

def gestionar_busqueda_por_dni(lista_pacientes: list[dict], minimo: int, maximo: int, reintentos: int) -> str:
    if comprobar_len_lista(lista_pacientes):
        resultado_busqueda = busqueda_por_dni(lista_pacientes, minimo, maximo, reintentos)
        if type(resultado_busqueda) == dict:
            retorno = "Paciente encontrado con éxito."
        elif resultado_busqueda == False:
            retorno = "No se encontró ningún paciente con ese DNI."
        else:
            retorno = "Se agotaron los intentos para ingresar datos."
    else:
        retorno = "La lista está vacía, ingrese pacientes."

    return retorno

def obtener_dato_a_modificar(lista_grupos_sanguineos: list, dato_modificar: str) -> str|int|float|bool:
    retorno = True
    match dato_modificar:
        case "nombre":
            nombre = pedir_nombre(1, 20, 5)
            retorno = nombre
        case "apellido":
            apellido = pedir_apellido(1, 20, 5)
            retorno = apellido
        case "edad":
            edad = pedir_edad(1, 120, 5)
            retorno = edad
        case "altura":
            altura = pedir_altura(30, 230, 5)
            retorno = altura
        case "peso":
            peso = pedir_peso(10, 300, 5)
            retorno = peso
        case "dni":
            dni = pedir_dni(4000000, 99999999)
            retorno = dni
        case "grupo sanguineo":
            grupo_sanguineo = pedir_grupo_sanguineo(lista_grupos_sanguineos, 5)
            retorno = grupo_sanguineo

    return retorno
#endregion

#region Promedio
def gestionar_promedio(lista_pacientes: list[dict]) -> str:
    if comprobar_len_lista(lista_pacientes):
        menu_promedio(lista_pacientes)
        retorno = "Cálculo de promedio finalizado."
    else:
        retorno = "La lista esta vacía, ingrese pacientes."

    return retorno

def menu_promedio(lista_pacientes: list[dict]):
    continuar_promedio = True
    while continuar_promedio:
        mostrar_opciones_menu_promedio()
        opcion_promedio = seleccionar_opcion_menu("Seleccione una opción: ")
        match opcion_promedio:
            case 1:
                print(calcular_promedio(lista_pacientes, "edad"))
            case 2:
                print(f"{calcular_promedio(lista_pacientes, "altura")}cm")
            case 3:
                print(f"{calcular_promedio(lista_pacientes, "peso")}Kg")
            case 4:
                system("cls")
                if desea_continuar("Desea salir? (SI/NO): ", "Error. Ingrese SI/NO: "):
                    continuar_promedio = False
                    break
            case _:
                system("cls")
                print("Entrada no válida. Ingrese una opción del Menú.")
    

    return continuar_promedio

def calcular_promedio(lista_pacientes: list[dict], clave: str):
    acumulador_valores = 0
    for paciente in lista_pacientes:
        acumulador_valores += paciente[clave]
    promedio = acumulador_valores / len(lista_pacientes)
    retorno = f"El promedio de {clave} de los pacientes es de: {promedio}"
    

    return retorno
#endregion

#region Ordenamiento
def gestionar_ordenamiento(lista_pacientes: list[dict]) -> str:
    if comprobar_len_lista(lista_pacientes):
        posibles_flujos = ["ASCENDENTE", "DESCENDENTE"]
        flujo = pedir_flujo_ordenamiento(posibles_flujos, 5)
        if flujo:
            menu_ordenamiento(lista_pacientes, flujo)
            gestion = "Ordenamiento terminado."
        else:
            gestion = "Se agotaron los intentos para ingresar datos."
    else:
        gestion = "La lista está vacía, ingrese pacientes."
    
    
    return gestion

def menu_ordenamiento(lista_pacientes: list[dict], flujo: str):
    continuar_ordenamiento = True
    while continuar_ordenamiento:
        mostrar_opciones_menu_ordenamiento()
        opcion_ordenamiento = seleccionar_opcion_menu("Seleccione una opción: ")
        match opcion_ordenamiento:
            case 1:
                system("cls")
                print(ordenar_elementos_ascendente_descendente(lista_pacientes, "nombre", flujo)[0])
            case 2:
                system("cls")
                print(ordenar_elementos_ascendente_descendente(lista_pacientes, "apellido", flujo)[0])
            case 3:
                system("cls")
                print(ordenar_elementos_ascendente_descendente(lista_pacientes, "altura", flujo)[0])
            case 4:
                system("cls")
                print(ordenar_elementos_ascendente_descendente(lista_pacientes, "grupo sanguineo", flujo)[0])
            case 5:
                system("cls")
                if desea_continuar("Desea salir? (SI/NO): ", "Error. Ingrese SI/NO: "):
                    continuar_ordenamiento = False
                    break
            case _:
                system("cls")
                print("Entrada no válida. Ingrese una opción del Menú.")
    
    return continuar_ordenamiento

def ordenar_elementos_ascendente_descendente(lista_empleados: list[dict], parametro: str, flujo: str) -> list[dict]:
    for i in range(0, len(lista_empleados)):
        for j in range(0, len(lista_empleados) - i - 1):
            if flujo == "ASCENDENTE":
                if lista_empleados[j][parametro] > lista_empleados[j + 1][parametro]:
                    lista_empleados[j], lista_empleados[j + 1] = lista_empleados[j + 1], lista_empleados[j]
            else:
                if lista_empleados[j][parametro] < lista_empleados[j + 1][parametro]:
                    lista_empleados[j], lista_empleados[j + 1] = lista_empleados[j + 1], lista_empleados[j]
    
    mostrar_lista_pacientes(lista_empleados)
    retorno = (f"Pacientes ordenados con éxito.", lista_empleados)
    
    return retorno
#endregion

#region Opciones menús
def mostrar_opciones_menu_ordenamiento():
    print("\nMenú ordenamiento")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Altura")
    print("4. Grupo sanguíneo")
    print("5. Salir")
    
def mostrar_opciones_menu_promedio():
    print("\nMenú promedio")
    print("1. Edad")
    print("2. Altura")
    print("3. Peso")
    print("4. Salir")

def mostrar_opciones_menu_modificacion():
    print("\nMenú modificación")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Edad")
    print("4. Altura")
    print("5. Peso")
    print("6. Dni")
    print("7. Grupo sanguíneo")
    print("8. Salir")

def mostrar_opciones_menu_principal():
    print("\nMenú")
    print("1. Dar de alta")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar todos")
    print("5. Ordenar pacientes")
    print("6. Buscar paciente por DNI")
    print("7. Calcular promedio")
    print("8. Salir")
#endregion