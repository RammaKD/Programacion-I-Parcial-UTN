def desea_continuar(mensaje:str, mensaje_error: str) -> bool:
    continuar = input(mensaje).lower()
    while continuar != "si" and continuar != "no":
        continuar = input(mensaje_error).lower()
    if continuar == "si":
        bandera_salir = True
    else:
        bandera_salir = False
    
    return bandera_salir

def seleccionar_opcion_menu(mensaje: str) -> int:
    try:
        opciones_menu = int(input(mensaje))
    except:
        opciones_menu = -1

    return opciones_menu

def comprobar_len_lista(lista: list) -> bool:
    if len(lista) == 0:
        lenght = False
    else:
        lenght = True
    
    return lenght

def encontrar_ultimo_valor_en_clave(lista_diccionarios: list[dict], clave: str) -> int:
    valor = 0
    for diccionario in lista_diccionarios:
        posible_valor = diccionario.get(clave, 0)
        if posible_valor != 0:
            valor = int(posible_valor)
    return valor

def incrementar_id (lista_diccionarios:list[dict]) -> int:
    ultimo_id = encontrar_ultimo_valor_en_clave(lista_diccionarios, "id")
    id_incrementado = ultimo_id + 1
    return id_incrementado

def crear_lista_keys(lista_diccionarios: list[dict]) -> list:
    claves_unicas = set()
    for empleado in lista_diccionarios:
        claves_unicas.update(empleado.keys())
    lista_parametros = list(claves_unicas)

    return lista_parametros