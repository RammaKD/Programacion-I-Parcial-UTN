#region Funciones Get()
def get_str_find(mensaje: str, mensaje_error: str, lista: list, reintentos: int) -> str|bool:
    contador_reitentos = 0
    cadena_validada = False
    while contador_reitentos <= reintentos:
        cadena = input(mensaje).upper()
        cadena_validada = validate_find_string(cadena, lista)
        if cadena_validada:
            cadena_validada = cadena
            break
        else:
            contador_reitentos += 1
            mensaje = mensaje_error


    return cadena_validada

def get_str_len(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int:
    contador_reitentos = 0
    cadena_validada = False
    while contador_reitentos <= reintentos:
        cadena_original = input(mensaje)
        cadena_sin_espacios = cadena_original.replace(" ", "")
        if cadena_sin_espacios.isalpha():
            cadena_validada = validate_lenght(cadena_sin_espacios.strip(""), minimo, maximo)
            if cadena_validada:
                cadena_validada = cadena_original.title()
                break
            else:
                contador_reitentos += 1
                mensaje = mensaje_error
        else:
            contador_reitentos += 1
            mensaje = mensaje_error
    
    return cadena_validada

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reitentos: int) -> int|bool:
    contador_reitentos = 0
    numero_validado = False
    
    while contador_reitentos <= reitentos:
        numero = input((mensaje))
        if numero.isdigit():
            numero = int(numero)
            numero_validado = validate_number(numero, minimo, maximo)
            
            if numero_validado:                            
                numero_validado = numero
                break
            else:
                contador_reitentos += 1
                mensaje = mensaje_error
        else:
            contador_reitentos += 1
            mensaje = mensaje_error

    return numero_validado

def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reitentos: int) -> float|bool:
    contador_reitentos = 0
    numero_validado = False
    
    while contador_reitentos <= reitentos:
        numero = input((mensaje)).replace(",", ".")
        try:
            numero = float(numero)
            numero_validado = validate_number(numero, minimo, maximo)
            
            if numero_validado:                            
                numero_validado = numero
                break
            else:
                contador_reitentos += 1
                mensaje = mensaje_error
        except:
            contador_reitentos += 1
            mensaje = mensaje_error

    return numero_validado

def get_str(mensaje: str, mensaje_error: str, reintentos: int) -> str|bool:
    contador_reintentos = 0
    cadena_validada = False 
    while contador_reintentos <= reintentos:
        cadena = input(mensaje)
        
        if cadena.isalpha():
            cadena_validada = cadena
            break
        
        else:
            contador_reintentos += 1
            mensaje = mensaje_error

    return cadena_validada
#endregion

#region Funciones Validate()
def validate_number(numero: int|float, minimo: int|float, maximo: int|float) -> int|float|bool:
    if numero < minimo or numero > maximo:
        validacion = False
    else:
        validacion = numero

    return validacion

def validate_lenght(cadena: str, minimo: int, maximo: int) -> str|bool:
    if len(cadena) <= minimo or len(cadena) >= maximo:
        validacion = False
    else:
        validacion = cadena
    return validacion

def validate_find_string(cadena: str, lista: int) -> str|bool:
    validacion = False
    for elemento in lista:
        if elemento == cadena:
            validacion = cadena
            break

    return validacion
#endregion 