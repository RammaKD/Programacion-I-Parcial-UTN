from os import system
from inputs import *
from generales import *
from funciones_archivos import *

#region Create
def crear_paciente(id: int,nombre: str,apellido: str, edad: int, altura: int, peso: float, dni: int, grupo_sanguineo: str) -> dict:
    """Crea un diccionario con las claves y valores de cada paciente.

    Args:
        id (int): recibe ID del paciente
        nombre (str): recibe nombre del paciente
        apellido (str): recibe apellido del paciente
        edad (int): recibe edad del paciente
        altura (int): recibe altura del paciente
        peso (float): recibe peso del paciente
        dni (int): recibe DNI del paciente
        grupo_sanguineo (str): recibe grupo sanguíneo del paciente

    Returns:
        dict: diccionario con los datos del paciente
    """
    diccionario_empleado = {
        "id" : int(id),
        "nombre" : nombre,
        "apellido" : apellido,
        "edad" : int(edad),
        "altura" : int(altura),
        "peso" : float(peso),
        "dni" : int(dni),
        "grupo sanguineo" : grupo_sanguineo
    }
    return diccionario_empleado

def ingresar_paciente_lista(lista_pacientes: list[dict], un_paciente: dict) -> list[dict]:
    """Se encarga de agregar a la lista de pacientes el nuevo paciente.

    Args:
        lista_pacientes (list[dict]): Recibe la lista de pacientes
        lista_grupos_sanguineos (list): Recibe lista de posibles grupos sanguíneos

    Returns:
        lista_pacientes (list[dict]): retorna la lista de pacientes con los datos añadidos
    """
    lista_pacientes.append(un_paciente)

    return lista_pacientes

def cargar_datos_paciente(lista_grupos_sanguineos: list, path_json_ultimo_id: str) -> bool|dict:
    """Carga los datos del paciente y guarda un diccionario, luego lo retorna si no hubo error.

    Args:
        lista_pacientes (list[dict]): recibe la lista de pacientes
        lista_grupos_sanguineos (list): recibe la lista de posibles grupos sanguineos

    Returns:
        bool|dict: retorna False si algun dato no paso la validacion, sino el diccionario.
    """
    datos = obtener_datos(lista_grupos_sanguineos, path_json_ultimo_id)
    if not datos:
        retorno = False
    else:
        diccionario_paciente = crear_paciente(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7])
        retorno = diccionario_paciente
        

    return retorno
#endregion

#region Read
def mostrar_lista_pacientes(lista_pacientes: list[dict]) -> str:
    """Muestra la información de la lista de pacientes en formato tabla

    Args:
        lista_pacientes (list[dict]): Recibe la lista de pacientes

    Returns:
        str: mensaje si la lista fue mostrada con éxito o si la lista está vacía
    """
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
    """Muestra la información de un paciente.

    Args:
        un_paciente (dict): Recibe un paciente de la lista

    Returns:
        dict: diccionario del paciente 
    """
    print(f"{un_paciente["id"]}|{un_paciente['nombre']:<20}|{un_paciente['apellido']:<20}|{un_paciente['edad']:<15}|{un_paciente['altura']:<15}|{un_paciente['peso']:<15}|{un_paciente['dni']:<15}|{un_paciente['grupo sanguineo']:<15}|")
    
    return un_paciente

def mostrar_un_paciente_con_tabla(un_paciente: dict) -> dict:
    """Muestra la información de un empleado con la tabla encima.

    Args:
        un_paciente (dict): _description_

    Returns:
        dict: _description_
    """
    print("***************************************************************************************************************************")
    print("|       Nombre       |      Apellido      |     Edad      |   Altura(cm)  |    Peso(KG)   |      DNI      |Grupo sanguíneo|")
    print("---------------------------------------------------------------------------------------------------------------------------")
    print(f"{un_paciente["id"]}|{un_paciente['nombre']:<20}|{un_paciente['apellido']:<20}|{un_paciente['edad']:<15}|{un_paciente['altura']:<15}|{un_paciente['peso']:<15}|{un_paciente['dni']:<15}|{un_paciente['grupo sanguineo']:<15}|")
    print("***************************************************************************************************************************")

    return un_paciente

