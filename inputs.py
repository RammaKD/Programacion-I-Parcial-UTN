#region Get
def get_str_len(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> str|bool:
    contador_reintentos = 0
    cadena_validada = False
    
    while contador_reintentos <= reintentos:
        cadena = input(mensaje).strip()
  
        if cadena.isalpha():
            cadena_validada = validate_lenght(cadena, minimo, maximo)
            if cadena_validada:
                cadena_validada = cadena.capitalize()
                break
            else:
                contador_reintentos += 1
                mensaje = mensaje_error
        else:
            contador_reintentos += 1
            mensaje = "Error. Ingrese solo caracteres alfabéticos y un solo dato: "
    
    return cadena_validada

def get_str_search(mensaje: str, mensaje_error: str, lista: list, reintentos: int) -> str|bool:
    contador_reintentos = 0
    cadena_validada = False
    
    while contador_reintentos <= reintentos:
        cadena = input(mensaje).upper()
        if validate_string_search(cadena, lista):
            cadena_validada = cadena
            break
        else:
            contador_reintentos += 1
            mensaje = mensaje_error

    return cadena_validada

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reitentos: int) -> int|bool:
    contador_reintentos = 0
    numero_validado = False
    
    while contador_reintentos <= reitentos:
        numero = input(mensaje).strip()
        try:
            numero = int(numero)
            if validate_range(numero, minimo, maximo):
                numero_validado = numero
                break
            else:
                contador_reintentos += 1
                mensaje = mensaje_error
        except:
            contador_reintentos += 1
            mensaje = "Error. Ingrese solo caracteres numéricos y un solo dato: "

    return numero_validado
                                     
def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float|bool:
    contador_reintentos = 0
    numero_validado = False
    
    while contador_reintentos <= reintentos:
        numero = input(mensaje).strip()
        try:
            numero = float(numero)
            if validate_range(numero, minimo, maximo):
                numero_validado = numero
                break
            else:
                contador_reintentos += 1
                mensaje = mensaje_error
        except:
            contador_reintentos += 1
            mensaje = "Error. Ingrese solo caracteres numéricos y un solo dato: "

    return numero_validado
                                       
def get_validate_dni(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|bool:
    contador_reintentos = 0
    numero_validado = False

    while contador_reintentos <= reintentos:
        numero = input(mensaje).strip().zfill(8)
        try:
            numero = int(numero)
            if validate_range(numero, minimo, maximo):
                numero_validado = numero
                break
            else:
                contador_reintentos += 1
                mensaje = mensaje_error
        except:
            contador_reintentos += 1
            mensaje = "Error. Ingrese solo caracteres númericos y un solo dato: "

    return numero_validado
#endregion

#region Validate
def validate_lenght(cadena: str, minimo: int, maximo: int) -> str|bool:
    if len(cadena) < minimo or len(cadena) > maximo:
        validacion = False
    else:
        validacion = cadena
    return validacion

def validate_string_search(cadena: str, lista: list) -> str|bool:
    validacion = False
    for elemento in lista:
        if elemento == cadena:
            validacion = cadena
            break
    
    return validacion

def validate_range(numero: int|float, minimo: int|float, maximo: int|float) -> int|float|bool:
    if numero < minimo or numero > maximo:
        validacion = False
    else:
        validacion = numero

    return validacion
#endregion 

#region Inputs específicos
def pedir_nombre(minimo, maximo, reintentos):
    nombre = get_str_len(f"Ingrese nombre (Max. {maximo} caracteres): ", 
             f"Error. Reingrese nombre (Max. {maximo} caracteres): ", 
             minimo, maximo, reintentos)
    
    return nombre

def pedir_apellido(minimo, maximo, reintentos):
    apellido = get_str_len(f"Ingrese apellido (Max. {maximo} caracteres): ", 
               f"Error. Reingrese apellido (Max. {maximo} caracteres): ", 
               minimo, maximo, reintentos)
    
    return apellido

def pedir_edad(minimo, maximo, reintentos):
    edad = get_int(f"Ingrese edad (Min: {minimo} - Max: {maximo}): ", 
           f"Error. Reingrese edad (Min: {minimo} - Max: {maximo}): ", 
           minimo, maximo, reintentos)
    
    return edad

def pedir_altura(minimo, maximo, reintentos):
    altura = get_int(f"Ingrese altura(cm) (Min: {minimo} - Max: {maximo}): ", 
             f"Error. Reingrese altura(cm) (Min: {minimo} - Max: {maximo}): ", 
             minimo, maximo, reintentos)
    
    return altura

def pedir_peso(minimo, maximo, reintentos):
    peso = get_float(f"Ingrese peso(Kg) (Sin comas, solo puntos|Min: {minimo} - Max: {maximo}): ", 
           f"Error. Reingrese peso (Min: {minimo} - Max: {maximo}): ", 
           minimo, maximo, reintentos)
    
    return peso

def pedir_dni(minimo, maximo, reintentos):
    dni = get_validate_dni(f"Ingrese DNI (Sin comas, ni puntos| Min: {minimo} - Max: {maximo}): ", 
          f"Error. Reingrese DNI (Min:{minimo}-Max:{maximo}): ", 
          minimo, maximo, reintentos)
    
    return dni

def pedir_grupo_sanguineo(lista, reintentos):
    grupo_sanguineo = get_str_search("Ingrese grupo sanguíneo: ", 
                      "Error. Grupo sanguíneo inexistente, reingrese: ",
                      lista, reintentos)
    
    return grupo_sanguineo

def pedir_flujo_ordenamiento(lista, reintentos):
    flujo = get_str_search("Elija el flujo de ordenamiento (ASCENDENTE-DESCENDENTE): ", 
                          "Error. Ingrese (ASCENDENTE-DESCENDENTE): ", 
                          lista, reintentos)
    return flujo

#endregion