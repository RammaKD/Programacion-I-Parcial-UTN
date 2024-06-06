# def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reitentos: int) -> float|bool:
#     contador_reitentos = 0
#     numero_validado = False
    
#     while contador_reitentos <= reitentos:
#         numero = input((mensaje)).replace(",", ".")
#         numero = float(numero)
#         numero_validado = validate_number(numero, minimo, maximo)
        
#         if numero_validado:                            
#             numero_validado = numero
#             break
#         else:
#             contador_reitentos += 1
#             mensaje = mensaje_error

#     return numero_validado

# def validate_number(numero: int|float, minimo: int|float, maximo: int|float) -> int|float|bool:
#     if numero < minimo or numero > maximo:
#         validacion = False
#     else:
#         validacion = numero

#     return validacion


# peso = get_float("ingrese peso: ", "error reingrese: ", 10, 300, 3)
# print(peso)