def buscar_paciente(lista_pacientes: list[dict], clave: str, valor: int|str) -> dict|bool:
    """Se encarga de buscar un paciente en la lista de pacientes.

    Args:
        lista_pacientes (list[dict]): lista de pacientes
        clave (str): una clave para realizar la busqueda
        valor (int | str): un valor para realizar la busqueda

    Returns:
        dict|bool: si se encuentra retorna diccionario del paciente,
        sino retorna False.
    """
    retorno = False
    for paciente in lista_pacientes:
        if paciente[clave] == valor:
            mostrar_un_paciente_con_tabla(paciente)
            retorno = paciente
            break
    
    return retorno
#endregion

#region Update
def modificar_paciente(lista_grupos_sanguineos: list, un_paciente: dict, dato_a_modificar: str) -> str:
    """Se encarga de modificar al empleado solicitado.
    
    Args:
        lista_grupos_sanguineos (list): recibe lista de posibles grupos sanguineos
        un_paciente (dict): recibe un paciente a modificar
        dato_a_modificar (str): el dato que se quiere modificar del paciente

    Returns:
        str: retorna mensaje del resultado de la modificación
    """
    nuevo_dato = obtener_dato_a_modificar(lista_grupos_sanguineos, dato_a_modificar)
    estado_anterior = un_paciente[dato_a_modificar]
    
    if not nuevo_dato:
        retorno = "Se agotaron los intentos para ingresar nuevo dato."
        mostrar_un_paciente_con_tabla(un_paciente)
    elif desea_continuar("¿Desea efectuar el cambio? (SI/NO): ", "Error. Ingrese (SI/NO): "):
        un_paciente[dato_a_modificar] = nuevo_dato
        mostrar_un_paciente_con_tabla(un_paciente)
        retorno = "Paciente modificado."
        if deshacer_modificacion(un_paciente, dato_a_modificar, estado_anterior):
            retorno = "Se deshicieron los cambios."
        else:
            retorno = f"Cambio/s confirmado/s con éxito.\nNuevo dato: {nuevo_dato}\nDato antiguo: {estado_anterior}"
    else:
        mostrar_un_paciente_con_tabla(un_paciente)
        retorno = "Cambio deshecho."

    return retorno

def deshacer_modificacion(un_paciente: dict, dato_modificar: str, estado_anterior: str|int|float) -> bool:
    """Se encarga de deshacer una modificación si el usuario lo desea.

    Args:
        un_paciente (dict): recibe paciente al cual se quiere deshacer el cambio
        dato_modificar (str): recibe el dato a deshacer 
        estado_anterior (dict): recibe el dato anterior a la modificacion

    Returns:
        bool: retorna True si se deshizo la modificación, sino False.
    """
    if desea_continuar("¿Desea deshacer el cambio? (SI/NO): ", "Error. Ingrese (SI/NO): "):
        un_paciente[dato_modificar] = estado_anterior
        mostrar_un_paciente_con_tabla(un_paciente)
        retorno = True
    else:
        retorno = False

    return retorno
#endregion

#region Delete
def eliminar_paciente(lista_pacientes: list[dict], eliminado: dict) -> str:
    """Se encarga de eliminar un paciente de la lista de pacientes.

    Args:
        lista_pacientes (list[dict]): recibe la lista de pacientes
        lista_pacientes_eliminados (list): recibe la lista de pacientes eliminados
        eliminado (dict): recibe el paciente a eliminar

    Returns:
        str: mensaje con el resultado de la eliminacion
    """
    if desea_continuar("¿Está seguro que desea eliminar? (SI/NO): ", "Error. Ingrese (SI/NO): "):
        lista_pacientes.remove(eliminado)
        print("Eliminación hecha.")
        if deshacer_eliminacion(lista_pacientes, eliminado):
            retorno = "Eliminación cancelada."
        else:
            retorno = "Eliminación confirmada con éxito."
    else:
        retorno = "Eliminación deshecha."

    return retorno

