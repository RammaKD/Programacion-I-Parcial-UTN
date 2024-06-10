#region Get
def get_str_len(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> str|bool:
    """Solicita al usuario una cadena y valida su longitud llamando a su funcion.
    Ademas valida si el contenido es alfabético o no

    Args:
        mensaje (str): mensaje a mostrar al solicitar la cadena
        mensaje_error (str): mensaje a mostrar en caso de error
        minimo (int): longitud minima permitida
        maximo (int): longitud maxima permitida
        reintentos (int): cant. maxima de reintentos permitidos

    Returns:
        str|bool: retorna la cadena si pasó la validacion y sino False.
    """
    contador_reintentos = 0
    cadena_validada = False
    
    while contador_reintentos <= reintentos:
        try:
            cadena_original = input(mensaje).strip()
            cadena = cadena_original.replace(" ", "")
            if cadena.isalpha():
                cadena_validada = validate_lenght(cadena.strip(""), minimo, maximo)
                if cadena_validada:
                    cadena_validada = metodo_title(cadena_original)
                    break
                else:
                    contador_reintentos += 1
                    mensaje = mensaje_error
            else:
                contador_reintentos += 1
                mensaje = "Error. Ingrese solo caracteres alfabéticos: "
        except:
            contador_reintentos += 1
            mensaje = "Error. Entrada no válida, reingrese dato: "
    
    return cadena_validada
            
def get_str_search(mensaje: str, mensaje_error: str, lista: list, reintentos: int) -> str|bool:
    """Solicita al usuario una cadena y valida si se encuentra en una lista dada.

    Args:
        mensaje (str): mensaje a mostrar al solicitar la cadena
        mensaje_error (str): mensaje a mostrar en caso de error
        lista (list): lista en la que se validará si la cadena se encuentra o no.
        reintentos (int): cant. maxima de reintentos permitidos 

    Returns:
        str|bool: retorna la cadena si se encontró, sino False
    """
    contador_reintentos = 0
    cadena_validada = False
    
    while contador_reintentos <= reintentos:
        try:
            cadena = input(mensaje).upper()
            if validate_string_search(cadena, lista):
                cadena_validada = cadena
                break
            else:
                contador_reintentos += 1
                mensaje = mensaje_error
        except:
            contador_reintentos += 1
            mensaje = "Error. Entrada no válida, reingrese dato: "

    return cadena_validada

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|bool:
    """Solicita al usuario un número entero y valida si se encuentra en un rango.

    Args:
        mensaje (str): mensaje a mostrar al solicitar el numero
        mensaje_error (str): mensaje a mostrar en caso de error
        minimo (int): valor minimo permitido
        maximo (int): valor maximo permitido
        reintentos (int): cant. maxima de reintentos permitidos

    Returns:
        int|bool: retorna el numero si pasó la validacion, sino False
    """
    contador_reintentos = 0
    numero_validado = False
    
    while contador_reintentos <= reintentos:
        try:
            numero = input(mensaje).strip()
            numero = int(numero)
            if validate_range(numero, minimo, maximo):
                numero_validado = numero
                break
            else:
                contador_reintentos += 1
                mensaje = mensaje_error
        except:
            contador_reintentos += 1
            mensaje = "Error. Ingrese solo caracteres numéricos: "

    return numero_validado
 
def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float|bool:
    """Solicita al usuario un número flotante y valida que esté dentro de un rango

    Args:
        mensaje (str): mensaje a mostrar al solicitar el numero
        mensaje_error (str): mensaje a mostrar en caso de error
        minimo (float): valor minimo permitido
        maximo (float): valor maximo permitido
        reintentos (int): cant. maxima de reintentos permitidos

    Returns:
        float|bool: retorna el numero si pasó la validación, sino False
    """
    contador_reintentos = 0
    numero_validado = False
    
    while contador_reintentos <= reintentos:
        try:
            numero = input(mensaje).strip()
            numero = float(numero)
            if validate_range(numero, minimo, maximo):
                numero_validado = numero
                break
            else:
                contador_reintentos += 1
                mensaje = mensaje_error

        except:
            contador_reintentos += 1
            mensaje = "Error. Ingrese solo caracteres numéricos: "

    return numero_validado
         
def get_validate_dni(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|bool:
    contador_reintentos = 0
    numero_validado = False
    
    while contador_reintentos <= reintentos:
        try:
            numero = input(mensaje).strip().zfill(8)
            numero = int(numero)
            if validate_range(numero, minimo, maximo):
                numero_validado = numero
                break
            else:
                contador_reintentos += 1
                mensaje = mensaje_error
        except:
            contador_reintentos += 1
            mensaje = "Error. Ingrese solo caracteres numéricos: "

    return numero_validado
#endregion

#region Validate
def validate_lenght(cadena: str, minimo: int, maximo: int) -> str|bool:
    """Valida el largo de una cadena bajo un minimo y un maximo.

    Args:
        cadena (str): recibe la cadena a validar
        minimo (int): recibe el minimo de largo que puede tener la cadena
        maximo (int): recibe el maximo de largo que puede tener la cadena

    Returns:
        str|bool: retorna la cadena si está en rango, sino False
    """
    if len(cadena) < minimo or len(cadena) > maximo:
        validacion = False
    else:
        validacion = cadena
    return validacion

def validate_string_search(cadena: str, lista: list) -> str|bool:
    """Valida si una cadena se encuentra dentro de una lista.

    Args:
        cadena (str): recibe la cadena a validar
        lista (list): recibe la lista

    Returns:
        str|bool: retorna la cadena si se encontró en la lista, sino False
    """
    validacion = False
    for elemento in lista:
        if elemento == cadena:
            validacion = cadena
            break
    
    return validacion

def validate_range(numero: int|float, minimo: int|float, maximo: int|float) -> int|float|bool:
    """Valida si un número se encuentra en un rango especificado

    Args:
        numero (int | float): recibe numero a validar
        minimo (int | float): recibe el minimo que puede tener el numero
        maximo (int | float): recibe el maximo que puede tener el numero

    Returns:
        int|float|bool: retorna el numero si está en rango, sino False
    """
    if numero < minimo or numero > maximo:
        validacion = False
    else:
        validacion = numero

    return validacion
#endregion 

#region Inputs específicos
def pedir_nombre(minimo: int, maximo: int, reintentos: int) -> str|bool:
    nombre = get_str_len(f"Ingrese nombre (Max. {maximo} caracteres): ", 
             f"Error. Reingrese nombre (Max. {maximo} caracteres): ", 
             minimo, maximo, reintentos)
    
    return nombre

def pedir_apellido(minimo: int, maximo: int, reintentos: int) -> str|bool:
    apellido = get_str_len(f"Ingrese apellido (Max. {maximo} caracteres): ", 
               f"Error. Reingrese apellido (Max. {maximo} caracteres): ", 
               minimo, maximo, reintentos)
    
    return apellido

def pedir_edad(minimo: int, maximo: int, reintentos: int) -> int|bool:
    edad = get_int(f"Ingrese edad (Min: {minimo} - Max: {maximo}): ", 
           f"Error. Reingrese edad (Min: {minimo} - Max: {maximo}): ", 
           minimo, maximo, reintentos)
    
    return edad

def pedir_altura(minimo: int, maximo: int, reintentos: int) -> int|bool:
    altura = get_int(f"Ingrese altura(cm) (Min: {minimo} - Max: {maximo}): ", 
             f"Error. Reingrese altura(cm) (Min: {minimo} - Max: {maximo}): ", 
             minimo, maximo, reintentos)
    
    return altura

def pedir_peso(minimo: float, maximo: float, reintentos: int) -> float|bool:
    peso = get_float(f"Ingrese peso(Kg) (Sin comas, solo puntos|Min: {minimo} - Max: {maximo}): ", 
           f"Error. Reingrese peso (Min: {minimo} - Max: {maximo}): ", 
           minimo, maximo, reintentos)
    
    return peso

def pedir_dni(minimo: int, maximo: int, reintentos: int) -> int|bool:
    dni = get_validate_dni(f"Ingrese DNI (Sin comas, ni puntos| Min: {minimo} - Max: {maximo}): ", 
          f"Error. Reingrese DNI (Min:{minimo}-Max:{maximo}): ", 
          minimo, maximo, reintentos)
    

    return dni

def pedir_grupo_sanguineo(lista: list, reintentos: int) -> str|bool:
    grupo_sanguineo = get_str_search("Ingrese grupo sanguíneo: ", 
                      "Error. Grupo sanguíneo inexistente, reingrese: ",
                      lista, reintentos)
    
    return grupo_sanguineo

def pedir_flujo_ordenamiento(lista: list, reintentos: int) -> str|bool:
    flujo = get_str_search("Elija el flujo de ordenamiento (ASCENDENTE-DESCENDENTE): ", 
                          "Error. Ingrese (ASCENDENTE-DESCENDENTE): ", 
                          lista, reintentos)
    return flujo
#endregion

#region Método string propio
def metodo_title(cadena: str) -> str:
    palabras = cadena.split()
    palabras_titulo = []
    
    for palabra in palabras:
        if palabra:
            palabra_titulo = palabra[0].upper() + palabra[1:].lower()
            palabras_titulo.append(palabra_titulo)
    cadena_titulo = " ".join(palabras_titulo)
    return cadena_titulo
#endregion