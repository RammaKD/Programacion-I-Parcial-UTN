def desea_continuar(mensaje:str, mensaje_error: str) -> bool:
    """Pregunta al usuario si quiere continuar con una determinada funcion o no.

    Args:
        mensaje (str): recibe un mensaje si quiere seguir
        mensaje_error (str): recibe un mensaje de error si el usuario no ingresa
        SI / NO

    Returns:
        bool: retorna True si el usuario ingresó SI, y sino False.
    """
    while True:
        try:
            continuar = input(mensaje).lower()
            while continuar != "si" and continuar != "no":
                continuar = input(mensaje_error).lower()
            if continuar == "si":
                bandera_salir = True
                break
            else:
                bandera_salir = False
                break
        except:
            mensaje = mensaje_error
            
    
    return bandera_salir
    
def seleccionar_opcion_menu(mensaje: str) -> int:
    """Permite al usuario ingresar una opcion numérica del menu que quiera.
    Pero si la opcion no se encuentra retorna False 

    Args:
        mensaje (str): recibe una mensaje para seleccionar una opcion

    Returns:
        int|bool: retorna el número en caso de ser en entero, sino False.
    """
    try:
        opciones_menu = int(input(mensaje))
    except:
        opciones_menu = False

    return opciones_menu

def comprobar_len_lista(lista: list) -> bool:
    """Comprueba el largo de una lista, si está vacía o no.

    Args:
        lista (list): recibe una lista

    Returns:
        bool: devuelve False si el largo es 0, sino True
    """
    if len(lista) == 0:
        lenght = False
    else:
        lenght = True
    
    return lenght

def encontrar_ultimo_valor_en_lista_diccionarios(lista_diccionarios: list[dict], clave: str) -> int:
    """Encuentra el último valor de determinada clave en la lisra de diccionarios.

    Args:
        lista_diccionarios (list[dict]): recibe una lista de diccionarios
        clave (str): recibe la clave del último valor a encontrar

    Returns:
        int|float|str: retorna el último valor de la clave solicitada.
    """
    value = 0
    for diccionario in lista_diccionarios:
        posible_valor = diccionario[clave]
        if posible_valor != 0:
            value = posible_valor
            
    return value

def incrementar_id (lista_diccionarios:list[dict]) -> int:
    """Suma 1 al último ID de la lista de diccionarios que recibe.

    Args:
        lista_diccionarios (list[dict]): recibe una lista de diccionarios

    Returns:
        int: retorna el id incrementado
    """
    ultimo_id = encontrar_ultimo_valor_en_lista_diccionarios(lista_diccionarios, "id")
    id_incrementado = ultimo_id + 1
    return id_incrementado

def crear_lista_keys(lista_diccionarios: list[dict]) -> list:
    """Crea una lista con las keys de una lista de diccionarios.

    Args:
        lista_diccionarios (list[dict]): recibe una lista de diccionarios

    Returns:
        list: retorna la lista con las keys encontradas, sin repetirse.
    """
    claves_unicas = set()
    for empleado in lista_diccionarios:
        claves_unicas.update(empleado.keys())
    lista_parametros = list(claves_unicas)

    return lista_parametros