def deshacer_eliminacion(lista_pacientes: list[dict], eliminado: dict) -> bool:
    """Se encarga de deshacer la eliminacion de un paciente si el usuario lo desea.
    Si no quiere deshacer la eliminacion, agrega al eliminado a la lista de 
    pacientes eliminados.

    Args:
        lista_pacientes (list[dict]): recibe lista de pacientes
        lista_pacientes_eliminados (list): recibe lista de pacientes eliminados
        eliminado (dict): recibe el paciente eliminado

    Returns:
        _bool_: retorna True si se deshizo la eliminación, sino False 
    """
    if desea_continuar("¿Desea deshacer la eliminación? (SI/NO): ", "Error. Ingrese (SI/NO): "):
        lista_pacientes.append(eliminado)
        retorno = True
    else:
        retorno = False

    return retorno
#endregion 

#######################################################################################################################################

#region Gestión
def gestionar_ingreso(lista_pacientes: list[dict], lista_grupos_sanguineos: list, path_json_ultimo_id: str) -> str:
    """Permite al usuario cargar paciente llamando a sus respectivas funciones.
    Notifica con un mensaje si el ingreso fue exitoso o no.

    Args:
        lista_pacientes (list[dict]): recibe la lista de paciente
        lista_grupos_sanguineos (list): recibe la lista de posibles grupos sanguineos

    Returns:
        str: retorna un mensaje detallando el resultado del ingreso.
    """
    retorno = "Ingreso exitoso."
    while True:
        paciente_nuevo = cargar_datos_paciente(lista_grupos_sanguineos, path_json_ultimo_id)
        if not paciente_nuevo:
            retorno = "Ingreso fallido. Se agotaron los intentos para ingresar datos."
            break
        else:
            ingresar_paciente_lista(lista_pacientes, paciente_nuevo)
            if not desea_continuar("Desea seguir cargando (SI/NO)?: ", "Error. Ingrese SI/NO: "):
                break
    
    return retorno

def gestionar_modificacion(lista_pacientes: list[dict], lista_grupos_sanguineos: list, minimo: int, maximo: int, reintentos: int) -> str:
    """Permite buscar un paciente por DNI en la lista y, si se encuentra, poder, modificar sus datos. 
    Si la lista esta vacía, no se encuentra al paciente o
    se agotan los intentos, se notifica al usuario.

    Args:
        lista_pacientes (list[dict]): Lista de pacientes
        lista_grupos_sanguineos (list): lista de posibles grupo sanguineos
        minimo (int): recibe un minimo para pasarle a la funcion de buscar por dni
        maximo (int): recibe un maximo para pasarle a la funcion de buscar por dni
        reintentos (int): recibe una cant. de reintentos para pasarle a la función
        de buscar por dni.

    Returns:
        str: mensaje del resultado de la gestión de la modificación
    """
    if comprobar_len_lista(lista_pacientes):
        resultado_busqueda = buscar_por_dni(lista_pacientes, minimo, maximo, reintentos)
        if type(resultado_busqueda) == dict:
            empleado_encontrado = resultado_busqueda
            ejecutar_menu_modificacion(lista_grupos_sanguineos, empleado_encontrado)
            gestion = "Modificación finalizada."
        elif resultado_busqueda == False:
            gestion = "No se encontró ningún paciente con ese DNI."
        else:
            gestion = "Se agotaron los intentos para ingresar datos."
    else:
        gestion = "La lista está vacía, ingrese pacientes."
    
    return gestion

def gestionar_eliminacion(lista_pacientes: list[dict], minimo: int, maximo: int, reintentos: int) -> str:
    """Permite buscar un paciente por DNI en la lista y, si se encuentra, poder eliminarlo. 
    Ademas notifica si la lista esta vacía, no se encuentra al paciente o
    se agotan los intentos.

    Args:
        lista_pacientes (list[dict]): Lista de pacientes
        lista_grupos_sanguineos (list): lista de posibles grupo sanguineos
        minimo (int): recibe un minimo para pasarle a la funcion de buscar por dni
        maximo (int): recibe un maximo para pasarle a la funcion de buscar por dni
        reintentos (int): recibe una cant. de reintentos para pasarle a la función
        de buscar por dni.

    Returns:
        str: mensaje del resultado de la gestión de la eliminación
    """
    if comprobar_len_lista(lista_pacientes):
        retorno_dni = buscar_por_dni(lista_pacientes, minimo, maximo, reintentos)
        if type(retorno_dni) == dict:
            paciente_a_eliminar = retorno_dni
            gestion = eliminar_paciente(lista_pacientes, paciente_a_eliminar)
        elif retorno_dni == False:
            gestion = "No se encontró ningún paciente con ese DNI."
        else:
            gestion = "Se agotaron los intentos para ingresar datos."
    else:
        gestion = "La lista está vacía, ingrese pacientes."
    
    return gestion

