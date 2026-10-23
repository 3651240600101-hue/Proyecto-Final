# validaciones.py

def validar_numero_en_base(cadena, base):
    """
    Valida que la cadena sea un entero no negativo de hasta 128 dígitos
    y que sus caracteres correspondan a la base indicada.
    Retorna: (es_valido: bool, mensaje_error: str)
    """
    if len(cadena) == 0:
        return False, "Error: La entrada no puede estar vacía."
    
    if len(cadena) > 128:
        return False, "Error: El número excede el límite máximo de 128 dígitos."
    
    # Verificar que no tenga espacios ni signos ni prefijos
    for caracter in cadena:
        if caracter == " ":
            return False, "Error: No se permiten espacios en blanco."
        if caracter in ["+", "-", ".", ","]:
            return False, "Error: No se permiten signos ni números fraccionarios."

    if len(cadena) >= 2 and cadena[0] == "0" and cadena[1] in ["x", "X", "b", "B", "o", "O"]:
        return False, "Error: No se permiten prefijos de base (como 0x, 0b, 0o)."

    # Definir caracteres permitidos según la base
    if base == 2:
        permitidos = "01"
        nombre_base = "Binario (solo 0 y 1)"
    elif base == 8:
        permitidos = "01234567"
        nombre_base = "Octal (dígitos del 0 al 7)"
    elif base == 10:
        permitidos = "0123456789"
        nombre_base = "Decimal (dígitos del 0 al 9)"
    elif base == 16:
        permitidos = "0123456789ABCDEFabcdef"
        nombre_base = "Hexadecimal (dígitos 0-9 y letras A-F)"
    else:
        return False, "Error: Base desconocida."

    for caracter in cadena:
        if caracter not in permitidos:
            return False, f"Error: El carácter '{caracter}' no es válido en el sistema {nombre_base}."

    return True, ""


def normalizar_mayusculas(cadena):
    """
    Convierte letras minúsculas (a-f) a mayúsculas (A-F) manualmente o con .upper()
    """
    return cadena.upper()