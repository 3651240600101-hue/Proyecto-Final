# main.py
from validaciones import validar_numero_en_base, normalizar_mayusculas
from conversiones import obtener_nombre_base, convertir_entre_bases
from historial import agregar_al_historial, mostrar_menu_historial
from practica import ejecutar_modo_practica

def seleccionar_base_origen():
    """Muestra el menú para elegir la base de origen y retorna la base (2, 8, 10, 16) o 0 para volver."""
    mapa_opciones = {"1": 2, "2": 8, "3": 10, "4": 16}
    while True:
        print("\n========================================================")
        print("SELECCIONE LA BASE DE ORIGEN")
        print("========================================================")
        print("1. Binario")
        print("2. Octal")
        print("3. Decimal")
        print("4. Hexadecimal")
        print("0. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "0":
            return 0
        elif opcion in mapa_opciones:
            return mapa_opciones[opcion]
        else:
            print("Error: Opción inexistente o inválida. Intente de nuevo.")


def seleccionar_base_destino(base_origen):
    """
    Muestra únicamente las bases diferentes a 'base_origen' para evitar
    que el usuario seleccione la misma base como origen y destino.
    """
    todas_las_bases = [2, 8, 10, 16]
    bases_permitidas = []
    for b in todas_las_bases:
        if b != base_origen:
            bases_permitidas.append(b)
            
    while True:
        print("\n========================================================")
        print("SELECCIONE LA BASE DE DESTINO")
        print("========================================================")
        indice = 1
        for b in bases_permitidas:
            print(f"{indice}. {obtener_nombre_base(b)}")
            indice += 1
        print("0. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "0":
            return 0
        elif opcion in ["1", "2", "3"]:
            idx = int(opcion) - 1
            return bases_permitidas[idx]
        else:
            print("Error: Opción inexistente o inválida. Intente de nuevo.")


def flujo_realizar_conversion(lista_historial):
    """Gestiona el flujo completo de una conversión."""
    base_origen = seleccionar_base_origen()
    if base_origen == 0:
        return
        
    base_destino = seleccionar_base_destino(base_origen)
    if base_destino == 0:
        return
        
    nombre_origen = obtener_nombre_base(base_origen)
    nombre_destino = obtener_nombre_base(base_destino)
    
    while True:
        print("\n========================================================")
        print(f"CONVERSIÓN: {nombre_origen.upper()} A {nombre_destino.upper()}")
        print("========================================================")
        print("Ingrese un entero no negativo de hasta 128 dígitos.")
        print("Escriba 'volver' para regresar al menú principal.")
        
        entrada = input("Número a convertir: ").strip()
        if entrada.lower() == "volver":
            return
            
        es_valido, mensaje_error = validar_numero_en_base(entrada, base_origen)
        if not es_valido:
            print(f"\n{mensaje_error}")
            print("Por favor, ingrese un valor válido.")
        else:
            break
            
    entrada_normalizada = normalizar_mayusculas(entrada)
    resultado, pasos = convertir_entre_bases(entrada_normalizada, base_origen, base_destino)
    
    print("\n========================================================")
    print("RESULTADO")
    print("========================================================")
    print(f"Número ingresado: {entrada_normalizada}")
    print(f"Base de origen: {nombre_origen}")
    print(f"Base de destino: {nombre_destino}")
    print(f"Resultado: {resultado}")
    
    print("\n========================================================")
    print("PROCEDIMIENTO PASO A PASO")
    print("========================================================")
    for linea in pasos:
        print(linea)
        
    agregar_al_historial(lista_historial, entrada_normalizada, nombre_origen, nombre_destino, resultado)
    print("\nConversión agregada al historial.")
    input("Presione Enter para continuar...")


def menu_principal():
    """Ciclo principal del programa."""
    lista_historial = []
    estadisticas_practica = {"aciertos": 0, "respondidos": 0}
    
    while True:
        print("\n========================================================")
        print("CONVERSOR DE SISTEMAS NUMÉRICOS")
        print("========================================================")
        print("1. Realizar una conversión")
        print("2. Consultar el historial")
        print("3. Iniciar el modo de práctica")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            flujo_realizar_conversion(lista_historial)
        elif opcion == "2":
            mostrar_menu_historial(lista_historial)
        elif opcion == "3":
            ejecutar_modo_practica(estadisticas_practica)
        elif opcion == "4":
            print("\nGracias por utilizar el Conversor de Sistemas Numéricos. ¡Hasta pronto!")
            break
        else:
            print("\nError: Opción inválida. Por favor ingrese un número del 1 al 4.")


if __name__ == "__main__":
    menu_principal()