def gestionar_busqueda_por_dni(lista_pacientes: list[dict], minimo: int, maximo: int, reintentos: int) -> str:
    """Permite al usuario buscar un paciente por su DNI y notificar el resultado de la busqueda.
    Args:
        lista_pacientes (list[dict]): recibe la lista de pacientes
        minimo (int): recibe un minimo 
        maximo (int): recibe un maximo
        reintentos (int): recibe cant. maxima de reintentos

    Returns:
        str: mensaje del resultado de la busqueda, si la hubo.
    """
    if comprobar_len_lista(lista_pacientes):
        resultado_busqueda = buscar_por_dni(lista_pacientes, minimo, maximo, reintentos)
        if type(resultado_busqueda) == dict:
            retorno = "Paciente encontrado con éxito."
        elif resultado_busqueda == False:
            retorno = "No se encontró ningún paciente con ese DNI."
        else:
            retorno = "Se agotaron los intentos para ingresar datos."
    else:
        retorno = "La lista está vacía, ingrese pacientes."

    return retorno

def gestionar_promedio(lista_pacientes: list[dict]) -> str:
    """Notifica al usuario si las operaciones de promedio finalizaron. 
    Sino, si la lista está vacia.

    Args:
        lista_pacientes (list[dict]): recibe la lista de pacientes

    Returns:
        str: mensaje si el calculo de los promedios finalizó o si la lista está
        vacía
    """
    if comprobar_len_lista(lista_pacientes):
        ejecutar_menu_promedio(lista_pacientes)
        retorno = "Cálculo de promedio finalizado."
    else:
        retorno = "La lista esta vacía, ingrese pacientes."

    return retorno

def gestionar_ordenamiento(lista_pacientes: list[dict]) -> str:
    """Notifica al usuario si la operaciones de ordenamiento finalizaron.
    Ademas indica si la lista esta vacia o si se agotaron los intentos para
    ingresar datos.

    Args:
        lista_pacientes (list[dict]): recibe la lista de pacientes

    Returns:
        str: mensaje si el ordenamiento terminó, si la lista esta vacia o 
        si los intentos se agotaron.
    """
    if comprobar_len_lista(lista_pacientes):
        posibles_flujos = ["ASCENDENTE", "DESCENDENTE"]
        flujo = pedir_flujo_ordenamiento(posibles_flujos, 5)
        if flujo:
            ejecutar_menu_ordenamiento(lista_pacientes, flujo)
            gestion = "Ordenamiento terminado."
        else:
            gestion = "Se agotaron los intentos para ingresar datos."
    else:
        gestion = "La lista está vacía, ingrese pacientes."
    
    
    return gestion

def gestionar_compatibilidad(lista_pacientes: list[dict], lista_diccionarios_compatibilidad, minimo, maximo, reintentos) -> str:
    """Permite al usuario poder determinar su compatibilidad sanguinea y notificar el resultado.

    Args:
        lista_pacientes (list[dict]): recibe la lista de pacientes
        lista_diccionarios_compatibilidad (_type_): recibe la lista de diccionarios de grupos sanguineos compatibles
        minimo (_type_): recibe un minimo para buscar por DNI
        maximo (_type_): recibe un maximo para buscar por DNI
        reintentos (_type_): recibe una cantidad de reintentos.

    Returns:
        _type_: retorna un mensaje indicando que sucedió
    """
    if comprobar_len_lista(lista_pacientes):
        paciente_encontrado = buscar_por_dni(lista_pacientes, minimo, maximo, reintentos)
        
        if paciente_encontrado == False:
            retorno = "Paciente no encontrado."
        elif paciente_encontrado == None:
            retorno = "Se agotaron los intentos para ingresar datos."
        else:
            posibles_grupos_sanguineos_donantes = determinar_posibles_grupos_sanguineos_donantes(lista_diccionarios_compatibilidad, paciente_encontrado)
            mostrar_compatibilidades(paciente_encontrado, lista_diccionarios_compatibilidad)
            determinar_donantes(lista_pacientes, posibles_grupos_sanguineos_donantes, paciente_encontrado)
            retorno = "Compatibilidad finalizada."
    else:
        retorno = "La lista esta vacía, ingrese pacientes."
  
    
    return retorno
