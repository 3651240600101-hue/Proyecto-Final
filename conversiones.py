# conversiones.py

def obtener_nombre_base(base):
    if base == 2:
        return "Binario"
    elif base == 8:
        return "Octal"
    elif base == 10:
        return "Decimal"
    elif base == 16:
        return "Hexadecimal"
    return ""


def caracter_a_valor(caracter):
    """Convierte un carácter ('0'-'9', 'A'-'F') a su valor numérico entero."""
    digitos = "0123456789ABCDEF"
    indice = 0
    for d in digitos:
        if d == caracter.upper():
            return indice
        indice += 1
    return 0


def valor_a_caracter(valor):
    """Convierte un valor entero (0-15) a su representación en carácter ('0'-'9', 'A'-'F')."""
    digitos = "0123456789ABCDEF"
    return digitos[valor]


def hacia_decimal(numero_str, base_origen):
    """
    Convierte un número desde 'base_origen' (2, 8 o 16) a Decimal (base 10)
    utilizando el algoritmo de Notación Posicional.
    Retorna: (valor_decimal: int, pasos: list[str])
    """
    pasos = []
    nombre_origen = obtener_nombre_base(base_origen).upper()
    pasos.append(f"ETAPA: {nombre_origen} A DECIMAL")
    
    longitud = len(numero_str)
    suma_total = 0
    posicion = 0
    
    # Recorrer de derecha a izquierda (desde el último carácter hasta el primero)
    indice = longitud - 1
    while indice >= 0:
        digito_char = numero_str[indice]
        valor_digito = caracter_a_valor(digito_char)
        potencia = base_origen ** posicion
        aporte = valor_digito * potencia
        suma_total += aporte
        
        if base_origen == 16:
            pasos.append(f"{digito_char} (valor {valor_digito}) x {base_origen}^{posicion} = {aporte}")
        else:
            pasos.append(f"{digito_char} x {base_origen}^{posicion} = {aporte}")
            
        posicion += 1
        indice -= 1
        
    pasos.append(f"Suma de los aportes: {suma_total}")
    return suma_total, pasos


def desde_decimal(numero_decimal, base_destino):
    """
    Convierte un número entero Decimal a 'base_destino' (2, 8 o 16)
    utilizando el algoritmo de Divisiones Sucesivas.
    Retorna: (resultado_str: str, pasos: list[str])
    """
    pasos = []
    nombre_destino = obtener_nombre_base(base_destino)
    pasos.append(f"ETAPA: DECIMAL A {nombre_destino.upper()}")
    
    if numero_decimal == 0:
        pasos.append(f"0 / {base_destino}: cociente = 0, residuo = 0, dígito = 0")
        pasos.append("Resultado directo para el valor cero: 0")
        return "0", pasos
        
    actual = numero_decimal
    residuos_chars = []
    
    while actual > 0:
        cociente = actual // base_destino
        residuo = actual % base_destino
        digito_char = valor_a_caracter(residuo)
        
        pasos.append(f"{actual} / {base_destino}: cociente = {cociente}, residuo = {residuo}, dígito = {digito_char}")
        residuos_chars.append(digito_char)
        actual = cociente
        
    # Construir el resultado leyendo los residuos del último al primero
    resultado_str = ""
    indice = len(residuos_chars) - 1
    while indice >= 0:
        resultado_str += residuos_chars[indice]
        indice -= 1
        
    pasos.append(f"Leer los residuos del último al primero: {resultado_str}")
    pasos.append(f"Resultado final en {nombre_destino}: {resultado_str}")
    return resultado_str, pasos


def convertir_entre_bases(numero_str, base_origen, base_destino):
    """
    Coordina cualquiera de las 12 conversiones entre bases diferentes.
    Si ninguna de las dos bases es 10, utiliza Decimal como base intermedia.
    Retorna: (resultado_str: str, lista_pasos: list[str])
    """
    numero_limpio = numero_str.upper()
    todos_los_pasos = []
    
    # Caso 1: Origen es Decimal (10) -> Destino (2, 8, 16)
    if base_origen == 10:
        valor_dec = int(numero_limpio)
        resultado, pasos_div = desde_decimal(valor_dec, base_destino)
        # Ajustar encabezado a ETAPA 1
        pasos_div[0] = f"ETAPA 1: DECIMAL A {obtener_nombre_base(base_destino).upper()}"
        todos_los_pasos.extend(pasos_div)
        return resultado, todos_los_pasos
        
    # Caso 2: Origen (2, 8, 16) -> Destino es Decimal (10)
    elif base_destino == 10:
        valor_dec, pasos_pos = hacia_decimal(numero_limpio, base_origen)
        pasos_pos[0] = f"ETAPA 1: {obtener_nombre_base(base_origen).upper()} A DECIMAL"
        pasos_pos.append(f"Resultado final en Decimal: {valor_dec}")
        todos_los_pasos.extend(pasos_pos)
        return str(valor_dec), todos_los_pasos
        
    # Caso 3: Origen y Destino son distintos de Decimal (usa Decimal como base intermedia)
    else:
        valor_dec, pasos_etapa1 = hacia_decimal(numero_limpio, base_origen)
        pasos_etapa1[0] = f"ETAPA 1: {obtener_nombre_base(base_origen).upper()} A DECIMAL"
        
        resultado, pasos_etapa2 = desde_decimal(valor_dec, base_destino)
        pasos_etapa2[0] = f"ETAPA 2: DECIMAL A {obtener_nombre_base(base_destino).upper()}"
        
        todos_los_pasos.extend(pasos_etapa1)
        todos_los_pasos.append("") # Línea en blanco para separar etapas
        todos_los_pasos.extend(pasos_etapa2)
        return resultado, todos_los_pasos