#endregion

#region Funciones auxiliares
def buscar_por_dni(lista_pacientes: list[dict], minimo: int, maximo: int, reintentos: int) -> dict|bool|None:
    """Permite al usuario buscar un paciente por su DNI, llamando a su respectiva funcion.
    Si lo encuentra devuelve el paciente, sino False.
    Si se agotaron los intentos, devuelve None.

    Args:
        lista_pacientes (list[dict]): recibe la lista de pacientes
        minimo (int): recibe minimo
        maximo (int): recibe maximo
        reintentos (int): recibe cantidad maxima de reintentos

    Returns:
        dict|bool|None: devuelve False si no se encontró, diccionario si se,
        encontró, y si se agotaron los intentos None.
    """
    dni = pedir_dni(minimo, maximo, reintentos)
    if dni:
        paciente_encontrado = buscar_paciente(lista_pacientes, "dni", dni)
        if not paciente_encontrado:
            retorno = False
        else:
            retorno = paciente_encontrado
    else:
        retorno = None

    
    return retorno

def obtener_datos(lista_grupos_sanguineos: list, path_json_ultimo_id: str) -> bool|tuple:
    """Se encarga de obtener los datos de los pacientes y retornarlos en una tupla.

    Args:
        lista_pacientes (list[dict]): recibe la lista de pacientes
        lista_grupos_sanguineos (list): recibe la lista de posibles grupos sanguineos

    Returns:
        bool|tuple: retorna False si no se pasó la validación de algun dato sino,
        la tupla con los datos.
    """
    retorno = False
    while True:
        nombre = pedir_nombre(1, 20, 5)
        if not nombre:
            break
        apellido = pedir_apellido(1, 20, 5)
        if not apellido:
            break
        edad = pedir_edad(1, 120, 5)
        if not edad:
            break
        altura = pedir_altura(30, 230, 5)
        if not altura:
            break 
        peso = pedir_peso(10, 300, 5)
        if not peso:
            break
        dni = pedir_dni(4000000, 99999999, 5)
        if not dni:
            break
        grupo_sanguineo = pedir_grupo_sanguineo(lista_grupos_sanguineos, 5)
        if not grupo_sanguineo:
            break
        id = incrementar_id(path_json_ultimo_id)
        retorno = (id, nombre, apellido, edad, altura, peso, dni, grupo_sanguineo)
        break
    
    
    return retorno

def obtener_dato_a_modificar(lista_grupos_sanguineos: list, dato_a_modificar: str) -> str|int|float|bool:
    """Se encarga de obtener el nuevo dato a modificar del paciente.

    Args:
        lista_grupos_sanguineos (list): recibe lista de posibles grupo sanguineo
        dato_a_modificar (str): recibe el tipo de dato que se quiere modificar

    Returns:
        str|int|float|bool: devuelve False si se agotaron los intentos, sino,
        el dato solicitado.
    """
    retorno = True
    match dato_a_modificar:
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

def calcular_promedio(lista_pacientes: list[dict], clave: str) -> str:
    """Calcula el promedio de los datos que el usuario desee.

    Args:
        lista_pacientes (list[dict]): recibe la lista de pacientes
        clave (str): recibe la clave de lo valores que se quiere calcular el promedio

    Returns:
        str: retorna mensaje con el promedio
    """
    acumulador_valores = 0
    for paciente in lista_pacientes:
        acumulador_valores += paciente[clave]
    promedio = acumulador_valores / len(lista_pacientes)
    retorno = f"El promedio de {clave} de los pacientes es de: {promedio}"
    
    return retorno

def ordenar_elementos_ascendente_descendente(lista_pacientes: list[dict], parametro: str, flujo: str) -> list[dict]:
    """Ordena elementos de forma ascendente o descendente segun el usuario quiera.
    
    Args:
        lista_pacientes (list[dict]): recibe la lista de pacientes a ordenar
        parametro (str): recibe la clave de los valores bajo el cual se quiere ordenar
        flujo (str): recibe el flujo, ya sea, ascendente o descendente

    Returns:
        list[dict]: retorna la lista de pacientes ordenada.
    """
    for i in range(0, len(lista_pacientes) - 1):
        for j in range(i + 1, len(lista_pacientes)):
            if flujo == "ASCENDENTE":
                if lista_pacientes[i][parametro] > lista_pacientes[j][parametro]:
                    lista_pacientes[i], lista_pacientes[j] = swap(lista_pacientes[i], lista_pacientes[j])
            else:
                if lista_pacientes[i][parametro] < lista_pacientes[j][parametro]:
                    lista_pacientes[i], lista_pacientes[j] = swap(lista_pacientes[i], lista_pacientes[j])
    
    mostrar_lista_pacientes(lista_pacientes)
    print("Pacientes ordenados con éxito.")
    retorno = lista_pacientes
    
    if desea_continuar("Desea seguir ordenando (SI/NO)?", "Error. Ingrese SI/NO."):
        gestionar_ordenamiento(lista_pacientes)

    return retorno

def swap(a, b):
    """Intercambiar dos variables de lugar.

    Args:
        a (_type_): recibe una variable
        b (_type_): recibe otra variable

    Returns:
        _type_: retorna las variables en posicion opuesta
    """
    return b, a

def determinar_donantes(lista_pacientes: list[dict], posibles_grupos_sanguineos: list, paciente_a_donar: dict) -> list[dict]:
    """Muestra los posibles donantes del paciente que se está analizando.

    Args:
        lista_pacientes (list[dict]): recibe la lista de paciente
        posibles_grupos_sanguineos (_type_): recibe la lista de grupos sanguineos compatibles
        paciente_a_donar (dict): recibe un paciente al cual se le va a donar.

    Returns:
        list[dict]: retorna la lista de donantes
    """
    lista_donantes = []
    contador_donantes_maximos = 0

    for paciente in lista_pacientes:
        if paciente["grupo sanguineo"] in posibles_grupos_sanguineos[0][1] and contador_donantes_maximos < 3:
            if paciente["id"] != paciente_a_donar["id"]:
                contador_donantes_maximos += 1
                lista_donantes.append(paciente)
    
    if len(lista_donantes) > 0:
        mostrar_lista_pacientes(lista_donantes)
        print("Posibles donantes mostrados.")
    else:
        print("No hay donantes disponibles.")

    return lista_donantes

def determinar_posibles_grupos_sanguineos_donantes(lista_diccionarios_compatibilidad: list[dict], un_paciente: list[dict]) -> list:
    """Crea una lista con los posibles grupos sanguineos

    Args:
        lista_diccionarios_compatibilidad (list[dict]): recibe la lista de diccionarios de grupos sanguineo compatibles
        un_paciente (list[dict]): recibe un paciente

    Returns:
        _type_: retorna la lista de posibles grupos sanguineos compatibles
    """
    grupo_sanguineo_paciente = un_paciente["grupo sanguineo"]
    posibles_grupos_sanguineo = []
    
    for diccionario in lista_diccionarios_compatibilidad:
        if diccionario["grupo sanguineo"][0] == grupo_sanguineo_paciente:
            grupos_compatibles = diccionario["grupo sanguineo"][1], diccionario["grupo sanguineo"][2]
            posibles_grupos_sanguineo.append(grupos_compatibles)

    return posibles_grupos_sanguineo

def mostrar_compatibilidades(un_paciente: dict, lista_diccionarios_compatibilidad: dict) -> dict:
    """Se encarga de mostrar las compatibilidades de un paciente

    Args:
        un_paciente (dict): recibe un paciente
        lista_diccionarios_compatibilidad (dict): recibe la lista de diccionarios de grupos sanguineo compatibles

    Returns:
        _type_: retorna el paciente
    """
    grupo_sanguineo_paciente = un_paciente["grupo sanguineo"]
    for diccionario in lista_diccionarios_compatibilidad:
        if diccionario["grupo sanguineo"][0] == grupo_sanguineo_paciente:
            print(f"Puede donar a: {diccionario['grupo sanguineo'][1]}")
            print(f"Puede recibir de: {diccionario['grupo sanguineo'][2]}")
            break
    return un_paciente
#endregion

#region Menus
def ejecutar_menu_ordenamiento(lista_pacientes: list[dict], flujo: str):
    """Ejecuta el menu de ordenamiento, con sus opciones.

    Args:
        lista_pacientes (list[dict]): recibe la lista de pacientes
        flujo (str): recibe el flujo, ascendente o descendente
    """
    continuar_ordenamiento = True
    while continuar_ordenamiento:
        mostrar_opciones_menu_ordenamiento()
        opcion_ordenamiento = seleccionar_opcion_menu("Seleccione una opción: ")
        match opcion_ordenamiento:
            case 1:
                ordenar_elementos_ascendente_descendente(lista_pacientes, "nombre", flujo)
                break
            case 2:
                ordenar_elementos_ascendente_descendente(lista_pacientes, "apellido", flujo)
                break
            case 3:
                ordenar_elementos_ascendente_descendente(lista_pacientes, "altura", flujo)
                break
            case 4:
                ordenar_elementos_ascendente_descendente(lista_pacientes, "grupo sanguineo", flujo)
                break
            case 5:
                if desea_continuar("Desea salir? (SI/NO): ", "Error. Ingrese SI/NO: "):
                    continuar_ordenamiento = False
                    break
            case _:
                system("cls")
                print("Entrada no válida. Ingrese una opción del Menú.")    

def ejecutar_menu_promedio(lista_pacientes: list[dict]):
    """Ejecuta el menu de promedio, con sus opciones.

    Args:
        lista_pacientes (list[dict]): recibe la lista de pacientes
    """
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
    
def ejecutar_menu_modificacion(lista_grupos_sanguineos: list, paciente_encontrado: dict):
    """Ejecuta el menu de modificacion, con sus opciones

    Args:
        lista_grupos_sanguineos (list): recibe la lista de posibles grupos sanguineos
        paciente_encontrado (dict): recibe el paciente encontrado
    """
    continuar_modificacion = True
    while continuar_modificacion:
        mostrar_opciones_menu_modificacion()
        opcion_modificacion = seleccionar_opcion_menu("Seleccione una opción: ")

        match opcion_modificacion:
                case 1:
                    system("cls")
                    print(modificar_paciente(lista_grupos_sanguineos, paciente_encontrado, "nombre"))
                case 2:
                    system("cls")
                    print(modificar_paciente(lista_grupos_sanguineos, paciente_encontrado, "apellido"))
                case 3:
                    system("cls")
                    print(modificar_paciente(lista_grupos_sanguineos, paciente_encontrado, "edad"))
                case 4:
                    system("cls")
                    print(modificar_paciente(lista_grupos_sanguineos, paciente_encontrado, "altura"))
                case 5:
                    system("cls")
                    print(modificar_paciente(lista_grupos_sanguineos, paciente_encontrado, "peso"))
                case 6:
                    system("cls")
                    print(modificar_paciente(lista_grupos_sanguineos, paciente_encontrado, "dni"))
                case 7:
                    system("cls")
                    print(modificar_paciente(lista_grupos_sanguineos, paciente_encontrado, "grupo sanguineo"))
                case 8:
                    system("cls")
                    if desea_continuar("Desea salir? (SI/NO): ", "Error. Ingrese SI/NO: "):
                        continuar_modificacion = False
                        break
                case _:
                    system("cls")
                    print("Entrada no válida. Ingrese una opción del Menú.")
#endregion

#region Opciones menús
def mostrar_opciones_menu_ordenamiento():
    """Muestra las opciones del menu de ordenamiento
    """
    print("\nMenú ordenamiento")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Altura")
    print("4. Grupo sanguíneo")
    print("5. Salir")
    
def mostrar_opciones_menu_promedio():
    """Muestra las opciones del menu de promedio
    """
    print("\nMenú promedio")
    print("1. Edad")
    print("2. Altura")
    print("3. Peso")
    print("4. Salir")

def mostrar_opciones_menu_modificacion():
    """Muestra las opciones del menu de modificacion
    """
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
    """Muestra las opciones del menu principal
    """
    print("\nMenú")
    print("1. Dar de alta")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar todos")
    print("5. Ordenar pacientes")
    print("6. Buscar paciente por DNI")
    print("7. Calcular promedio")
    print("8. Determinar compatibilidad.")
    print("9. Salir")
#endregion



